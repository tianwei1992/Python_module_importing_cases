"""from sound.effects import *
Not really import everything ,only those defined in __all__(list) of __init__.py.
"""
from sound.effects import *
echo.echo_effects()
"""
Result:
NameError: name 'echo' is not defined
"""
"""after adding ___all__ = ["echo"] to __init__.py, importing succeed!
"""