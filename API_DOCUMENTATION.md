# Task Management API - Documentation

## Overview
A comprehensive Task Management REST API built with Flask, implementing SOLID principles and Domain-Driven Design (DDD) patterns.

## OpenAPI/Swagger UI Improvements

### What's Been Enhanced

#### 1. **Improved API Documentation**
- Added detailed descriptions for all endpoints
- Included examples for request/response models
- Added validation rules and constraints
- Comprehensive error response documentation

#### 2. **Enhanced UI Configuration**
- **Doc Expansion**: Set to 'list' - shows all endpoints in an organized list view
- **Operation IDs**: Enabled for better endpoint identification
- **Request Duration**: Shows timing for API calls
- **Ordered Endpoints**: Endpoints are displayed in a logical order
- **Validation**: Automatic request validation enabled

#### 3. **Better Models & Examples**
- Separate models for create, update, and response operations
- Realistic examples for all fields
- Proper field validation (min/max lengths, required fields)
- Clear error response models

#### 4. **Security Documentation**
- JWT Bearer token authentication clearly documented
- 'Authorize' button in Swagger UI for easy token management
- Security requirements shown for each protected endpoint

#### 5. **Response Status Codes**
All endpoints now document:
- 200/201: Success responses with models
- 400: Bad Request with error details
- 401: Unauthorized access
- 404: Resource not found
- 500: Internal server errors

## Accessing the API Documentation

### Swagger UI
Visit: `http://localhost:5000/api/v1/docs`

The Swagger UI provides:
- Interactive API testing
- Request/response examples
- Model schemas
- Authentication testing with the 'Authorize' button

### API Endpoints

#### Authentication (`/api/v1/auth`)
- **POST /register** - Register a new user
- **POST /login** - Login and receive JWT token
- **POST /logout** - Logout and clear session

#### Tasks (`/api/v1/tasks`)
- **GET /** - List all tasks
- **GET /{task_id}** - Get specific task
- **POST /create** - Create new task
- **PUT /{task_id}/update** - Update existing task
- **DELETE /{task_id}/delete** - Delete task

#### Dashboard (`/api/v1/dashboard`)
- **GET /** - Get dashboard information

## Using the API

### 1. Register a User
```bash
curl -X POST http://localhost:5000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass123!",
    "email": "john.doe@example.com"
  }'
```

### 2. Login
```bash
curl -X POST http://localhost:5000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "password": "SecurePass123!"
  }'
```

Response:
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

### 3. Use Token for Protected Endpoints
```bash
curl -X GET http://localhost:5000/api/v1/tasks/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### 4. Using Swagger UI
1. Navigate to `http://localhost:5000/api/v1/docs`
2. Click the **'Authorize'** button (green lock icon)
3. Enter: `Bearer YOUR_TOKEN_HERE`
4. Click **'Authorize'**
5. Now you can test all protected endpoints directly in the UI!

## Configuration Options

The following Swagger UI options are configured in `core/config/__init__.py`:

```python
# Swagger UI Configuration
RESTX_MASK_SWAGGER = False              # Disable field masking
SWAGGER_UI_DOC_EXPANSION = 'list'       # Show endpoints in list view
SWAGGER_UI_OPERATION_ID = True          # Display operation IDs
SWAGGER_UI_REQUEST_DURATION = True      # Show request timing
ERROR_404_HELP = False                  # Disable 404 suggestions
RESTX_VALIDATE = True                   # Enable request validation
```

## Model Validation

All models now include validation:
- **Username**: 3-50 characters, required
- **Password**: Minimum 6 characters, required
- **Email**: Valid email format, required
- **Task Title**: 1-200 characters, required
- **Task Description**: Optional text field

## Error Handling

All endpoints return consistent error responses:

```json
{
  "message": "Descriptive error message",
  "success": false
}
```

Common HTTP status codes:
- `200` - Success
- `201` - Created
- `204` - No Content (successful deletion)
- `400` - Bad Request (validation error)
- `401` - Unauthorized (invalid/missing token)
- `404` - Not Found
- `500` - Internal Server Error

## API Features

✅ JWT Authentication
✅ Rate Limiting
✅ Request Validation
✅ Comprehensive Error Handling
✅ Clean Architecture (SOLID + DDD)
✅ Interactive API Documentation
✅ Response Marshalling
✅ Database Migrations
✅ Production Ready

## Support

For issues or questions:
- Email: kjgnaquines@gmail.com
- GitHub: https://github.com/kiannaquines/flask-SOLID-DDD-implementation-rate-limiter

## License

MIT License
