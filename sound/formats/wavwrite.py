"""包内引用-相对路径:
注意直接作为主模块运行会报错，要执行prove_sound7才可以
报错信息：
        from .wavread import wave_read
	ModuleNotFoundError: No module named '__main__.wavread'; '__main__' is not a package
官网解释：
      相对导入的路径依赖于当前模块的name这种方式去找平级或者上级文件的。因为作为主模块运行时，_name_ == __main__，所以这时是识别不出平级或上级文件，这时应当用绝对路径导入，不要用相对路径。
"""
from .wavread import wave_read
from .. import effects
print("from .wavread import wave_read")
wave_read()
print()
print("from .. import effects")
effects.echo.echo_effects()