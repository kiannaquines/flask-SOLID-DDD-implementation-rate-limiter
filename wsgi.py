from core import create_app

# gunicorn -w 4 wsgi:app
app = create_app()