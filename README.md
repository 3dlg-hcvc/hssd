HSSD: Habitat Synthetic Scene Dataset
==================================

This repository serves as a guide for training and evaluating ObjectNav agents in HSSD, AI2THOR, and HM3D scene datasets using Habitat, and reproducing experiments provided in the following `HSSD-200` paper.

`Habitat Synthetic Scenes Dataset (HSSD-200): An Analysis of 3D Scene Scale and Realism Tradeoffs for ObjectGoal Navigation`

[hssd-teaser-small.webm](https://github.com/3dlg-hcvc/hssd/assets/24846546/1e773001-9f0c-4b8d-a508-ec68d2ff477b)

## About

> We contribute the Habitat-Floorplanner Scenes Dataset, a dataset of 211 high-quality 3D scenes, and use it to test navigation agent generalization to realistic 3D environments. Our dataset represents real interiors and contains a diverse set of 18,656 models of real-world objects. We investigate the impact of synthetic 3D scene dataset scale and realism on the task of training embodied agents to find and navigate to objects (ObjectGoal navigation).


## Pre-requisites

To load HSSD and other scene datasets in simulation and train and evlaute embodied agents in them, you will need to install:

- [Habitat-sim](https://github.com/facebookresearch/habitat-sim#installation)
- [Habitat-lab](https://github.com/facebookresearch/habitat-lab#installation)

## Scene datasets

### HSSD:

HSSD has been hosted on HuggingFace at [https://huggingface.co/hssd/hssd](https://huggingface.co/hssd/hssd). Here, you can preview the dataset and find information about the folder structure and instructions on getting started.

The dataset can be cloned using:

```
git clone https://huggingface.co/datasets/hssd/hssd
```

### (Optional) ProcTHOR-hab: 

To train or evaluate embodied agents on Habitat-compatible ProcTHOR, iTHOR, or RoboTHOR datasets, please download the scene datasets from: https://huggingface.co/datasets/hssd/ai2thor-hab.

### (Optional) HM3D-semantics: 

To download the HM3D scene and episode datasets, refer to the instructione here.

## Episode datasets

| Task | Scenes | Link | Extract path | Config to use                                                                                                          | Archive size |
| --- | --- | --- | --- |------------------------------------------------------------------------------------------------------------------------| --- |
| [Object goal navigation](https://arxiv.org/abs/2006.13171) | HSSD | [objectnav_hssd_v0.2.3.zip](https://www.dropbox.com/s/26ribfiup5249b8/objectnav_hssd_v0.2.3.zip) | `data/datasets/objectnav/hssd_v0.2.3` | [`datasets/objectnav/hssd.yaml`](habitat-lab/habitat/config/habitat/dataset/objectnav/hssd.yaml)                                    | 206 MB |
| [Object goal navigation](https://arxiv.org/abs/2006.13171) | ProcTHOR-hab | [objectnav_procthor-hab.zip](https://www.dropbox.com/s/mdfpevn1srr37cr/objectnav_procthor-hab.zip) | `data/datasets/objectnav/procthor-hab` | [`datasets/objectnav/procthor-hab.yaml`](habitat-lab/habitat/config/habitat/dataset/objectnav/procthor-hab.yaml)                                    | 755 MB |
| [Object goal navigation](https://arxiv.org/abs/2006.13171) | HM3DSem-v0.2 | [objectnav_hm3d_v2.zip](https://dl.fbaipublicfiles.com/habitat/data/datasets/objectnav/hm3d/v2/objectnav_hm3d_v2.zip) | `data/datasets/objectnav/hm3d/v2/` | [`datasets/objectnav/hm3d_v2.yaml`](habitat-lab/habitat/config/habitat/dataset/objectnav/hm3d_v2.yaml)                                    | 245 MB |


## Setup

```
python setup.py --hab-lab-path /path/to/habitat-lab
```

This copies the paper-specific task and training config files to appropriate folders in your habitat-lab installation.

## Commands

### Pre-train

You can pre-train an ObjectNav agent on HSSD, ProcTHOR-hab, or HM3D, using the following command:

```
python -u -m habitat_baselines.run --config-name=objectnav/ddppo_objectnav_hssd.yam
```

### Evaluate

```
python -u -m habitat_baselines.run --config-name=objectnav/ddppo_objectnav_hssd.yaml habitat_baselines.evaluate=True
```

## Citation
