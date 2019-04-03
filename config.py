import os


class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    # Flask

    SECRET_KEY = 'SECRET_KEY'
    TEMPLATES_AUTO_RELOAD = True
    DEBUG = True
    APP_FOLDER = "app/"


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
