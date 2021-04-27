python=python3
manage=./manage.py

runserver:
	$(python) $(manage) runserver

check:
	$(python) $(manage) check

migrate:
	$(python) $(manage) makemigrations && $(python) $(manage) migrate

shell:
	$(python) $(manage) shell_plus

superuser:
	$(python) $(manage) createsuperuser

freze:
	pip freeze > requirements.txt
