import importlib
from .metrics import *

# Check if CuPy is available
if importlib.util.find_spec("cupy"):
    import cupy as xp
else:
    import numpy as xp

# Expose xp as the array module (CuPy or NumPy)
__all__ = ["xp"]

__version__ = "0.1"