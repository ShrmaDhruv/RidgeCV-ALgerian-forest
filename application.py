import pickle
from flask import Flask,jsonify,render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


application=Flask(__name__)

@application.route('/')
def Hello():
    return '<h1> Hello World</h1>'

if __name__=='__main__':
    application.run(host='0.0.0.0',debug=True)
