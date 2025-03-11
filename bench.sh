#!/bin/bash

# 1 core
for input_file in "data/input.precise_qa_beta1_mn12_ns99" "data/input.w7x_beta1_mn5_ns51"; do 
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time mpirun -n 1 python run_vmec2000.py ${input_file}
  done

  export OMP_NUM_THREADS=1
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time python run_vmecpp.py ${input_file}
  done
done

# 4 cores
for input_file in "data/input.precise_qa_beta1_mn12_ns99" "data/input.w7x_beta1_mn5_ns51"; do 
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time mpirun -n 4 python run_vmec2000.py ${input_file}
  done

  export OMP_NUM_THREADS=4
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time python run_vmecpp.py ${input_file}
  done
done
