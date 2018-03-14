import logging
import os


class Config(object):
    # noinspection PyPackageRequirements
    DEBUG = False

    LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s - %(message)s'
    LOG_LEVEL = logging.INFO

    # Flask-SQLAlchemy settings
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@host/db?charset=utf8'
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_POOL_SIZE = 5
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = True


class StagingConfig(Config):
    DEBUG = True

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    LOG_LEVEL = logging.WARNING


_configs = {
    'dev': DevelopmentConfig,
    'staging': StagingConfig,
    'prod': ProductionConfig
}


def get_config_class(env=None):
    if not env:
        env = os.environ.get('proj_env'.upper(), 'dev').lower()
    return _configs[env]


# CONF 是一个全局对象，用于获取配置项。
# 在 Flask Application Context 里，也可以通过 current_app.config 获取配置项
CONF = get_config_class()
