# FastAPI Todo Application

## Project Structure

```text
todo_app/
├── app/
│   ├── main.py                # FastAPI app entry point
│   ├── core/                  # Core application logic
│   │   ├── config.py          # Settings, env variables
│   │   ├── security.py        # JWT, password hashing
│   │   └── database.py        # DB connection
│   ├── models/                # Database models (ORM)
│   │   ├── user.py
│   │   └── todo.py
│   ├── schemas/               # Pydantic schemas
│   │   ├── user.py
│   │   └── todo.py
│   ├── repositories/          # DB operations (CRUD)
│   │   ├── user_repo.py
│   │   └── todo_repo.py
│   ├── services/              # Business logic
│   │   ├── auth_service.py
│   │   └── todo_service.py
│   ├── api/                   # Routes (like Django urls)
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── auth.py
│   │       └── todo.py
│   ├── utils/                 # Helper utilities
│   │   └── response.py
├── .env                       # Environment variables
├── requirements.txt
├── alembic/                   # DB migrations (SQL)
├── README.md
└── run.py                     # Optional run file
