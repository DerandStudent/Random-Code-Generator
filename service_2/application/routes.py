from flask import Flask, request, render_template, url_for, redirect
from application import app
import requests
import os

# route for service 2


@app.@app.route('/code_part_1', methods=['GET'])
def code_part_1():
    # where the code is decided
    choice = ["A", "B", "C", "D", "E", "F"]
    code_p1 = choice[randrange(len(choice))]

    str(code_p1)

    return code_p1
