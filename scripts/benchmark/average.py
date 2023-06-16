import numpy as np
import os
import argparse

def compute_average(results):
    return np.mean(results), np.std(results)

def load_result(file_path):

    with open(file_path, 'r') as fp:
        lines = [x.strip() for x in fp.readlines()]

    scene_res = {}
    for l in lines:
        scene, fps = l.split(' : ')
        scene_res[scene] = float(fps) 
    
    results = [scene_res[x] for x in scene_res]
    return results

def main(args):

    split_results = load_result(args.file_path)
    split_avg, split_std = compute_average(split_results)
    print(f"{os.path.basename(args.file_path)}: {np.round(split_avg)} +- {np.round(split_std)}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, required=True)
    args = parser.parse_args()
    main(args)
