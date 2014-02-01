import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_chameleon',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
    'waitress',
    'pytest',
    'pexpect'
    ]

setup(name='ProjectConway',
      version='0.0',
      description='ProjectConway',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Michael Wilson, Richard Lancaster, Geoff Doffs, Niklas Scholz',
      author_email='mw362@kent.ac.uk, rl221@kent.ac.uk, gd96@kent.ac.uk, ns468@kent.ac.uk',
      url='https://github.com/CO600GOL/Game_of_life',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='projectconway',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = projectconway:main
      [console_scripts]
      initialize_ProjectConway_db = projectconway.scripts.initializedb:main
      """,
      )
