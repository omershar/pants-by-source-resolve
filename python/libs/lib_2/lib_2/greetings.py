import requests

from lib_3 import say_hello as say_hello_lib_3


def say_hello(name: str):
    say_hello_lib_3(name)
    print(f'requests version: {requests.__version__}')
