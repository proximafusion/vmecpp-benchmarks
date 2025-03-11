"""
Run this under mpirun!
"""

from pathlib import Path
import argparse
import time

print("Begin importing simsopt.mhd (often slow because of MPI)...")
start_import = time.time()
import simsopt.mhd  # noqa: E402
end_import = time.time()
print(f"End importing simsopt.mhd. Took {end_import - start_import} s")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vmec_indata_file", type=Path)
    vmec_indata_file = p.parse_args().vmec_indata_file

    vmec = simsopt.mhd.Vmec(str(vmec_indata_file))
    start = time.time()
    vmec.run()
    runtime = time.time() - start

    print(f"VMEC2000 ON {vmec_indata_file} -- runtime(s): {runtime}")
