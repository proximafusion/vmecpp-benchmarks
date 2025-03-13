import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = [
    ("VMEC2000", "precise_qa_beta1_mn12_ns99", 1, 34.59669518470764),
    ("VMEC2000", "precise_qa_beta1_mn12_ns99", 1, 38.421379804611206),
    ("VMEC2000", "precise_qa_beta1_mn12_ns99", 1, 38.470274209976196),
    ("VMECPP", "precise_qa_beta1_mn12_ns99", 1, 26.268169164657593),
    ("VMECPP", "precise_qa_beta1_mn12_ns99", 1, 26.23130440711975),
    ("VMECPP", "precise_qa_beta1_mn12_ns99", 1, 26.23588800430298),
    ("VMEC2000", "w7x_beta1_mn5_ns51", 1, 21.627432584762573),
    ("VMEC2000", "w7x_beta1_mn5_ns51", 1, 21.74281334877014),
    ("VMEC2000", "w7x_beta1_mn5_ns51", 1, 21.649543046951294),
    ("VMECPP", "w7x_beta1_mn5_ns51", 1, 19.783687114715576),
    ("VMECPP", "w7x_beta1_mn5_ns51", 1, 20.08419919013977),
    ("VMECPP", "w7x_beta1_mn5_ns51", 1, 19.772046327590942),
    ("VMEC2000", "precise_qa_beta1_mn12_ns99", 4, 24.047865629196167),
    ("VMEC2000", "precise_qa_beta1_mn12_ns99", 4, 23.971978187561035),
    ("VMEC2000", "precise_qa_beta1_mn12_ns99", 4, 24.16266131401062),
    ("VMECPP", "precise_qa_beta1_mn12_ns99", 4, 16.425143718719482),
    ("VMECPP", "precise_qa_beta1_mn12_ns99", 4, 16.58508586883545),
    ("VMECPP", "precise_qa_beta1_mn12_ns99", 4, 16.614110231399536),
    ("VMEC2000", "w7x_beta1_mn5_ns51", 4, 29.975491285324097),
    ("VMEC2000", "w7x_beta1_mn5_ns51", 4, 24.51761484146118),
    ("VMEC2000", "w7x_beta1_mn5_ns51", 4, 26.609149932861328),
    ("VMECPP", "w7x_beta1_mn5_ns51", 4, 12.045800924301147),
    ("VMECPP", "w7x_beta1_mn5_ns51", 4, 11.920774459838867),
    ("VMECPP", "w7x_beta1_mn5_ns51", 4, 12.256176471710205),
]

# Convert to DataFrame
df = pd.DataFrame(data, columns=["VMEC_KIND", "INPUT", "CORES", "RUNTIME"]).sort_values(by="CORES")

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