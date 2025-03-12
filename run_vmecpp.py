import vmecpp
from pathlib import Path
import argparse
import time


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vmec_indata_file", type=Path)
    p.add_argument("n_cores", type=int)
    args = p.parse_args()

    input = vmecpp.VmecInput.from_file(args.vmec_indata_file)
    start = time.time()
    vmecpp.run(input)
    runtime = time.time() - start

    print(f"VMECPP,{args.vmec_indata_file},{args.n_cores},{runtime}")
