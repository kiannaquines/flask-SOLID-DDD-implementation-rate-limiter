from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter

migrate = Migrate()
db = SQLAlchemy()

limiter = Limiter(
    key_func=lambda: "global",
    default_limits=["5000 per day", "1000 per hour","100 per minute"],
    storage_uri="memory://",
)