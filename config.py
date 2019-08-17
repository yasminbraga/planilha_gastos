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
    SQLALCHEMY_DATABASE_URI = 'postgres://kxcbaqawtgphbo:159637d0dce0975c4bdf922ee2e38c7d4749b91641c334d27c86a6b48fa707ea@ec2-107-20-230-70.compute-1.amazonaws.com:5432/d7oe0tn3n1tmnp'
    ENV = 'production'


