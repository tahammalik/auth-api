# Auth API
**Production-ready authentication API with JWT, Redis rate limiting, and Argon2 password hashing**

## ✨ Features

- ✅ **JWT Authentication** - Access tokens with 15-minute expiry
- ✅ **Argon2 Password Hashing** - Industry-standard password security with peppering
- ✅ **Account Lockout** - 5 failed attempts = 30-minute lockout (Redis-based)
- ✅ **Email Uniqueness** - Duplicate email prevention
- ✅ **PostgreSQL Database** - SQLAlchemy ORM with connection pooling
- ✅ **Redis Integration** - Failed attempt tracking & account lockout
- ✅ **CORS Support** - Configured for cross-origin requests
- ✅ **Custom Exception Handlers** - UserNotFound, EmailExists, AccountLocked
- ✅ **Pydantic Validation** - Request/response validation with custom validators
- ✅ **Swagger Documentation** - Auto-generated API docs at `/docs`
- ✅ **Logging** - Structured logging for user actions & errors
- ✅ **Dependency Injection** - FastAPI's built-in DI for database sessions

## 🛠️ Tech Stack

**Framework** | FastAPI 0.135.2 |
**ORM** | SQLAlchemy 2.0.48 |
**Database** | PostgreSQL (psycopg2-binary) |
**Cache/Lockout** | Redis 7.4 |
**Password Hashing** | Argon2-cffi 25.1.0 |
**JWT** | PyJWT 2.12.1 |
**Validation** | Pydantic 2.12.5 + Email-validator |
**Config Management** | Pydantic-settings 2.13.1 |
**Server** | Uvicorn 0.42.0 |
**Security** | Passlib (via argon2), Python-multipart |

# Clone repository
```bash
git clone https://github.com/tahammalik/auth-api
cd auth-api
```

# Create virtual environment
python -m venv venv
source venv/bin/activate  for  Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment files
```text
cp .env.example .env      # Database configuration
cp .key.example .key      # JWT secrets (keep this secure!)
```

# Start the server
uvicorn main:app --reload --port 8000

## Project Structure

```text
AUTH-API/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── auth.py
│   ├── core/
│   │   ├── config.py
│   │   ├── db.py
│   │   ├── dependencies.py
│   │   ├── exceptions.py
│   │   ├── redis_client.py
│   │   └── security.py
│   ├── models/
│   │   └── user.py
│   ├── schemas/
│   │   ├── token.py
│   │   └── user.py
│   └── services/
│       ├── auth_service.py
│       └── otp_service.py
├── main.py
├── .gitignore
├── README.md
└── requirements.txt
