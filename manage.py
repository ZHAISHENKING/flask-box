"""
# author:  师仁杰
# 说明:    系统入口文件，
# 功能:    实例化app,添加shell脚本
"""
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from admin import db
from production import *

try:
    from local_settings import *
except ImportError:
    pass

app = create_app(ENV)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)

@manager.command
def runserver():
    def run():
        app.run(port=12341, debug=app.config["DEBUG"])
    run()


if __name__ == '__main__':
    manager.run()
