import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '28cfdd92c3e78257eddec8e3c939b0de'
