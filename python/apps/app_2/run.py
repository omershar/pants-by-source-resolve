import sys

import numpy

from lib_1 import say_hello as say_hello1
from lib_2 import say_hello as say_hello2

if __name__ == '__main__':
    say_hello1('app_2 lib1')
    say_hello2('app_2 lib2')
    print(f'python {sys.version}')
    print(f'numpy version: {numpy.__version__}')
