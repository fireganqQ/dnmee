import os

ENV = bool(os.environ.get('ENV', False))
if ENV:
    token = os.environ.get('TOKEN', None)