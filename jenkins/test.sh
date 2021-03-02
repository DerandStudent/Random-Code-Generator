#!/bin/bash
#test service 1
cd service_1
#install requirements.txtx dependencies
pip3 install -r requirements.txt .
#run the test coverage
python3 -m pytest --cov
#finish
cd ..