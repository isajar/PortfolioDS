#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:58:18 2021

@author: isajarspector
"""

from flask import Flask

from flask_restful import Api, Resource, reqparse

from joblib import load

from tensorflow.keras.models import load_model

from sklearn.preprocessing import MinMaxScaler

from flask_cors import CORS

import numpy as np

APP = Flask(__name__)
API = Api(APP)

CORS(APP)

# load trained model from memory.
lm = load('model.joblib')

tf_model = load_model('tf_model.h5')

scaler = load('scaler.joblib')


class Predict(Resource):
    
    @staticmethod
    def post():
        
        # get each feature from the request
        
        parser = reqparse.RequestParser()
        parser.add_argument('CRIM')
        parser.add_argument('ZN')
        parser.add_argument('INDUS')
        parser.add_argument('CHAS')
        parser.add_argument('NOX')
        parser.add_argument('RM')
        parser.add_argument('AGE')
        parser.add_argument( 'DIS')
        parser.add_argument('RAD')
        parser.add_argument('TAX')
        parser.add_argument('PTRATIO')
        parser.add_argument( 'B')
        parser.add_argument('LSTAT')

        # parsing 
        args = parser.parse_args()
        
        # make a numpy array from the request
        X_new = np.fromiter(args.values(), dtype=float)
        
        # get the prediction from the model
        out = {'prediction': lm.predict([X_new])[0]}

        # return prediction
        return out, 200
    
class PredictTF(Resource):
    @staticmethod
    def post():
        
        # get each feature from the request
        
        parser = reqparse.RequestParser()
        parser.add_argument('CRIM')
        parser.add_argument('ZN')
        parser.add_argument('INDUS')
        parser.add_argument('CHAS')
        parser.add_argument('NOX')
        parser.add_argument('RM')
        parser.add_argument('AGE')
        parser.add_argument( 'DIS')
        parser.add_argument('RAD')
        parser.add_argument('TAX')
        parser.add_argument('PTRATIO')
        parser.add_argument( 'B')
        parser.add_argument('LSTAT')

        # parsing 
        args = parser.parse_args()
        
        # make a numpy array from the request
        X_new = np.fromiter(args.values(), dtype=float)
        
        # scaling using the saved scaler 
        X_new = scaler.transform(X_new.reshape(1, -1))
        
        prediction =  tf_model.predict(X_new)[0]
        
        # get the prediction from the model
        out = {'prediction': float(prediction[0])}
     
        # return prediction
        return out, 200 
        

# set the path for the endpoint and add it to the API
API.add_resource(Predict, '/predict')
API.add_resource(PredictTF, '/predict-tf')

if __name__ == '__main__':
    APP.run(debug=True, port='1081')