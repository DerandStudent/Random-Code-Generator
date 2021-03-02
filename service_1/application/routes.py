from typing import Text
from flask import Flask, url_for, redirect, request
from application import app, db
import requests
import random

# the index page


@app.route("/", methods=['GET', 'POST'])
def index():
    url_p1 = "http://code_part_1:5001"
    url_p2 = "http://code_part_2:5002"
    url_p3 = "http://code_part_3:5003"
    # get the generated codes from the other services
    code_part_1 = requests.get(url_p1)
    code_part_2 = requests.get(url_p2)
    code_part_3 = requests.get(url_p3)
    # make sure that they are in the correct format --> string
    code_p1 = code_part_1.text
    code_p2 = code_part_2.text
    code_p3 = code_part_3.text
    # concat the strings into one large randomely generated code
    random_code = str(code_p1) + str(code_p2) + str(code_p3)

    # get the first part of the code
    # --> to decide what sub_code it is
    ###################TODO#############################
    s = code_p1
    if s == "A":
        sub_code = "You Won £10,000"
    if s == "B":
        sub_code = "You Won £1,000"
    if s == "C":
        sub_code = "You Won £100"
    if s == "D":
        sub_code = "You Won £1"
    if s == "E":
        sub_code = "You Won 1p"
    if s == "F":
        sub_code = "Unlucky: No Prize"

    #add to database
    code_db = Codes(code = random_code.text)
    #add
    db.session.add(code_db)
    db.session.commit()
    
    return render_template('index.html', random_code=random_code, sub_code=sub_code)
