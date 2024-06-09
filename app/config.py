import os

class config:
    SECRECT_KEY = os.eviron.get('SECRET_KEY') or 'you-will-never-guess'
