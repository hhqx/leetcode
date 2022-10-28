"""
this is a docstring

"""


"""
    # Reloading modules in Python2.x
    reload(module)
    # For above 2. x and <=Python3.3
    import imp
    imp.reload(module)
    
    # Reloading modules for >=Python3.4 and above
    import importlib
    importlib.reload(module)
"""

import decorators
import decorators

import importlib
# decorators = importlib.import_module("decorators")
importlib.reload(decorators)

print(__doc__)