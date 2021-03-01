from flask import Flask, request, render_template, url_for, redirect
from service_4 import app
import requests
import os

# route for service 2


@app.route('/code_part_3', methods=['GET'])
def code_part_3():
    # where the code is decided
    code_p3 = ""
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        code_p3 += str(choice[randrange(len(choice))])

    str(code_p3)

    return code_p3
