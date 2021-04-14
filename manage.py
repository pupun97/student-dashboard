from flask_app import app
from flask_script import Manager, Server
from flask_migrate import MigrateCommand
import flask_app.model

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server(port=8000, threaded=True, use_debugger=True))


if __name__ == '__main__':
    manager.run()