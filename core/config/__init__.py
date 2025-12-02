import os
from datetime import timedelta

# Only load .env file in local development (Vercel provides env vars directly)
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_COOKIE_SECURE = False
    JWT_HEADER_NAME = "Authorization"              
    JWT_HEADER_TYPE = "Bearer"    
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    APP_NAME = os.getenv('APP_NAME', 'Task Management System')
    
    # Swagger UI Configuration
    RESTX_MASK_SWAGGER = False
    SWAGGER_UI_DOC_EXPANSION = 'list'  # 'none', 'list', or 'full'
    SWAGGER_UI_OPERATION_ID = True
    SWAGGER_UI_REQUEST_DURATION = True
    ERROR_404_HELP = False
    RESTX_VALIDATE = True
    RESTX_JSON = {
        'indent': 2,
        'sort_keys': False,
    }

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB')
    DEBUG=os.getenv('DEBUG')

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DB')
    DEBUG=os.getenv('DEBUG')

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DB')
    DEBUG=os.getenv('DEBUG')