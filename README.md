# bale-bot-template
An MVC template to implement a bale bot.

Bale is a popular messanger in iran that is basically used for finantial
transactions. 

## Getting Started

# Enviroment setup
First install requirments and create a virtual environment for the project
using codes below:
```
sudo apt-get install python3-pip python3-dev
sudo pip3.6 install virtualenvwrapper
echo "export VIRTUALENVWRAPPER_PYTHON=`which python3.6`" >> ~/.bashrc
echo "alias v.activate=\"source $(which virtualenvwrapper.sh)\"" >> ~/.bashrc
source ~/.bashrc
v.activate
mkvirtualenv --python=$(which python3.6) --no-site-packages bale_template
```

Clone the project with the following link:
```
git@github.com:mkhfring/bale-bot-template.git
```

start working on your virtual enviroment and then use the following commands:
```
pip install -e .
pip install -r requirements.txt
bale_template start
```
to attach this code to your own bot, please get a token from botfather in bale
and then issue your token in config.py

### Prerequisites

requirements for the project are listed in requirements.txt


## Deploy
To deploy this application, The docker-comopose.yml.example should be fill out
with approperiate values Then should be start by run docker-compose up -d
