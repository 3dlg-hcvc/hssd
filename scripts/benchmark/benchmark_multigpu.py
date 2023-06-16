#!/usr/bin/env python3

# Copyright (c) Meta Platforms, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.


import argparse
import numpy as np
import time
import os, tqdm

import demo_runner as dr

import torch.multiprocessing as mp
import os

def benchmark_scene(rank, args, scene, result_queue):

    default_settings = dr.default_sim_settings.copy()
    default_settings["scene_dataset_config_file"] = args.scene_dataset_config
    default_settings["gpu_device_id"] = rank
    default_settings["scene"] = scene
    default_settings["silent"] = True
    default_settings["seed"] = args.seed

    default_settings["save_png"] = False
    default_settings["print_semantic_scene"] = False
    default_settings["print_semantic_mask_stats"] = False
    default_settings["compute_shortest_path"] = False
    default_settings["compute_action_shortest_path"] = False

    default_settings["max_frames"] = args.max_frames
    default_settings["frustum_culling"] = not args.disable_frustum_culling

    benchmark_items = {
        "rgb": {},
    }
    if args.benchmark_semantic_sensor:
        benchmark_items["semantic_only"] = {
            "color_sensor": False,
            "semantic_sensor": True,
        }
        benchmark_items["rgbd_semantic"] = {
            "depth_sensor": True,
            "semantic_sensor": True,
        }

    if args.enable_physics:
        # TODO: cannot benchmark physics with no sensors as this won't create a renderer or load the scene.
        # benchmark_items["enable_physics_no_obs"] = {"color_sensor": False, "enable_physics": True}
        benchmark_items["phys_rgb"] = {"enable_physics": True}
        benchmark_items["phys_rgbd"] = {"depth_sensor": True, "enable_physics": True}
        default_settings["num_objects"] = args.num_objects
        default_settings["test_object_index"] = args.test_object_index

    default_settings["num_processes"] = args.num_procs
    performance = []
    default_settings["width"] = default_settings["height"] = args.resolution
    perf = {}
    for key, value in benchmark_items.items():
        demo_runner = dr.DemoRunner(
            default_settings, dr.DemoRunnerType.BENCHMARK
        )
        print(" ---------------------- %s ------------------------ " % key)
        settings = default_settings.copy()
        settings.update(value)
        perf[key] = demo_runner.benchmark(rank, settings)
        print(
            " ====== FPS (%d x %d, %s): %0.1f ======"
            % (settings["width"], settings["height"], key, perf[key].get("fps"))
        )
    performance.append(perf)
    
    print(
        " ================ Performance (FPS) NPROC={} rank={} ===================================".format(
            args.num_procs, rank
        )
    )
    title = "Resolution "
    for key in perf:
        title += "\t%-10s" % key
    print(title)
    for idx in range(len(performance)):
        row = "%d x %d" % (args.resolution, args.resolution)
        for value in performance[idx].values():
            row += "\t%-8.1f" % value.get("fps")
        print(row)
    print(
        " =============================================================================="
    )

    result_queue.put(performance)

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Running benchmarks on simulator")
    parser.add_argument("--scene_dataset_config", type=str, required=True)
    parser.add_argument("--scene_split", type=str, default=dr.default_sim_settings["scene"])
    parser.add_argument(
        "--max_frames",
        type=int,
        default=2000,
        help="Max number of frames simulated."
        "Default or larger value is suggested for accurate results.",
    )
    parser.add_argument(
        "--resolution",
        type=int,
        default=224,
        help="Resolution r for frame (r x r).",
    )
    parser.add_argument(
        "--num_procs",
        type=int,
        default=1,
        help="Number of concurrent processes.",
    )
    parser.add_argument(
        "--n_gpu",
        type=int,
        default=1,
        help="Number of gpus",
    )
    parser.add_argument(
        "--benchmark_semantic_sensor",
        action="store_true",
        help="Whether to enable benchmarking of semantic sensor.",
    )
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument(
        "--enable_physics",
        action="store_true",
        help="Whether to enable physics (kinematic by default or dynamics if installed with bullet) during benchmark or not.",
    )
    parser.add_argument(
        "--num_objects",
        type=int,
        default=10,
        help="Number of objects to spawn if enable_physics is true.",
    )
    parser.add_argument(
        "--test_object_index",
        type=int,
        default=0,
        help="Index the objects to spawn if enable_physics is true. -1 indicates random.",
    )
    parser.add_argument(
        "--disable_frustum_culling",
        action="store_true",
        help="Disable frustum culling (default is enabled)",
    )
    args = parser.parse_args()

    simset = dr.default_sim_settings.copy()

    with open(args.scene_split, 'r') as fp:
        SCENES = [x.strip() for x in fp.readlines()]

    start = time.time()
    scene_perf = {}
    split_name = os.path.basename(args.scene_split).split('.txt')[0]

    for scene in tqdm.tqdm(SCENES):
        result_queue = mp.Queue()
        for rank in range(args.n_gpu):
            mp.Process(target=benchmark_scene, args=(rank, args, scene, result_queue)).start()

        scene_perf[scene] = 0.
        for _ in range(args.n_gpu):
            proc_result = result_queue.get()
            assert len(proc_result) == 1
            scene_perf[scene] += proc_result[0]['rgb']['fps']

        with open(f'{split_name}_{args.n_gpu}_{args.num_procs}_progress.txt', 'a') as fp:
            fp.write(f"{scene} : {scene_perf[scene]}\n")
    
    end = time.time()

    scene_fps = []
    for sc, fps in scene_perf.items():
        scene_fps.append(fps)

    print(f'{np.mean(scene_fps)} +- {np.std(scene_fps)}')
    print('TIME TAKEN: ', end - start)
