#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

__version__ = '0.1.0'

tests_require = [
    'mock',
    'nose',
    'pylons',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'sphinx',
]

setup(
    name='color_schemer',
    version=__version__,
    author='Will Soto',
    author_email='will.soto9+github@gmail.com',
    url='https://github.com/paradox41/color-schemer-api',
    license='TBD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: TBD License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # add your dependencies here
        # remember to use 'package-name',notation (this way you get bugfixes)
        'flask',
        'Flask-Login',
        'Flask-OAuthlib',
        'Flask-SQLAlchemy',
        'Flask-Script',
        'Pygments',
        'SQLAlchemy',
        'alembic',
        'dateutils',
        'fixture',
        'psycopg2',
        'python-dateutil',
        'pytz',
        'pydash',
        'uwsgi',
        'configargparse',
        'ipython',
        # 'resource_alchemy'  # manually installed by docker atm, todo: fix this
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            'color-schemer=manage:main'
        ],
    },
)
