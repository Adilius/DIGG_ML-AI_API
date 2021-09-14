# DIGG project A
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

Create new branch: `git checkout -b branchname`

Push new branch to Github: 'git push origin branchname`
