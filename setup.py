import argparse
import glob
import os
import shutil


def copy_cfg_files(src_folder: str, dest_folder: str):
    src_files = glob.glob(src_folder)
    for file in src_files:
        shutil.copy(file, dest_folder)
    
    print(f"Copied files from `{src_folder}` to `{dest_folder}`.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hab-lab-path", type=str, required=True, help="path to habitat-lab"
    )
    args = parser.parse_args()

    # copy dataset configs
    src_folder = "configs/dataset/*"
    dest_folder = os.path.join(
        args.hab_lab_path, "../habitat-lab/habitat-lab/habitat/config/habitat/dataset/objectnav"
    )
    copy_cfg_files(src_folder, dest_folder)

    # copy task specs
    src_folder = "configs/task/*"
    dest_folder = os.path.join(
        args.hab_lab_path, "habitat-lab/habitat/config/benchmark/nav/objectnav/"
    )
    copy_cfg_files(src_folder, dest_folder)

    # copy pretraining configs
    src_folder = "configs/pretraining/*"
    dest_folder = os.path.join(
        args.hab_lab_path, "habitat-baselines/habitat_baselines/config/objectnav"
    )
    copy_cfg_files(src_folder, dest_folder)

    # copy zero-shot eval configs
    src_folder = "configs/eval/zero-shot/*"
    dest_folder = os.path.join(
        args.hab_lab_path, "habitat-baselines/habitat_baselines/config/objectnav"
    )
    copy_cfg_files(src_folder, dest_folder)