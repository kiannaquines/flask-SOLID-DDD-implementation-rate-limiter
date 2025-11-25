import os
from dotenv import load_dotenv

load_dotenv()

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    APP_NAME = os.getenv('APP_NAME', 'Task Management System')

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB')
    DEBUG=os.getenv('DEBUG')

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DB')
    DEBUG=os.getenv('DEBUG')

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DB')
    DEBUG=os.getenv('DEBUG')