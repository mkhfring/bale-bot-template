from setuptools import setup, find_packages
import os.path
import re

# reading package's version (same way sqlalchemy does)
with open(
    os.path.join(os.path.dirname(__file__), 'bot_template', '__init__.py')
) as v_file:
    package_version = \
        re.compile('.*__version__ = \'(.*?)\'', re.S)\
        .match(v_file.read())\
        .group(1)


dependencies = [
    'balebot==1.6.12',
]


setup(
    name='vip_adimin',
    version=package_version,
    author='Mohamad Khajezade',
    author_email='khajezade.mohamad@gmail.com',
    description='A bale bot for account officer administration tasks',
    install_requires=dependencies,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'bot_template = bot_template.cli.starter:main'
        ]
    }
)
