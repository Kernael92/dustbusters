import os

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY')
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:1234@localhost/blogger'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringaschool:1234@localhost/blogger'
    
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}