import importlib

# Check if CuPy is available
if importlib.util.find_spec("cupy"):
    print("cupy")
    import cupy as xp
else:
    print("numpy")
    import numpy as xp