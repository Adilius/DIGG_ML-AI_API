# DIGG project A.
Enabling open data for machine learning and AI

# Setup

Clone the repository: `git clone https://github.com/Adilius/DIGG_ML-AI_API.git`

# Run docker

Start docker desktop

Build & run docker image: `docker-compose up`

Build & run docker image from scratch: `docker-compose up --build --force-recreate`

# Run single files

Run build & run docker first

Open bash terminal in virtual enviroment: `docker exec -it api bash`

# Run tests

Test API service: `docker-compose exec api_service pytest . -v`

Test DB service: `docker-compose exec db_service pytest . -v`

# Access url to API docs

Docs urls: http://localhost:8080/docs

| Link        | ~Time           |
| ------------- |:-------------:|
| [Kronofogden1](https://kronofogden.entryscape.net/rowstore/dataset/9a1d6efb-d34c-4b8c-890f-f1625050a6bd?_limit=500&_offset=0)      | 11s |
| [Kronofogden2](https://kronofogden.entryscape.net/rowstore/dataset/84b8876c-091a-4b00-a625-918060ce10b9?_limit=500&_offset=0)      | 13s |
| [Kronofogden3](https://kronofogden.entryscape.net/store/2/resource/201)      | 11s |
| [Konsumentverket1](https://konsumentverket.entryscape.net/rowstore/dataset/ee53f020-2d4a-4a77-bffd-2b940dec5589)      | 11s |

# Project structure

```
├── api-service                         # Directory for API service container
│   ├── Dockerfile                      # Dockerfile for API service container
│   ├── requirements.txt                # Requirements for Python modules used by container
│   │
│   └── app                             # Directory containing all application logic
│       ├── __init__.py                 # Initialize module 
│       ├── main.py                     # Starts FastAPI server
│       └── router                      # Contains logic for /api/ routes
│           ├── __init__.py             # Initialize module
│           └── api.py                  # Handles /api/ routes
│
├── db-service                          # Directory for database service container
│   ├── Dockerfile                      # Dockerfile for database service container
│   ├── requirements.txt                # Requirements for Python modules used by container
│   │
│   ├── alembic                         # Directory containing logic for creating database structure
│   │   ├── versions                    # Directory containing most recent database structure
│   │   │   └── new_migration.py        # Conversion file from python class to database tables
│   │   ├── env.py                      # Envionment file for alembic and access to database
│   │   ├── README                      # Alembic explained
│   │   └── script.py.mako              # Updates migrationfiles when needed
│   ├── models.py                       # Database structure defined by python class
│   ├── alembic.ini                     # Initialize alembic conversion from models.py
│   │                                   
│   ├── schema.py                       # Defines response format for database api
│   ├── app                             # Directory containing all database api logic
│   │   └── main.py                     # Database api logic for handling database data
│   │
│   └── tests                           # Directory containing all database testing
│       ├── __init__.py                 # Initialize module
│       ├── conftest.py                 # Runs the tests
│       ├── test_database_add_data.py   # Test validation on database Posting
│       └── test_database_root.py       # Checking if database is running
│
├── docker-compose.yml                  # Creates all docker containers
├── nginx_config.conf                   # Config file for Nginx 
├── README.md                           # This file
```

# Useful git commands
List new or modified files not yet commited: `git status`

Fetch the latest changes from origin and merge: `git pull`

Stages all changed files: `git add .`

Commit staged files: `git commit -m "commit message`

Push local changes to Github: `git push`

Create new branch: `git checkout -b branchname`

Push new branch to Github: `git push origin branchname`
 
delete branch locally: `git branch -d localBranchName`

delete branch remotely: `git push origin --delete remoteBranchName`

# DB commands
Create new migration from models.py: `docker-compose run db_service alembic revision --autogenerate -m "New Migration"`

Update database with new migration: `docker-compose run db_service alembic upgrade head`

# PGAdmin
Link: http://localhost:5050

Username: admin@admin.com

Password: admin

Create server manually (for now): 

    General:

        Name: db

    Connection:

        Host: db

        Port: 5432

        Maintenance database: postgres

        Username: postgres

        Password: password
