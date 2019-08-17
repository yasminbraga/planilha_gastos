import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'jshdaga\sjkhfuhweugrweuklasd83764208iqohd73i2jduu89472902ojdaaçei2'


class Development(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_PASSWORD = 'yasmin04'
    SQLALCHEMY_DATABASE_URI = 'postgresql:///planilha_gastos_dev'
    ENV = 'development'
    

class Production(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    ENV = 'production'


