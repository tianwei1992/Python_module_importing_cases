"""包内引用-绝对路径:
"""
from sound.effects.echo import echo_effects

def wave_read():
	print("from sound.effects.echo import echo_effects")
	echo_effects()

if __name__ == "__main__":
	wave_read()