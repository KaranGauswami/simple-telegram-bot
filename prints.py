from __future__ import print_function
import platform
Platform = platform.system()
if Platform != 'Windows':
    import builtins as __builtin__
    def prints(color,*args, **kwargs):
        builtins.print('\033[01m',end='')
        builtins.print(color,end='')
        builtins.print(*args,**kwargs)
        builtins.print('\033[0m',end='')
else:
    def prints(color,*args,**kwargs):
        builtins.print(*args,**kwargs)

