"""Good case:
from sound.effects import * after module echo has been explicitly imported
Then it doesn't matter whether those were defined in __all__(list) of __init__.py.
"""

from sound.formats import wavwrite

