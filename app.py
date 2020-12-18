# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 08:24:54 2020

@author: g
"""

from flask import Flask

UPLOAD_FOLDER = 'C:/Users/g/dti1/uploads'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER