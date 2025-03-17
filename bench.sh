#!/bin/bash
# SPDX-FileCopyrightText: 2025-present Proxima Fusion GmbH <info@proximafusion.com>
#
# SPDX-License-Identifier: MIT

# For example, run as:
#   bash bench.sh 2>&1 | tee logs.txt

for n_cores in 1 4; do
  for input_file in "data/input.precise_qa_beta1_mn12_ns99" "data/input.w7x_beta1_mn5_ns51"; do 
    # Run a few times to gather statistics
    for i in 1 2 3; do
      taskset --cpu-list 0,2,4,6 /usr/bin/time mpirun -n ${n_cores} python run_vmec2000.py ${input_file} ${n_cores}
    done

    export OMP_NUM_THREADS=${n_cores}
    for i in 1 2 3; do
      taskset --cpu-list 0,2,4,6 /usr/bin/time python run_vmecpp.py ${input_file} ${n_cores}
    done
  done
done
