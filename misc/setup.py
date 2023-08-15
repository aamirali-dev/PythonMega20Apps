from setuptools import setup

# run this file as
# python setup.py sdist
# this creates a tar.gz file inside dist folder to be uploaded to pypl

# to upload this automatically, pip install twine
# twine upload --skip-existing dist/*
# you need to provide username and password on cmd and this'll upload everyting inside dist to pypl

setup(
    name='invoicing', # must not be taken and must be unique in whole pypl
    packages=['invoicing'],
    version='1.0.0',
    license='MIT',
    description='convert excel to pdf',
    author='Ardit',
    author_email='aamirali@curemd.com',
    keywords=['invoice', 'openpyxl'],
    classifiers=[
        '',
        '',
    ]
)