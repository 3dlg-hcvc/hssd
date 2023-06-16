FPS Benchmarking
==================================

Here, we present the code to reproduce the FPS Benchmarking results in the paper. 

To reproduce the numbers in Table. 2 of the paper, run the following command.

```
python benchmark_multigpu.py --scene_dataset_config /path/to/ai2thor-hab/ai2thor.scene_dataset_config.json --scene_split splits/small_set.txt --resolution 224 --num_procs 15 --n_gpu 1
```

This should produce a file named `small_set_1_15_progress.txt`. 
To get the average run, 
```
python average.py --file_path small_set_1_15_progress.txt 
```

Similarly, re-run the process with `n_gpu=1, num_proc=1` and `n_gpu=8, num_procs=15`.