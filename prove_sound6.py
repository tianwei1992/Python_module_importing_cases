"""Good case:
from sound.effects import * after module echo has been explicitly imported
Then it doesn't matter whether those were defined in __all__(list) of __init__.py.
"""
import sound.effects.echo
import sound.effects.surround
from sound.effects import *
echo.echo_effects()
