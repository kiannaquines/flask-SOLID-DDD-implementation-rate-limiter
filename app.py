from core import create_app
from core.config import ProductionConfig

# Create app instance for Vercel
app = create_app(config=ProductionConfig)

# For local development
if __name__ == "__main__":
    from core.config import DevelopmentConfig
    app = create_app(config=DevelopmentConfig)
    app.run(debug=True)