from flask import Flask, request, render_template, url_for, redirect
from service_3 import app
import requests
import os

# route for service 2


@app.route('/code_part_2', methods=['GET'])
def code_part_2():
    # where the code is decided
    code_p2 = ""
    choice = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(4):
        code_p2 += str(choice[randrange(len(choice))])

    str(code_p2)

    return code_p2
