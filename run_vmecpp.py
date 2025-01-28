import vmecpp
from pathlib import Path
import argparse


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vmec_indata_file", type=Path)
    args = p.parse_args()

    input = vmecpp.VmecInput.from_file(args.vmec_indata_file)
    vmecpp.run(input)
