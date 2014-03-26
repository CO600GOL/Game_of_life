# The following code is used in this project with permission from Allan Callaghan, under a CC-SA 3.0 license.
# calaldees@gmail.com
#
# This code has been reconfigured for use in this project. These configurations will be made clear
# by inline comments.

env = . env/bin/activate
deamon_name = projectconway

help:
	# Usage: make <target>, where target is
	# setup         -- setup python egg & install dependencys/env if needed
	# test          -- run all nosetests
	# test_coverage -- compile a document of the test coverage
	# run           -- run in production mode
	# run_develop   -- run the site in development mode
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
	$(env); pserve production.ini

run_develop:
	$(env); pserve --reload development.ini

daemon:
	sudo sh -c 'echo "PROJECTCONWAY_ENV=$(PWD)" | sudo cat > /etc/default/$(deamon_name)'
	sudo sh -c 'echo "PROJECTCONWAY_ARGS=\"$(PWD)/production.ini\"" | sudo cat >> /etc/default/$(deamon_name)'
	sudo sh -c 'echo "PROJECTCONWAY_LOG=\"/var/log/projectconway.log\"" | sudo cat >> /etc/default/$(deamon_name)'

shell:
	$(env); pshell development.ini

clean:
	rm env -rf
	rm *.egg-info -rf
