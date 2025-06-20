from setuptools import setup


setup(
    name='taskaty',
    version='0.1.0',
    description='A simple command-line Task-app written by python',
    author='Amoor',
    install_requirs = '[tabulate]',
    entry_pointa = {
            'cpnsole scripts' : [
                'taskaty:taskaty:main',
            ],


    },
)

