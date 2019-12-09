# This exist to make unittest aware of the application path
# When unitest needs any sample module , this __init__.py file gets call first and here
# we take the opportunity to add the sample module to the path as seem by unittest
# This will guarantee complex imports because in this module we have core.py that import helpers.py using absolute
# imports and if unittest  get there without having sample in the sys.path it will fail importing helpers
# This way we gurantee complex imports
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))
from .core import hmm
