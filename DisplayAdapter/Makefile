# Makefile for the DisplayAdapter application, ie the programs that run on the pi for ProjectConway

env_name = display_env
env = . $(env_name)/bin/activate
screensavers_file = screensavers.txt
script_local = display_adapter/scripts
db_name = ./internal_db.sqlite

help:
	# This makefile aids in the installation of the ProjectConway software on the Raspberry pi
	# Commands:
	#     setup                  -- Creates a virtual environment in which the software is ran from
	#     test                   -- Runs the automated tests in DisplayAdapter
	#     create_db              -- Creates and initialises the internal database
	#     update_screensavers    -- Search screensavers file and update the database
	#     clean                  -- Delete persistant storage

setup: env
	$(env); python setup.py develop
	$(env); cd ../GameEngine/; python setup.py develop
	$(MAKE) create_db
	$(MAKE) update_screensavers
env:
	if dpkg -s python-virtualenv ; then \
	    echo virtualenv already installed; \
	else \
	    echo installing virtualenv; \
	    sudo apt-get install python-virtualenv; \
	fi
	if dpkg -s python3-setuptools ; then \
	    echo python 3 already installed; \
	else \
	    echo installing python 3; \
	    sudo apt-get install python3-setuptools; \
	fi

	virtualenv -p python3 $(env_name)

test:
	$(env); py.test -v testing

create_db:
	$(env); python $(script_local)/init_db.py $(db_name)

update_screensavers:
	$(env); python $(script_local)/update_screensavers.py $(db_name) $(screensavers_file)

clean:
	rm $(env_name) -rf
	rm *.egg-info -rf

