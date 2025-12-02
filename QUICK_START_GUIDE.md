# Quick Start Guide - OpenAPI UI

## 🚀 Accessing Your Improved API Documentation

### URL
```
http://localhost:5000/api/v1/docs
```

## 📋 What You'll See

### Main Features

#### 1. Header Section
- **Title**: "Task Management API" (v1.0.0)
- **Description**: Multi-line formatted description with features
- **Authorize Button**: Green lock icon - click to set your JWT token
- **Explore**: Download OpenAPI spec

#### 2. Organized Namespaces
Your endpoints are grouped logically:

```
📁 Auth - Authentication and authorization operations
  POST /api/v1/auth/register    Register a new user
  POST /api/v1/auth/login       Login and get JWT token
  POST /api/v1/auth/logout      Logout user

📁 Dashboard - Dashboard and system information
  GET /api/v1/dashboard/        Get dashboard information

📁 Tasks - Task management operations
  GET    /api/v1/tasks/                    List all tasks
  GET    /api/v1/tasks/{task_id}           Get task by ID
  POST   /api/v1/tasks/create              Create a new task
  PUT    /api/v1/tasks/{task_id}/update    Update a task
  DELETE /api/v1/tasks/{task_id}/delete    Delete a task
```

#### 3. Interactive Testing

For each endpoint, you'll see:
- **HTTP Method** (color-coded: GET=blue, POST=green, PUT=orange, DELETE=red)
- **Path** with parameters highlighted
- **Description** of what the endpoint does
- **Lock icon** if authentication required

Click to expand and you'll see:
- Parameters (path, query, body)
- Request body schema with examples
- Response codes and schemas
- "Try it out" button

## 🔐 Authentication Workflow

### Step-by-Step Guide

#### 1️⃣ Register a User
```
1. Scroll to: Auth > POST /api/v1/auth/register
2. Click to expand
3. Click "Try it out"
4. You'll see pre-filled example:
   {
     "username": "john_doe",
     "password": "SecurePass123!",
     "email": "john.doe@example.com"
   }
5. Modify if needed
6. Click "Execute"
7. Check response (should be 201 Created)
```

#### 2️⃣ Login
```
1. Go to: Auth > POST /api/v1/auth/login
2. Click "Try it out"
3. Enter your credentials:
   {
     "username": "john_doe",
     "password": "SecurePass123!"
   }
4. Click "Execute"
5. Copy the access_token from the response
```

#### 3️⃣ Authorize
```
1. Click the "Authorize" button (top of page, green lock)
2. A modal appears
3. In the "Value" field, type: Bearer YOUR_TOKEN_HERE
   Example: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
4. Click "Authorize"
5. Click "Close"
6. Lock icons next to endpoints turn locked 🔒
```

#### 4️⃣ Test Protected Endpoints
```
1. Now try: Tasks > GET /api/v1/tasks/
2. Click "Try it out"
3. Click "Execute"
4. You'll get your tasks (authentication automatic!)
```

## 📝 Model Schemas

When you expand an endpoint, you'll see:

### Request Body Example
```json
{
  "title": "Complete project documentation",
  "description": "Write comprehensive API documentation with examples"
}
```

### Model Schema
```
Task {
  title*        string($string)
                minLength: 1
                maxLength: 200
                Example: "Complete project documentation"
                The task title
  
  description   string($string)
                Example: "Write comprehensive API docs"
                The task description
}

* = required
```

### Response Example
```json
{
  "id": 1,
  "title": "Complete project documentation",
  "description": "Write comprehensive API documentation with examples",
  "is_completed": false
}
```

## 🎯 Testing Features

### Create a Task
```
POST /api/v1/tasks/create

Request:
{
  "title": "My First Task",
  "description": "Learning to use the API"
}

Response (201):
{
  "id": 1,
  "title": "My First Task",
  "description": "Learning to use the API",
  "is_completed": false
}
```

### List Tasks
```
GET /api/v1/tasks/

Response (200):
{
  "tasks": [
    {
      "id": 1,
      "title": "My First Task",
      "description": "Learning to use the API",
      "is_completed": false
    }
  ]
}
```

### Update Task
```
PUT /api/v1/tasks/1/update

Request:
{
  "is_completed": true
}

Response (200):
{
  "id": 1,
  "title": "My First Task",
  "description": "Learning to use the API",
  "is_completed": true
}
```

### Delete Task
```
DELETE /api/v1/tasks/1/delete

Response: 204 No Content
```

## 🎨 UI Features You'll Notice

### Color Coding
- 🟢 **POST** - Green (creates resources)
- 🔵 **GET** - Blue (reads resources)
- 🟠 **PUT** - Orange (updates resources)
- 🔴 **DELETE** - Red (deletes resources)

### Icons
- 🔓 - Unlocked (no auth required)
- 🔒 - Locked (requires JWT token)
- ⚙️ - Parameters available
- 📄 - Request body expected

### Sections
- **Parameters** - Path/query parameters
- **Request body** - JSON payload with schema
- **Responses** - All possible response codes
- **Response Schema** - Structure of response data

## ⚠️ Common Issues

### "401 Unauthorized"
- Your token expired (tokens last 1 hour)
- Token format wrong (must be: `Bearer <token>`)
- Solution: Login again, get new token, re-authorize

### "400 Bad Request"
- Missing required field (check red asterisk *)
- Validation failed (check min/max length)
- Solution: Follow the model schema exactly

### "404 Not Found"
- Wrong resource ID
- Resource was deleted
- Solution: Check the ID exists (use GET /tasks first)

## 💡 Pro Tips

1. **Use the Models Tab**
   - Scroll to bottom of Swagger UI
   - Click "Models" to see all data structures
   - Great for understanding the API

2. **Download OpenAPI Spec**
   - Click the link at top of page
   - Import into Postman or other tools
   - Use for code generation

3. **Keyboard Shortcuts**
   - `Ctrl/Cmd + F` - Search endpoints
   - Click endpoint path to collapse/expand
   - Double-click text in examples to copy

4. **Save Time**
   - Once authorized, test multiple endpoints
   - Modify examples instead of typing from scratch
   - Keep the docs open while developing

## 🎓 Learn More

Each endpoint shows:
- What it does (description)
- What it needs (parameters, body)
- What it returns (response schema)
- What can go wrong (error codes)

Click around, try things out - you can't break anything!

---

**Happy API Testing! 🚀**

Need help? Check the error messages - they're descriptive now!
