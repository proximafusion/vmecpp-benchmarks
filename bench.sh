#!/bin/bash
# For example, run as:
#   bash bench.sh 2>&1 | tee logs.txt

N_CORES=1
for input_file in "data/input.precise_qa_beta1_mn12_ns99" "data/input.w7x_beta1_mn5_ns51"; do 
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time mpirun -n ${N_CORES} python run_vmec2000.py ${input_file} ${N_CORES}
  done

  export OMP_NUM_THREADS=${N_CORES}
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time python run_vmecpp.py ${input_file} ${N_CORES}
  done
done

N_CORES=4
for input_file in "data/input.precise_qa_beta1_mn12_ns99" "data/input.w7x_beta1_mn5_ns51"; do 
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time mpirun -n ${N_CORES} python run_vmec2000.py ${input_file} ${N_CORES}
  done

  export OMP_NUM_THREADS=${N_CORES}
  for i in 1 2 3; do
    taskset --cpu-list 0,2,4,6 /usr/bin/time python run_vmecpp.py ${input_file} ${N_CORES}
  done
done
