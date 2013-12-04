# The following code is used in this project with permission from
# Allan Callaghan, under a CC-SA 3.0 license. calaldees@gmail.com
#
# This code has been reconfigured for use in this project.
# These configurations will be made clear by inline comments.

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
# CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    # 'SQLAlchemy',
    # 'transaction',
    # 'pyramid_tm',
    # 'pyramid_debugtoolbar',
    # 'zope.sqlalchemy',
    # 'waitress',
    # 'pyramid_beaker',
    # 'decorator',
    # 'zope.interface',
    ]

# Most settings here have been reconfigured to suit our project
setup(name='ProjectConway',
      version='0.1',
      description='A website with which to interface with the Deeson game of \
life display',
      long_description=README + '\n',
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Richard Lancaster',
      author_email='rl221@kent.ac.uk',
      keywords='web pylons pyramid teach learn',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      # test_suite='',
      install_requires=requires,
      # entry_points="""\
      # [paste.app_factory]
      # main = teachprogramming:main
      # [console_scripts]
      # populate_TeachProgramming = teachprogramming.scripts.populate:main
      # """,
      )
