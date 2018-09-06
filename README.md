# 目的
通过简单示例，梳理python模块和包导入的相关规则

# 参考
https://docs.python.org/3.6/tutorial/modules.html#packages

# 结构说明

1. sound文件夹是将要被引入的包。其中sound是package，effects和formats是subpackage，echo.py等是module.
2. prove_sound*.py将会以不同的方式引用sound文件夹中的东西，验证是否能够正确引用.
3. 关于包内引用，分绝对引用和相对引用，坑比较多。
 示例文件是formats文件夹下的wavread.py和wavwrite.py.
