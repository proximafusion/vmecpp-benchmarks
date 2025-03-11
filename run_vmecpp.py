import vmecpp
from pathlib import Path
import argparse
import time


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vmec_indata_file", type=Path)
    args = p.parse_args()

    input = vmecpp.VmecInput.from_file(args.vmec_indata_file)
    start = time.time()
    vmecpp.run(input)
    runtime = time.time() - start

    print(f"VMECPP ON {args.vmec_indata_file} -- runtime(s): {runtime}")
