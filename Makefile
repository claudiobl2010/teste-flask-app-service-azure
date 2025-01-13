setup:
	@PIP_REQUIRE_VIRTUALENV=1 pip install -r requirements.txt --no-deps

start:
	@FLASK_ENV=development \
	FLASK_APP=server/app.py \
	flask run --host 0.0.0.0 --port 5000

gunicorn:
	@gunicorn --bind 0.0.0.0:5000 --chdir server --workers 1 app:app