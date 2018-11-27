import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    ARCGIS_BASE_URL = os.environ.get('ARCGIS_BASE_URL')
    TEMPORARY_TOKEN = os.environ.get('TEMPORARY_TOKEN')



    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}