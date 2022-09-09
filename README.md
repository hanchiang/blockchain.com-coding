
# Set up
* Install [python 3](https://www.python.org/downloads/)
* Create a virtual environment: `python3 -m venv venv`
* Activate virtual environment: `source venv/bin/activate`
* Install dependencies: `pip -r install requirements.txt`
* Set PYTHONPATH: `export PYTHONPATH=$(pwd)`
* Start server: `uvicorn --reload --app-dir src main:app`
  * Server runs at: `localhost:8000`
  * API documentation runs at: `localhost:8000/docs`, `localhost:8000/redoc`.
* Run test: `pytest`

# Set up with docker
* Install [docker](https://docs.docker.com/get-docker/)
* Start development server: `docker-compose up -d`
  * Server runs at: `localhost:8000`
* Run test: `docker-compose -f docker-compose.test.yml up`