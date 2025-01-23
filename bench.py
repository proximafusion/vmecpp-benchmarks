import vmecpp

print("Begin importing simsopt.mhd (often slow because of MPI)...")
import simsopt.mhd
print("End importing simsopt.mhd (often slow because of MPI)...")

from pathlib import Path
import time


def run_vmecpp(indata_file: Path):
    input = vmecpp.VmecInput.from_file(indata_file)
    vmecpp.run(input)


def run_vmec2000(indata_file: Path):
    vmec = simsopt.mhd.Vmec(str(indata_file))
    vmec.run()


def main():
    # precise_qa
    precise_qa_input = Path("data/input.precise_qa_beta1_mn5_ns51")

    print("Begin VMEC++ run on precise_qa...")
    start_time = time.time()
    run_vmecpp(precise_qa_input)
    end_time = time.time()
    print("End VMEC++ run on precise_qa...")
    vmecpp_precise_qa_time = end_time - start_time
    print("Runtime: ", vmecpp_precise_qa_time)

    print("Begin VMEC2000 run on precise_qa...")
    start_time = time.time()
    run_vmec2000(precise_qa_input)
    end_time = time.time()
    print("End VMEC2000 run on precise_qa...")
    vmec2000_precise_qa_time = end_time - start_time
    print("Runtime: ", vmec2000_precise_qa_time)

    # w7x
    w7x_input = Path("data/input.w7x_beta1_mn5_ns51")

    print("Begin VMEC++ run on w7x...")
    start_time = time.time()
    run_vmecpp(w7x_input)
    end_time = time.time()
    print("End VMEC++ run on w7x...")
    vmecpp_w7x_time = end_time - start_time
    print("Runtime: ", vmecpp_w7x_time)

    print("Begin VMEC2000 run on w7x...")
    start_time = time.time()
    run_vmec2000(w7x_input)
    end_time = time.time()
    print("End VMEC2000 run on w7x...")
    vmec2000_w7x_time = end_time - start_time
    print("Runtime: ", vmec2000_w7x_time)

    print("\nTIMES")
    print("\t\tVMEC2000\t\tVMEC++")
    print(f"precise_qa\t{vmec2000_precise_qa_time}\t{vmecpp_precise_qa_time}")
    print(f"w7x\t\t{vmec2000_w7x_time}\t{vmecpp_w7x_time}")


if __name__ == "__main__":
    main()
