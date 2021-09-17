# DIGG project A.
Enabling open data for machine learning and AI

# Setup

Clone the repository: `git clone https://github.com/Adilius/DIGG_ML-AI_API.git`

# Run docker

Start docker desktop

Build & run docker image: `docker-compose up`

# Run single files

Run build & run docker first

Open bash terminal in virtual enviroment: `docker exec -it api bash`

# Access urls to docker

Root url: http://localhost:8080/

Docs urls: http://localhost:8080/docs

Dataset url: http://localhost:8080/api/ (where our logic goes)

Dataset test url: http://localhost:8080/api/url/?url=https://opendata.umea.se/api/v2/catalog/datasets/skyddade-omraden-djur-och-vaxtskyddsomraden-sverigesweden/records

# Project structure

```
├── api-service             # Directory for API service container
│   ├── Dockerfile          # Dockerfile for API service container
│   ├── requirements.txt    # Requirements for Python modules used by container
│   └── app                 # Directory containing all application logic
│       ├── __init__.py     # Initialize module 
│       ├── main.py         # Starts FastAPI server
│       └── router          # Contains logic for /api/ routes
│           ├── __init__.py # Initialize module
│           └── api.py      # Handles /api/ routes
```

# Useful git commands
List new or modified files not yet commited: `git status`

Fetch the latest changes from origin and merge: `git pull`

Stages all changed files: `git add .`

Commit staged files: `git commit -m "commit message`

Push local changes to Github: `git push`

Create new branch: `git checkout -b branchname`

<<<<<<< HEAD
Push new branch to Github: 'git push origin branchname`

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

=======
Push new branch to Github: `git push origin branchname`
 
delete branch locally: `git branch -d localBranchName`

delete branch remotely: `git push origin --delete remoteBranchName`
>>>>>>> 3ce474f2d04585286d1537593a3e28418a2fc7fe
