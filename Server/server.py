from app.main import create_app,db
from flask_migrate import Migrate, migrate
from app.main.models import *

# main server file that runs the app

app = create_app()

migrate = Migrate(app,db)

if __name__ == "main":
    app.run()