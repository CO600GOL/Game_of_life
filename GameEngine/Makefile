# Makefile for the GameEngine package, this is not intended to be run seperately.
# It is intended to be imported and used in other projects.

env_name = game_env
env = . $(env_name)/bin/activate

help:
	# This makefile aids in the installation of the ProjectConway software on the Raspberry pi
	# Commands:
	#     setup                  -- Creates a virtual environment in which the software is ran from
	#     test                   -- Runs the automated tests in DisplayAdapter
	#     test_coverage			 -- Create html document for test coverage report, folder name: htmlcov
	#     clean                  -- Delete persistant storage

setup: env
	$(env); python setup.py develop
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

test_coverage:
	$(env); py.test --cov-config .coveragerc --cov game testing --cov game_of_life testing --cov-report html

clean:
	rm $(env_name) -rf
	rm *.egg-info -rf
