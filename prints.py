from __future__ import print_function
import platform
Platform = platform.system()
import builtins
def prints(color,*args, **kwargs):
    builtins.print('\033[01m',end='')
    builtins.print(color,end='')
    builtins.print(*args,**kwargs)
    builtins.print('\033[0m',end='')

if __name__=='__main__':
    print(Platform)