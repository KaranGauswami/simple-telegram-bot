from __future__ import print_function
import platform
Platform = platform.system()
if Platform != 'Windows':
    try:
        #python
        import __builtin__
    except ImportError:
        # Python 3
        import builtins as __builtin__
    def prints(color,*args, **kwargs):
        __builtin__.print('\033[01m',end='')
        __builtin__.print(color,end='')
        __builtin__.print(*args,**kwargs)
        __builtin__.print('\033[0m',end='')
else:
    def prints(color,*args,**kwargs):
        __builtin__.print(*args,**kwargs)

