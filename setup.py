#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='funsql',
    version='0.2.1',
    description='highlights sql syntax, and use template files to generate code',
    url='https://db2sql.com/funsql',
    author='Mahdi Jadaliha',
    author_email='jadaliha@gmail.com',
    license='MIT',
    py_modules = ['funsql','funsql.src','funsql.src.template', 'funsql.src.pghook'],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'psycopg2', 'pandas'
    ],
    data_files=[
        ('templates', ['funsql/data/sql_templates.sql']),
        ('keywords', ['funsql/data/sql_keywords.txt'])
    ],
    zip_safe=False)