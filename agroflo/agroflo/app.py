#importing the necessary libraries
from flask import Flask,render_template,url_for,request,jsonify
from flask_restful import reqparse, abort, Api, Resource
import urllib.request, json
import os
import pickle
import string, os
import warnings
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing

data = pd.read_csv('crop_data.csv')


def generate_crop(state, cost_hectare, cost_quintal,model):
    le = preprocessing.LabelEncoder()
    state_encoded = le.fit_transform(data.State.tolist())
    encoded = le.transform([state])
    predicted_crop = model.predict([[encoded, int(cost_hectare), int(cost_quintal)]])[0]
    return predicted_crop


model = pickle.load(open('software_1.pkl','rb'))

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('main.html')

#For displaying predicted value
@app.route('/predict',methods=['GET', 'POST'])
def predict():
    warnings.filterwarnings("ignore")
    warnings.simplefilter(action = 'ignore',category = FutureWarning)

    if request.method == 'POST':
        message1 = request.form['message1']
        message2 = request.form['message2']
        message3 = request.form['message3']
        my_prediction = generate_crop(state = message1,cost_hectare = message2,cost_quintal = message3,model = model)
    return render_template('main.html',prediction = my_prediction)


if __name__ == '__main__':
  app.run(debug = True, use_reloader = False)
