import argparse
import glob
import os
import shutil


def copy_cfg_files(src_folder: str, dest_folder: str):
    src_files = glob.glob(src_folder)
    for file in src_files:
        shutil.copy(file, dest_folder)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--hab-lab-path", type=str, required=True, help="path to habitat-lab"
    )
    args = parser.parse_args()

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
