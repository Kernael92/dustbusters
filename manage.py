import os
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app import create_app

app = create_app('development')
manager=Manager(app)
manager.add_command('server',Server)

@manager.shell
def shell_context():
    return dict(app=app)


if __name__=='__main__':
    manager.run()
