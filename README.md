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

## Installation

# Clone repository
git clone https://github.com/tahammalik/auth-api
cd auth-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  for  Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment files
cp .env.example .env      # Database configuration
cp .key.example .key      # JWT secrets (keep this secure!)


# Start the server
uvicorn main:app --reload --port 8000

## Project structure 
AUTH-API/
├── app/
│   ├── api/v1/              # API Routes (Version 1)
│   │   └── auth.py          # Authentication endpoints
│   │
│   ├── core/                # Core Configuration
│   │   ├── config.py        # App configuration & settings
│   │   ├── db.py            # Database connection
│   │   ├── dependencies.py  # FastAPI dependencies
│   │   ├── exceptions.py    # Custom exceptions
│   │   ├── redis_client.py  # Redis connection
│   │   └── security.py      # Security utilities (hashing, JWT)
│   │
│   ├── models/              # SQLAlchemy Models
│   │   └── user.py          # User database model
│   │
│   ├── schemas/             # Pydantic Schemas
│   │   ├── token.py         # Token schemas
│   │   └── user.py          # User schemas
│   │
│   ├── services/            # Business Logic
│   │   ├── auth_service.py  # Authentication logic
│   │   └── otp_service.py   # OTP generation/verification
│   │
│   └── main.py              # FastAPI application entry
|             
├── .gitignore               # Git ignore rules
├── README.md                # This file
└── requirements.txt         # Python dependencies