"""
Run this under mpirun!
"""

from pathlib import Path
import argparse
import time
import mpi4py

print("Begin importing simsopt.mhd (often slow because of MPI)...")
start_import = time.time()
import simsopt.mhd  # noqa: E402
end_import = time.time()
print(f"End importing simsopt.mhd. Took {end_import - start_import} s")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("vmec_indata_file", type=Path)
    p.add_argument("n_cores", type=int)
    args = p.parse_args()

    vmec = simsopt.mhd.Vmec(str(args.vmec_indata_file))
    start = time.time()
    vmec.run()
    runtime = time.time() - start

    p.add_argument("n_cores", type=int)

    if mpi4py.MPI.COMM_WORLD.Get_rank() == 0:
        print(f"VMEC2000,{args.vmec_indata_file},{args.n_cores},{runtime}")
