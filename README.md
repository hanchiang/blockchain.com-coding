
# How to use
* Install [python 3](https://www.python.org/downloads/)
* Create a virtual environment: `python3 -m venv venv`
* Activate virtual environment: `source venv/bin/activate`
* Install dependencies: `pip -r install requirements.txt`
* Set PYTHONPATH: `export PYTHONPATH=$(pwd)`
* Start server: `uvicorn --reload --app-dir src main:app`
  * Server runs at: `localhost:8000`
  * API documentation runs at: `localhost:8000/docs`, `localhost:8000/redoc`.
* Run test: `pytest`

