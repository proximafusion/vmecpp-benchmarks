# VMEC++ benchmarks

On Ubuntu 22.04, this should work out of the box:

```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python bench.py
```

On other systems, you need a Python environment with [VMEC2000](https://github.com/hiddenSymmetries/VMEC2000), [SIMSOPT](https://github.com/hiddenSymmetries/simsopt) and [VMEC++](https://github.com/proximafusion/vmecpp).
