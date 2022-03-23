# 596-S22-Backend
Backend Repo for 596RL Spring 2022
```
.
├── app
│   ├── __init__.py
│   └── main.py
│   └── models.py
│   └── schemas.py
│   └── database.py
│   └── crud.py
├── Alembic
├── Dockerfile
└── requirements.txt
```

### 👾 MUST BE INSTALLED
```
- Docker
- Alembic     (Locally for database manipulation)
- SQLAlchemy  (Locally for database manipulation)
```

### 👀 Configuring Secrets
To successfully connect to the database, we use a `.env` file, which you will need to generate using:
`touch .env` in the backend directory. This is an untracked file in our repo. Here you will need to paste in the secrets of the backend. DM Sam DuBois and he will send you the file.


### 🚀 How to Run the Container

This repo uses Docker to containerize any processes used. In order to the run the repo, it is advised that you install docker.

Make sure the Docker and the postgresSQL library are working.

From there, all you need to do to run the container is:
```
docker-compose up -d --build
docker-compose up
```

### 🧪 Useful Tools for Debugging and Testing
```
localhost:8000/docs   # This is a place to view all the routes available as well as manipulate them
Postman               # This is a popular dev tool for route testing and debugging (A personal favorite)
```

### 💻 Configuring PostgreSQL Server with Alembic
In order to begin posting to routes and adding in data, you will need to load in all the proper tables. Using Alembic this is really easy.

First, install alembic onto your local machine:
```
pip3 install alembic
```

Next, generate your alembic revision file (this is where you will do all your database modifications)
```
alembic revision -m "<What your revision is>"
```

To make sure your revision is properly written, you can check it with:
```
alembic upgrade head --sql
```

Finally, you need to upgrade the head in order to setup all the tables properly:
```
alembic upgrade head
```

### 💽 Downgrading and Upgrading the Database
Using alembic, you can downgrade to a previous version by typing:
```
alembic downgrade -1
```

Or you can upgrade 1 version by typing:
```
alembic upgrade +1
```
