# Ping Tester

Ping Tester is a simple Python script that regularly tests the ping and connectivity of a list of URLs. It records the results in CSV files for each website, including details such as response status, ping time, and more.


## To create the local environment:

````shell
pyenv local && pyenv install
virtualenv --python=`pyenv which python` venv
source venv/bin/activate
pip install pip setuptools --upgrade
pip install -r game/requirements.txt
````

## To Run Docker

````shell
docker build -t ping-tester .
docker run -d --name ping-tester-container ping-tester
````
