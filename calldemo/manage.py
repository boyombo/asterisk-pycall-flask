from flask.ext.script import Manager
from app import App


manager = Manager(app)
app.config['DEBUG'] = True


if __name__ == '__main__':
    manager.run()
