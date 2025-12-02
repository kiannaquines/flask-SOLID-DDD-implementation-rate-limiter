#!/usr/bin/env python3
"""
Run database migrations for production
Usage: python3 migrate.py
"""
import os
from core import create_app
from core.config.extension import db
from flask_migrate import upgrade

# Create app with production config
app = create_app()

with app.app_context():
    # Run migrations
    upgrade()
    print("✅ Database migrations completed successfully")
