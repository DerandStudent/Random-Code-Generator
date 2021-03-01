from flask import Flask, request
from application import routes
import requests
import os

app = Flask(__name__)
