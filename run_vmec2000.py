"""
Run this under mpiexec!  
"""

from pathlib import Path
import argparse
import time

print("Begin importing simsopt.mhd (often slow because of MPI)...")
start_import = time.time()
import simsopt.mhd  # noqa: E402
end_import = time.time()
print(f"End importing simsopt.mhd. Took {end_import - start_import} s")


def run_vmec2000(indata_file: Path):
    vmec = simsopt.mhd.Vmec(str(indata_file))
    vmec.run()


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vmec_indata_file", type=Path)
    vmec_indata_file = p.parse_args().vmec_indata_file

    run_vmec2000(vmec_indata_file)
