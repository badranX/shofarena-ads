import os
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    MONGO_URI = "mongodb+srv://python:python@cluster0-93bqo.mongodb.net/deldb?retryWrites=true"

class ProductionConfig(Config):
    MONGO_URI = os.environ.get('MONGO_URI')
    pass

config = {
    'development': DevelopmentConfig,
    'production' : ProductionConfig
}