# DIGG project A
Enabling open data for machine learning and AI

# Setup
Clone the repository: `git clone https://github.com/Adilius/DIGG_ML-AI_API.git`

Change directory to repoitory: `cd DIGG_ML-AI_API`

# Run docker

Start docker desktop

Build & run docker image: `docker-compose up`

# Run single files

Change directory to api-service: ` cd .\api-service\`

Create a virtual enviroment inside the repository with python 3.9.x using virtualenv: `virtualenv -p /path/to/Python/Python39/python.exe venv`

Activate the virtual enviroment: `venv\Scripts\activate`

Install the dependencies using pip: `pip install -r requirements.txt`


# Access urls to docker

Root url: http://localhost:8080/api

Docs urls: http://localhost:8080/api/docs

Dataset url: http://localhost:8080/api/dataset/ (where our logic goes)

Dataset test url: http://localhost:8080/api/dataset/url/?url=https://opendata.umea.se/api/v2/catalog/datasets/skyddade-omraden-djur-och-vaxtskyddsomraden-sverigesweden/records

# Useful git commands
List new or modified files not yet commited: `git status`

Fetch the latest changes from origin and merge: `git pull`

Stages all changed files: `git add .`

Commit staged files: `git commit -m "commit message`

Push local changes to Github: `git push`
