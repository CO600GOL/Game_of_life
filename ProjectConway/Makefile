# The following code is used in this project with permission from Allan Callaghan, under a CC-SA 3.0 license.
# calaldees@gmail.com
#
# This code has been reconfigured for use in this project. These configurations will be made clear
# by inline comments.

env = . env/bin/activate

help:
	# Usage: make <target>, where target is
	# setup         -- setup python egg & install dependencys/env if needed
	# test          -- run all nosetests
	# test_coverage -- compile a document of the test coverage
	# run           -- run the site in development mode
	# run_production -- run in production mode
	# shell         -- Runs the development shell
	# clean         -- reset the folder to clean git checkout (removes virtual python env)

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
	    sudo apt-get install python3-setuptools python-setuptools; \
	fi
	# Reference - http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/narr/install.html
	virtualenv --no-site-packages -p python3 env
	$(env); easy_install pyramid

setup: env
	$(env); python setup.py develop
	$(env); cd ../GameEngine/; python setup.py develop

test:
	$(env);	py.test -v projectconway

test_coverage:
	$(env); py.test --cov-config .coveragerc --cov projectconway projectconway/testing --cov-report html

run:
	$(env); pserve --reload development.ini

run_production:
	$(env); pserve production.ini

shell:
	$(env); pshell development.ini

clean:
	rm env -rf
	rm *.egg-info -rf
