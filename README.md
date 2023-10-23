HSSD: Habitat Synthetic Scene Dataset
==================================

[![arXiv](https://img.shields.io/badge/cs.cv-arXiv%3A1912.11463-42ba94.svg)](https://arxiv.org/abs/2306.11290)


This repository serves as a guide for training and evaluating ObjectNav agents in HSSD, AI2THOR, and HM3D scene datasets using Habitat, and reproducing experiments provided in the HSSD paper.

`Habitat Synthetic Scenes Dataset (HSSD): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation`


https://github.com/3dlg-hcvc/hssd/assets/24846546/879d2a36-870f-4ea9-b7cd-f0a9002da056



## Table of contents

- [About](#about)
- [Pre-requisites](#pre-requisites)
- [Scene datasets](#scene-datasets)
    - [HSSD](#hssd)
    - [ProcTHOR-HAB](#optional-procthor-hab)
    - [HM3D-semantics](#optional-hm3d-semantics)
- [ObjectNav episode datasets](#objectnav-episode-datasets)
- [Training and evaluation setup](#training-and-evaluation-setup)
- [Training and evaluation commands](#training-and-evaluation-commands)



## About

> We contribute the Habitat Synthetic Scenes Dataset, a dataset of 211 high-quality 3D scenes, and use it to test navigation agent generalization to realistic 3D environments. Our dataset represents real interiors and contains a diverse set of 18,656 models of real-world objects. We investigate the impact of synthetic 3D scene dataset scale and realism on the task of training embodied agents to find and navigate to objects (ObjectGoal navigation).


## Pre-requisites

To load HSSD and other scene datasets in simulation and train and evlaute embodied agents in them, you will need to install:

- [Habitat-lab (`v0.2.3_hssd` branch)](https://github.com/facebookresearch/habitat-lab/tree/v0.2.3_hssd)
- [Habitat-sim (`v0.2.3_hssd` branch)](https://github.com/facebookresearch/habitat-sim/tree/v0.2.3_hssd): build from source.
- [CLIP](https://github.com/openai/CLIP) (`pip install git+https://github.com/openai/CLIP.git@40f5484c1c74edd83cb9cf687c6ab92b28d8b656`)

Note: Even though the HSSD scene dataset is compatible with the latest habitat-sim and habitat-lab versions, the results in the paper were reported using `v0.2.3_hssd` branch of both habitat libraries.

## Scene datasets

### HSSD:

HSSD has been hosted on HuggingFace at [huggingface.co/datasets/hssd/hssd-hab](https://huggingface.co/datasets/hssd/hssd-hab). Here, you can preview the dataset and find information about the folder structure and instructions on getting started.

For conveniently running subsequent training and evaluation experiments, you can clone the dataset to the following path in your `habitat-lab` installation:

```
cd /path/to/habitat-lab
git clone https://huggingface.co/datasets/hssd/hssd-hab data/scene_datasets/hssd-hab
```

### (Optional) ProcTHOR-HAB: 

You can find Habitat-compatible AI2THOR scene datasets (like ProcTHOR, iTHOR, and RoboTHOR), here: [huggingface.co/datasets/hssd/ai2thor-hab](https://huggingface.co/datasets/hssd/ai2thor-hab).

For conveniently running subsequent training and evaluation experiments, you can clone the dataset to the following path in your `habitat-lab` installation:

```
cd /path/to/habitat-lab
git clone https://huggingface.co/datasets/hssd/ai2thor-hab data/scene_datasets/ai2thor-hab
```

### (Optional) HM3D-semantics: 

To download the HM3D scene dataset, refer to the instructions provided [here](https://github.com/facebookresearch/habitat-sim/blob/main/DATASETS.md#habitat-matterport-3d-research-dataset-hm3d).

## ObjectNav episode datasets

To download episode datasets for HSSD, ProcTHOR-HAB, and HM3D-semantics, you will need to fetch the zipped files from the provided links and extract them to the corresponding paths specified below.

| Task | Scenes | Link | Extract path | Config to use                                                                                                          | Archive size |
| --- | --- | --- | --- |------------------------------------------------------------------------------------------------------------------------| --- |
| [Object goal navigation](https://arxiv.org/abs/2006.13171) | HSSD-hab | [objectnav_hssd-hab_v0.2.3.zip](https://www.dropbox.com/s/26ribfiup5249b8/objectnav_hssd_v0.2.3.zip) | `data/datasets/objectnav/hssd-hab` | [`datasets/objectnav/hssd-hab.yaml`](habitat-lab/habitat/config/habitat/dataset/objectnav/hssd-hab.yaml)                                    | 206 MB |
| [Object goal navigation](https://arxiv.org/abs/2006.13171) | ProcTHOR-HAB | [objectnav_procthor-hab.zip](https://www.dropbox.com/s/mdfpevn1srr37cr/objectnav_procthor-hab.zip) | `data/datasets/objectnav/procthor-hab` | [`datasets/objectnav/procthor-hab.yaml`](habitat-lab/habitat/config/habitat/dataset/objectnav/procthor-hab.yaml)                                    | 755 MB |
| [Object goal navigation](https://arxiv.org/abs/2006.13171) | HM3DSem-v0.2 | [objectnav_hm3d_v2_locobot_multifloor.zip](https://dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/hm3d/v2/objectnav_hm3d_v2_locobot_multifloor.zip) | `data/datasets/objectnav/hm3d/v2/` | [`datasets/objectnav/hm3d_v2.yaml`](habitat-lab/habitat/config/habitat/dataset/objectnav/hm3d_v2.yaml)                                    | 245 MB |


## Training and evaluation setup

Now that you have habitat installed, and the scene and episode datasets downloaded, you are all set to train and evaluate ObjectNav agents in simulation. 

However, to reproduce specific experiments from the HSSD paper – with the specified agent embodiment, camera sensor resolution, and a CLIP visual encoder backbone – you will need Habitat to use the task and training configuration files provided in this repository. 

For your convenience, you can run the script below to conveniently move the necessary config files to appropriate folders in your `habitat-lab` installation directory. This will make it significantly easier to invoke train and eval commands using Habitat.

```
python setup.py --hab-lab-path /path/to/habitat-lab
```

## Training and evaluation commands

Change directory to habitat-lab for successfuly running subsequent commands.

```
cd /path/to/habitat-lab
```

### Pre-train

You can pre-train an ObjectNav agent on HSSD, ProcTHOR-hab, or HM3D, using any variant of the following command:

```
python -u habitat-baselines/habitat_baselines/run.py --exp-config habitat-baselines/habitat_baselines/config/objectnav/hssd-200_ver_clip_{hssd-hab, procthor-hab, hm3d}.yaml --run-type train
```

You can find more information about training runs through checkpoints and tensorboard logs saved here: `/path/to/habitat-lab/data/training/objectnav`.

Note: The above script will run training on 1 GPU. However, all the training experiments in the paper used 4 A40 GPUs and 16 CPU cores per GPU on a SLURM-based compute cluster. To schedule a similar training run, you can start with the sample batch script provided in the `scripts/slurm` directory of this repository – and modify it as per your requirement.

### Evaluate

You can evaluate trained models on val datasets as such:

```
python -u habitat-baselines/habitat_baselines/run.py --exp-config habitat-baselines/habitat_baselines/config/objectnav/hssd-200_ver_clip_{hssd-hab, procthor-hab, hm3d}.yaml --run-type eval habitat_baselines.load_resume_state_config=False
```

This will run evaluation using all training checkpoints. Eval performance metrics can also be visualized through tensorboard logs saved in the path mentioned above. To also save videos of episodes of trained agents, you can add modify the `video_option` flag in the --exp-config file passed above as such:

```
video_option: ["disk"]
```

### Zero-shot evaluate on HM3D-semantics

You can zero-shot evaluate models pre-trained above on HM3D-sem's val datasets as such:

```
python -u habitat-baselines/habitat_baselines/run.py --exp-config habitat-baselines/habitat_baselines/config/objectnav/hssd-200_eval_zeroshot_{hssd-hab, procthor-hab}_to_hm3d.yaml --run-type eval
```

### Fine-tune on HM3D-semantics

To fine-tune models pre-trained on HSSD or ProcTHOR on the HM3D-sem training dataset:

- Update config file `habitat-baselines/habitat_baselines/config/objectnav/hssd-200_hm3d_finetune_ver_clip_{hssd-hab, procthor-hab}.yaml` to specify path to pre-trained weights:

    ```
    pretrained_weights: /path/to/weights_file
    ```

- Finetune by running:

    ```
    python -u habitat-baselines/habitat_baselines/run.py --exp-config habitat-baselines/habitat_baselines/config/objectnav/hssd-200_hm3d_finetune_ver_clip_{hssd-hab, procthor-hab}.yaml --run-type train
    ```

- Evaluate fine-tuned models by running:

    ```
    python -u habitat-baselines/habitat_baselines/run.py --exp-config habitat-baselines/habitat_baselines/config/objectnav/hssd-200_hm3d_finetune_ver_clip_{hssd-hab, procthor-hab}.yaml --run-type eval habitat_baselines.load_resume_state_config=False
    ```

## Citing HSSD

If you use our dataset or find our work useful, please consider citing:

```
@article{khanna2023hssd,
    author={{Khanna*}, Mukul and {Mao*}, Yongsen and Jiang, Hanxiao and Haresh, Sanjay and Shacklett, Brennan and Batra, Dhruv and Clegg, Alexander and Undersander, Eric and Chang, Angel X. and Savva, Manolis},
    title={{Habitat Synthetic Scenes Dataset (HSSD-200): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation}},
    journal={arXiv preprint},
    year={2023},
    eprint={2306.11290},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```
