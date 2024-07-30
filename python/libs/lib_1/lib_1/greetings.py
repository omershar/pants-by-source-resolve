import requests


def say_hello(name: str):
    print(f'Hello, {name}!')
    print(f'requests version: {requests.__version__}')
