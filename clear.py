from __future__ import print_function
import platform
import os
Platform = platform.system()
if Platform != 'Windows':
    def clear():
    	os.system('clear')
else:
    def clear():
            os.system('cls')

