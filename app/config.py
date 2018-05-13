import os
# 设置当前路径
path = os.path.abspath(os.path.dirname(__file__))
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY','123456')
    # 设置密钥
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 配置是否追踪
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # 配置是否默认提交
    BOOTSTRAP_SERVE_LOACAL = True
    # 是否加载本地bootstrap

#配置开发环境
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(path,'blog-dev.sqlite')

#测试环境,项目写完进行调试
class TestingConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(path, 'blog-test.sqlite')

#生成环境，调试完成进行使用
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(path, 'blog.sqlite')

# 将类装入字典，调用时名字更容易拼写
config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    #设置一个默认的环境
    'default':DevelopmentConfig
}

