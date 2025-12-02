# Task Management API

A comprehensive Task Management REST API built with Flask, implementing SOLID principles and Domain-Driven Design (DDD) patterns.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/kiannaquines/flask-SOLID-DDD-implementation-rate-limiter)

## 🚀 Features

- **Authentication**: Secure JWT-based authentication
- **Task Management**: Full CRUD operations for tasks
- **Rate Limiting**: Built-in API rate limiting for security
- **Clean Architecture**: Implements SOLID principles and DDD patterns
- **OpenAPI/Swagger**: Interactive API documentation
- **Serverless Ready**: Optimized for Vercel deployment

## 📋 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/kiannaquines/flask-SOLID-DDD-implementation-rate-limiter.git
cd task_management

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start the development server
python app.py
```

Visit `http://localhost:5000/api/v1/docs` for the interactive API documentation.

### Deploy to Vercel

```bash
# Install Vercel CLI
npm i -g vercel

# Deploy
vercel
```

Or click the "Deploy with Vercel" button above.

## 📚 Documentation

- **[API Documentation](API_DOCUMENTATION.md)** - Complete API guide and usage examples
- **[Vercel Deployment Guide](VERCEL_DEPLOYMENT.md)** - Detailed deployment instructions
- **[OpenAPI Improvements](OPENAPI_IMPROVEMENTS.md)** - Swagger UI enhancements
- **[JWT Token Format Guide](JWT_TOKEN_FORMAT_GUIDE.md)** - Authentication help
- **[Quick Start Guide](QUICK_START_GUIDE.md)** - Step-by-step usage guide

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following:

```bash
# Database
DEV_DB=mysql+pymysql://user:password@localhost/task_db_dev
PROD_DB=mysql+pymysql://user:password@host/task_db_prod

# JWT
JWT_SECRET_KEY=your-secret-key-here

# Application
DEBUG=True
APP_NAME=Task Management System
```

### For Vercel Deployment

Set these environment variables in your Vercel project settings:
- `PROD_DB` - Production database connection string
- `JWT_SECRET_KEY` - Secret key for JWT tokens
- `DEBUG` - Set to `False` for production
- `APP_NAME` - Your application name

## 📖 API Endpoints

### Authentication
- `POST /api/v1/auth/register` - Register a new user
- `POST /api/v1/auth/login` - Login and get JWT token
- `POST /api/v1/auth/logout` - Logout user

### Tasks
- `GET /api/v1/tasks/` - List all tasks
- `GET /api/v1/tasks/{id}` - Get task by ID
- `POST /api/v1/tasks/create` - Create new task
- `PUT /api/v1/tasks/{id}/update` - Update task
- `DELETE /api/v1/tasks/{id}/delete` - Delete task

### Dashboard
- `GET /api/v1/dashboard/` - Get dashboard information

### System
- `GET /` - API information
- `GET /health` - Health check endpoint
- `GET /api/v1/docs` - Interactive API documentation (Swagger UI)

## 🔐 Authentication

This API uses JWT (JSON Web Tokens) for authentication.

1. Register a user via `/api/v1/auth/register`
2. Login via `/api/v1/auth/login` to get your token
3. Include the token in the Authorization header:
   ```
   Authorization: Bearer <your_token>
   ```

See [JWT_TOKEN_FORMAT_GUIDE.md](JWT_TOKEN_FORMAT_GUIDE.md) for detailed instructions.

## 🏗️ Architecture

```
task_management/
├── app.py                  # Application entry point
├── wsgi.py                 # WSGI entry point for production
├── migrate.py              # Database migration script
├── core/
│   ├── __init__.py        # App factory
│   ├── application/       # Application services
│   │   ├── task/
│   │   └── user/
│   ├── domain/            # Domain models
│   │   ├── task.py
│   │   └── user.py
│   ├── infrastructure/    # Data access layer
│   │   ├── task/
│   │   └── user/
│   ├── routes/            # API routes
│   │   ├── auth.py
│   │   ├── task.py
│   │   └── dashboard.py
│   ├── config/            # Configuration
│   │   ├── __init__.py
│   │   └── extension.py
│   └── exceptions/        # Custom exceptions
└── migrations/            # Database migrations
```

## 🧪 Testing

```bash
# Install dev dependencies
pip install -r requirements.dev.txt

# Run tests
pytest

# Run with coverage
pytest --cov=core
```

## 🛠️ Technology Stack

- **Flask** - Web framework
- **Flask-RESTX** - REST API with OpenAPI/Swagger
- **Flask-JWT-Extended** - JWT authentication
- **Flask-SQLAlchemy** - ORM
- **Flask-Migrate** - Database migrations
- **Flask-Limiter** - Rate limiting
- **PyMySQL** - MySQL driver
- **Gunicorn** - Production WSGI server

## 📊 Database

This application uses MySQL/MariaDB. For serverless deployments, consider:

- **Neon** (PostgreSQL)
- **PlanetScale** (MySQL)
- **Supabase** (PostgreSQL)
- **Railway** (MySQL/PostgreSQL)

### Migrations

```bash
# Create a new migration
flask db migrate -m "Description"

# Apply migrations
flask db upgrade

# Or use the migrate script
python migrate.py
```

## 🔒 Security Features

- JWT-based authentication
- Password hashing
- Rate limiting (100 requests/minute)
- CORS support
- Input validation
- SQL injection protection (via SQLAlchemy)

## 🚀 Performance

- Connection pooling for database
- Optimized for serverless (Vercel Functions)
- Static file serving via CDN (Vercel)
- Automatic scaling
- Cold start optimization

## 📈 Monitoring

### Health Check

```bash
curl https://your-app.vercel.app/health
```

Response:
```json
{
  "status": "healthy",
  "service": "task-management-api",
  "version": "1.0.0"
}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -am 'Add feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details

## 👤 Author

**Kianna Quines**
- Email: kjgnaquines@gmail.com
- GitHub: [@kiannaquines](https://github.com/kiannaquines)

## 🙏 Acknowledgments

- Flask documentation and community
- Vercel for serverless deployment platform
- Contributors and users of this project

## 📞 Support

For issues or questions:
- Create an issue on GitHub
- Email: kjgnaquines@gmail.com
- Check the [documentation files](VERCEL_DEPLOYMENT.md)

---

**Ready to deploy?** See [VERCEL_DEPLOYMENT.md](VERCEL_DEPLOYMENT.md) for detailed instructions.
