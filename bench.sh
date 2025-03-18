#!/bin/bash
# SPDX-FileCopyrightText: 2025-present Proxima Fusion GmbH <info@proximafusion.com>
#
# SPDX-License-Identifier: MIT

# For example, run as:
#   bash bench.sh 2>&1 | tee logs.txt

# Run a few times to gather statistics
for i in 1 2 3 4 5; do
  for n_cores in 1 4; do
    for input_file in "data/input.precise_qa_beta1_mn12_ns99"  "data/input.w7x_beta1_mn5_ns51"; do
      time mpirun --map-by core --allow-run-as-root -n ${n_cores} python run_vmec2000.py ${input_file} ${n_cores}

      export OMP_NUM_THREADS=${n_cores}
      taskset --cpu-list 0,2,4,6 time python run_vmecpp.py ${input_file} ${n_cores}
    done
  done
done
