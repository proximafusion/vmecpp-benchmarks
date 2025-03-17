# SPDX-FileCopyrightText: 2025-present Proxima Fusion GmbH <info@proximafusion.com>
#
# SPDX-License-Identifier: MIT
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import argparse
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument("runtimes_file", type=Path)
runtimes_file = p.parse_args().runtimes_file

df = pd.read_csv(runtimes_file, names=["VMEC_KIND", "INPUT", "CORES", "RUNTIME"]).sort_values(by="CORES")
df["INPUT"] = df["INPUT"].apply(lambda txt: txt.removeprefix("data/input."))

# Compute mean and standard deviation for error bars
grouped_runtime = df.groupby(["VMEC_KIND", "CORES",  "INPUT"])["RUNTIME"]
mean_runtimes = grouped_runtime.mean().unstack(level=0)
std_runtimes = grouped_runtime.std().unstack(level=0)

x = np.arange(len(mean_runtimes))
width = 0.4

plt.bar(x-width/2, mean_runtimes["VMEC2000"], width, yerr=std_runtimes["VMEC2000"], capsize=5, label="VMEC2000", color="gray")
plt.bar(x+width/2, mean_runtimes["VMECPP"], width, yerr=std_runtimes["VMECPP"], capsize=5, label="VMECPP", color="#04ffc3")

plt.xticks(x)
plt.gca().set_xticklabels([f"{inp}\ncores={core}" for core, inp in mean_runtimes.index], rotation=25)
plt.ylabel("Runtime (s)")
plt.title(f"VMEC2000 vs VMECPP Runtime Comparison")
plt.legend()

# Compute the average speedup for each corecount across all test cases
unique_cores = df["CORES"].unique()
for i, n_cores_for_comparison in enumerate(unique_cores):
  speedup = (mean_runtimes["VMEC2000"]/mean_runtimes["VMECPP"])[n_cores_for_comparison].mean()
  # Place the text in the middle of the single threaded and multi threaded groups of bars
  plt.text(i*len(unique_cores)+len(x)/len(unique_cores)/4,
    mean_runtimes.to_numpy().mean(),
    f"{n_cores_for_comparison}-core speedup: {speedup:.2f}x",
    horizontalalignment="center",
    bbox=dict(facecolor='white', alpha=0.5))

plt.tight_layout()
plt.savefig("benchmark.png")
plt.show()
