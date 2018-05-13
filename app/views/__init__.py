from .main import main
from .movie import movie
#蓝本的配置，将蓝本中的对象名与路由以元组的形式写入元组，进行for循环遍历
DEFAULT_BULEPRINT = (
    (main,'/main'),
    (movie,'/movie'),
)
def config_blueprint(app):
    for blueprint,url_prefix in DEFAULT_BULEPRINT:
        app.register_blueprint(blueprint,url_prefix=url_prefix)


