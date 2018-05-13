from flask import Flask
from app.config import config
from app.extensions import config_extensions
from app.views import config_blueprint
def create_app(config_name):        #在此处创建app因为app内部使用app多，如蓝本，扩展，初始化配置等
    app = Flask(__name__)
    #初始化配置文件
    app.config.from_object(config[config_name])
    #各种扩展库的初始化
    config_extensions(app)
    #注册蓝本
    config_blueprint(app)
    return app