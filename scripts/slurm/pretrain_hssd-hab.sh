#!/bin/zsh
#SBATCH --job-name=fp-objectnav-v0.2.3
#SBATCH --output=slurm.out
#SBATCH --error=slurm.err
#SBATCH --gpus 4
#SBATCH --nodes 1
#SBATCH --cpus-per-task 16
#SBATCH --ntasks-per-node 4
#SBATCH --partition=short
#SBATCH --constraint=a40

MAIN_ADDR=$(srun --ntasks=1 hostname 2>&1 | tail -n1)
export MAIN_ADDR
export CUDA_LAUNCH_BLOCKING=1

source ~/.zshrc
conda activate <ENV_NAME>
cd /path/to/habitat-lab

export GLOG_minloglevel=2
export MAGNUM_LOG=quiet
export HABITAT_SIM_LOG=quiet
export PYTHONPATH=$PYTHONPATH:./

srun python -u habitat-baselines/habitat_baselines/run.py --exp-config habitat-baselines/habitat_baselines/config/objectnav/hssd-200_ver_clip_hssd-hab.yaml --run-type train
