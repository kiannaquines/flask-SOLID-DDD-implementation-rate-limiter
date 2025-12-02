from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_jwt_extended import JWTManager

migrate = Migrate()

db = SQLAlchemy(
    engine_options={
        'pool_size': 5,              # Number of connections to maintain
        'pool_pre_ping': True,       # Verify connections before using
        'pool_recycle': 3600,        # Recycle connections after 1 hour
        'max_overflow': 2,           # Max connections beyond pool_size
        'pool_timeout': 30,          # Timeout for getting connection
        'connect_args': {
            'connect_timeout': 10    # Database connection timeout
        }
    }
)

jwt = JWTManager()

limiter = Limiter(
    key_func=lambda: "global",
    default_limits=["5000 per day", "1000 per hour", "100 per minute"],
    storage_uri="memory://",
)