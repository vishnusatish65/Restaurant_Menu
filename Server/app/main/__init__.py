from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import Config
# this is the app creation file
db = SQLAlchemy()

from app.main.route.menu import menu as menu_blueprint

def create_app():
    # function to create the app 
    app = Flask(__name__)
    CORS(app)
    config_data = Config()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%s@localhost/%s'%(config_data.DB_PASS,config_data.database_name)

    db.init_app(app)

    app.register_blueprint(menu_blueprint,url_prefix="/menu")
    
    return app

