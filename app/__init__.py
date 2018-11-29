from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads,IMAGES
from flask_bootstrap  import Bootstrap
from flask import Blueprint
from flask_simplemde import SimpleMDE

bootstrap=Bootstrap()
db = SQLAlchemy()
main = Blueprint('main',__name__)
simple = SimpleMDE()



def create_app(config_name):
    app=Flask(__name__ )
    
  # app extensions
    simple.init_app(app)
    db.init_app(app)
    bootstrap.init_app(app)
    
    app.config.from_object(config_options [config_name])
    config_options[config_name].init_app(app)
   
    #main blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
