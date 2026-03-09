# 🚀 BlogHub API

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![Flutter](https://img.shields.io/badge/Flutter-Frontend-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

BlogHub API is a backend service built using **FastAPI** that powers a blog platform.

It provides secure **JWT Authentication**, **Role-Based Access Control**, and complete **CRUD operations** for managing users and blog posts.

The **backend** is developed using **Python (FastAPI)** and the **mobile frontend** is built using **Flutter**.

---

# 📌 Features

- 🔐 JWT Authentication
- 👥 Role-Based Access Control
- 🧑‍💻 User Management
- 📝 Blog Post Management
- ⚡ RESTful API Design
- 🔒 Secure Password Hashing
- 🧩 Modular FastAPI Architecture
- 📚 Interactive API Documentation (Swagger)

---

# 🛠 Tech Stack

## Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- JWT Authentication
- Uvicorn

## Frontend
- Flutter
- Dart

## Tools
- Git
- GitHub
- Swagger UI
- Postman
- Thunder Client

---

# 📂 Project Structure

```bash
BLOGHUB
│
├── app
│   │
│   ├── core
│   │   └── security.py
│   │
│   ├── crud
│   │   ├── users.py
│   │   └── post.py
│   │
│   ├── models
│   │   ├── users.py
│   │   └── post.py
│   │
│   ├── routers
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── post.py
│   │
│   ├── schemas
│   │   ├── users.py
│   │   └── post.py
│   │
│   ├── database.py
│   └── main.py
│
├── venv
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/bloghub.git
cd bloghub
```

---

# 🐍 Backend Setup

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Linux / Mac

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run FastAPI Server

```bash
uvicorn app.main:app --reload
```

Server will run at:

```
http://127.0.0.1:8000
```

---

# 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 🔐 Authentication

Authentication is implemented using **JWT (JSON Web Token)**.

## Authentication Flow

1️⃣ User registers  
2️⃣ User logs in  
3️⃣ Server returns **JWT Token**  
4️⃣ Client sends token in request headers

Example:

```http
Authorization: Bearer <your_token>
```

---

# 👥 User APIs

| Method | Endpoint | Description |
|------|------|------|
| GET | `/users/` | Get all users |
| GET | `/users/{user_id}` | Get user by ID |
| PUT | `/users/{user_id}` | Update user |
| DELETE | `/users/{user_id}` | Deactivate user |
| DELETE | `/users/hard/{user_id}` | Permanently delete user |

---

# 🔑 Authentication APIs

| Method | Endpoint | Description |
|------|------|------|
| POST | `/auth/register` | Register new user |
| POST | `/auth/login` | Login user |

---

# 📝 Post APIs

| Method | Endpoint | Description |
|------|------|------|
| GET | `/posts/` | Get all posts |
| POST | `/posts/` | Create new post |
| GET | `/posts/{post_id}` | Get post by ID |
| PUT | `/posts/{post_id}` | Update post |
| DELETE | `/posts/{post_id}` | Delete post |

---

# 🔒 Security

Security measures implemented:

- Password hashing using **bcrypt**
- **JWT Token Authentication**
- **Protected Routes**
- **Role-Based Access Control**
- **User Ownership Validation for Posts**

---

# 🧪 API Testing

You can test APIs using:

- Swagger UI
- Postman
- Thunder Client (VS Code Extension)

Swagger UI:

```
http://localhost:8000/docs
```

---

# 👨‍💻 Contributors

### Backend
**Soham Reshamwala**  
FastAPI Developer

### Frontend
**Deep Patel**  
Flutter Developer  

GitHub:  
https://github.com/deeppatel2610

Flutter Repository:  
https://github.com/deeppatel2610/blog_hub

---

# ⭐ Support

If you like this project, please consider giving it a **star ⭐ on GitHub**.

---

# 📄 License

This project is licensed under the **MIT License**.
