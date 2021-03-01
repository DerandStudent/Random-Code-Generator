from flask import Flask, request
from service_1 import routes
import requests
import os

app = Flask(__name__)
