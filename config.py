import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'i-will-never-tell'