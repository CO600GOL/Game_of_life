# The following code is used in this project with permission from Allan Callaghan, under a CC-SA 3.0 license.
# calaldees@gmail.com
#
# This code has been reconfigured for use in this project. These configurations will be made clear
# by inline comments.

help:
	# Usage: make <target>, where target is
	# setup         -- setup python egg & install dependencys/env if needed
	# test          -- run all nosetests
	# blank-db      -- create a blank database
	# run           -- run the site in development mode
	# run_production -- run in production mode
	# clean         -- reset the folder to clean git checkout (removes virtual python env)

env_activate:
	source env/bin/activate
env_deactivate:
	deactivate

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
	cd env;	bin/easy_install pyramid

setup: env
	cd ProjectConway; ../env/bin/python setup.py develop
	cd src; ../env/bin/python setup.py develop

run:
	#$(MAKE) env_activate
	env/bin/pserve --reload ProjectConway/development.ini
	#$(MAKE) env_deactivate

run_production:
	env/bin/pserve production.ini

shell:
	env/bin/pshell development.ini

test:
	. env/bin/activate;	py.test -v src ProjectConway

clean:
	rm env -rf
	rm *.egg-info -rf
