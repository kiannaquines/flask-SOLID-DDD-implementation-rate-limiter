# JWT Token Format Guide

## ⚠️ Common Error: Missing 'Bearer' in Authorization Header

### The Error
```json
{
  "msg": "Missing 'Bearer' type in 'Authorization' header. Expected 'Authorization: Bearer <JWT>'"
}
```

### The Problem
You're sending the token without the "Bearer " prefix.

## ✅ Correct Format

### In curl
```bash
# ❌ WRONG - Missing "Bearer"
curl -X GET 'http://127.0.0.1:5000/api/v1/tasks/' \
  -H 'Authorization: vcxvcvcxvxcvcxvcxv'

# ✅ CORRECT - Includes "Bearer " prefix
curl -X GET 'http://127.0.0.1:5000/api/v1/tasks/' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...'
```

### In Swagger UI
When you click the "Authorize" button:

```
❌ WRONG:
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

✅ CORRECT:
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### In Code (Python requests)
```python
import requests

# ❌ WRONG
headers = {
    'Authorization': 'your_token_here'
}

# ✅ CORRECT
headers = {
    'Authorization': 'Bearer your_token_here'
}

response = requests.get(
    'http://127.0.0.1:5000/api/v1/tasks/',
    headers=headers
)
```

### In JavaScript (fetch)
```javascript
// ❌ WRONG
fetch('http://127.0.0.1:5000/api/v1/tasks/', {
  headers: {
    'Authorization': 'your_token_here'
  }
})

// ✅ CORRECT
fetch('http://127.0.0.1:5000/api/v1/tasks/', {
  headers: {
    'Authorization': 'Bearer your_token_here'
  }
})
```

## 📝 Complete Workflow

### Step 1: Login
```bash
curl -X POST 'http://127.0.0.1:5000/api/v1/auth/login' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "your_username",
    "password": "your_password"
  }'
```

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODM2MDAwMCwianRpIjoiYWJjZDEyMzQiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiam9obl9kb2UiLCJuYmYiOjE2MzgzNjAwMDAsImV4cCI6MTYzODM2MzYwMH0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
}
```

### Step 2: Copy the Token
Copy the entire `access_token` value (the long string).

### Step 3: Use with Bearer Prefix
```bash
curl -X GET 'http://127.0.0.1:5000/api/v1/tasks/' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODM2MDAwMCwianRpIjoiYWJjZDEyMzQiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoiam9obl9kb2UiLCJuYmYiOjE2MzgzNjAwMDAsImV4cCI6MTYzODM2MzYwMH0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c'
```

## 🔍 Error Messages Explained

### 1. Missing 'Bearer' Type
```json
{
  "message": "Invalid token format. Use 'Authorization: Bearer <your_token>'",
  "error": "invalid_token",
  "hint": "Make sure to include 'Bearer ' before your token"
}
```
**Solution:** Add "Bearer " before your token.

### 2. Missing Authorization Header
```json
{
  "message": "Authorization header is missing. Please provide a valid JWT token.",
  "error": "authorization_required",
  "hint": "Use 'Authorization: Bearer <your_token>' in the request header"
}
```
**Solution:** Include the Authorization header in your request.

### 3. Token Expired
```json
{
  "message": "The token has expired. Please login again to get a new token.",
  "error": "token_expired"
}
```
**Solution:** Login again to get a fresh token (tokens expire after 1 hour).

### 4. Token Revoked
```json
{
  "message": "The token has been revoked. Please login again.",
  "error": "token_revoked"
}
```
**Solution:** Login again to get a new token.

## 💡 Key Points

1. **Always include "Bearer "** - This is the authentication scheme name
2. **Case sensitive** - Use "Bearer" with capital B
3. **One space** - There's exactly one space between "Bearer" and your token
4. **Full token** - Include the entire token string (all three parts separated by dots)
5. **Header name** - Use "Authorization" (not "Auth" or "Token")

## 🎯 Format Template

```
Authorization: Bearer <token>
               ↑      ↑
               |      |
               |      +-- Your JWT token
               |
               +-- Must be "Bearer " (with space)
```

## ✅ Testing Your Token

### Quick Test
```bash
# Set your token as a variable
TOKEN="your_token_here"

# Test it
curl -X GET 'http://127.0.0.1:5000/api/v1/tasks/' \
  -H "Authorization: Bearer $TOKEN"
```

### Verify Token Format
Your token should look like this:
```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODM2MDAwMH0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
↑ Header (base64)                  ↑ Payload (base64)                        ↑ Signature (base64)
```

Three parts separated by dots (`.`).

## 📱 In Swagger UI

1. Click the **"Authorize"** button (green lock icon at top)
2. In the popup, enter: `Bearer ` followed by your token
3. Click **"Authorize"**
4. Click **"Close"**
5. Now all protected endpoints will use this token automatically

**Example entry in Swagger:**
```
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzODM2MDAwMH0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

---

**Remember:** The word "Bearer" tells the server what type of authentication you're using. It's required by the JWT specification!
