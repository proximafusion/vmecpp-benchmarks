import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("logs.txt", names=["VMEC_KIND", "INPUT", "CORES", "RUNTIME"]).sort_values(by="CORES")

# Compute mean and standard deviation for error bars
grouped_runtime = df.groupby(["VMEC_KIND", "CORES",  "INPUT"])["RUNTIME"]
mean_runtimes = grouped_runtime.mean().unstack(level=0)
std_runtimes = grouped_runtime.std().unstack(level=0)

# Compute the average speedup across all *multithreaded* test cases 
n_cores_for_comparison = df["CORES"].max()
speedup = (mean_runtimes["VMEC2000"]/mean_runtimes["VMECPP"])[n_cores_for_comparison].mean()
print(speedup)

x = np.arange(len(mean_runtimes))
width = 0.4

plt.bar(x-width/2, mean_runtimes["VMEC2000"], width, yerr=std_runtimes["VMEC2000"], capsize=5, label="VMEC2000", color="gray")
plt.bar(x+width/2, mean_runtimes["VMECPP"], width, yerr=std_runtimes["VMECPP"], capsize=5, label="VMECPP", color="#04ffc3")

plt.xticks(x)
plt.gca().set_xticklabels([f"{inp}\ncores={core}" for core, inp in mean_runtimes.index], rotation=25)
plt.ylabel("Runtime (s)")
plt.title(f"VMEC2000 vs VMECPP Runtime Comparison\nAverage speedup on {n_cores_for_comparison} cores: {speedup:.2f}x")
plt.legend()

plt.tight_layout()
plt.show()