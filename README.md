todo_app/
│
├── app/
│   ├── main.py                # FastAPI app entry point
│   │
│   ├── core/                  # Core application logic
│   │   ├── config.py          # Settings, env variables
│   │   ├── security.py        # JWT, password hashing
│   │   └── database.py        # DB connection
│   │
│   ├── models/                # Database models (ORM)
│   │   ├── user.py
│   │   └── todo.py
│   │
│   ├── schemas/               # Pydantic schemas (request/response)
│   │   ├── user.py
│   │   ├── todo.py
│   │   └── token.py
│   │
│   ├── repositories/          # DB operations (CRUD logic)
│   │   ├── user_repo.py
│   │   └── todo_repo.py
│   │
│   ├── services/              # Business logic
│   │   ├── auth_service.py
│   │   └── todo_service.py
│   │
│   ├── api/                   # Routes (like Django urls)
│   │   ├── deps.py            # Dependencies (current user)
│   │   │
│   │   ├── v1/
│   │   │   ├── auth.py        # Login / Register APIs
│   │   │   └── todo.py        # Todo APIs
│   │
│   └── utils/                 # Helper utilities
│       └── response.py
│
├── .env                       # Environment variables
├── requirements.txt
├── alembic/                   # DB migrations (if SQL DB)
├── README.md
└── run.py                     # Optional run file
