import sys

import numpy
import requests

from lib_1 import say_hello

if __name__ == '__main__':
    say_hello('app_1')
    print(f'python {sys.version}')
    print(f'numpy version: {numpy.__version__}')
    print(f'requests version: {requests.__version__}')
