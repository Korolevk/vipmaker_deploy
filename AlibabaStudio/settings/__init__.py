from .base import *

try:
    from .local import *
except ImportError:
    print("No local file in my project (look into file local.pu.skeleton)")