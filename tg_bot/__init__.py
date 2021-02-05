import os

ENV = bool(os.environ.get('ENV', False))
if ENV:
    TOKEN = os.environ.get('TOKEN', None)
