export DJANGOPORT := 8000
export DEBUG := True
# you must update the value of HEROKUHOST
export HEROKUHOST := git:remote protected-bastion-43256
PSQL = psql
CMD = python3 manage.py
HEROKU = heroku run export SQLITE=1 &
# Add applications to APP variable as they are
# added to settings.py file
APP = models services
# export DATABASE_URL = postgres://qgdzyaxe:xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx@lucky.db.elephantsql.com/qgdzyaxe

## delete and create a new empty database
#clear_db:
#	@echo Clear Database
#	dropdb --if-exists $(PGDATABASE)
#	createdb

# create alumnodb super user
create_super_user:
	$(CMD) shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('alumnodb', 'admin@myproject.com', 'alumnodb')"

populate:
	@echo populate database
	$(CMD) populate

runserver:
ifeq ($(DEBUG),False)
		@echo "Running in production mode"
		$(CMD) collectstatic --noinput
endif
	$(CMD) runserver $(DJANGOPORT)

update_models:
	$(CMD) makemigrations $(APP)
	$(CMD) migrate

#reset_db: clear_db update_models create_super_user

shell:
	@echo manage.py  shell
	@$(CMD) shell

dbshell:
	@echo manage.py dbshell
	@$(CMD) dbshell

addparticipants:
	@echo populate database
	python3 ./manage.py addparticipants

coverage: coverage_models coverage_services coverage_api

coverage_models:
	@echo "Running coverage (models)"
	coverage erase
	coverage run --omit="*/test*" --source=models ./manage.py test models.test_additional models.test_authentication
	@coverage report -m -i

coverage_services:
	@echo "Running coverage (services)"
	coverage erase
	coverage run --omit="*/test*" --source=services ./manage.py test services.test_additional services.test_services_game
	@coverage report -m -i

coverage_api:
	@echo "Running coverage (api)"
	coverage erase
	coverage run --omit="*/test*" --source=restServer ./manage.py test restServer.test_additional
	@coverage report -m -i

static:
	@echo manage.py collectstatic
	python3 ./manage.py collectstatic

fully_update_db:
	@echo del migrations and make migrations and migrate
	rm -rf */migrations
	python3 ./manage.py makemigrations $(APP) 
	python3 ./manage.py migrate

test_authentication:
	$(CMD) test models.test_authentication --keepdb

test_model:
	$(CMD) test models.test_additional --keepdb
	$(CMD) test models.test_models --keepdb

test_services:
	$(CMD) test services.test_services_game --keepdb
	$(CMD) test services.test_additional --keepdb
#No es necesario ejecutar test_services porque ya se ejecutan en test_additional, que hereda de test_services

test_api:
	$(CMD) test restServer.test_additional --keepdb
#No es necesario ejecutar tests porque ya se ejecutan en test_additional, que hereda de tests
	