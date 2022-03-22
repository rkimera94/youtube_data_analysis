import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app, db


# app.config.from_object(os.environ['APP_SETTINGS'])

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://postgres:123Ht@localhost/aviyel_1"


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
