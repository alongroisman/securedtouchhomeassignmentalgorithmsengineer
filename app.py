#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 16:06:15 2019

@author: alon
"""

from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import json

import os

app = Flask(__name__)


               
class Model:
    def __init__ (self,d):
        self.data=d
        self.dic={}
        for i in self.data['parameters']:
           self.dic[i['feature_name']]= i
        self.type= self.data["type"]
         
            

    def predict(self,feauters):
        result = self.data['offset']       
        for k, v in self.dic.items():
             if k not in feauters.keys():
                  print ("bug bug") #throw exception
             normlizes_value = (feauters[k]-v['mean'])/np.sqrt(v['variance'])
             result+=normlizes_value*v['parameter']
        return result
        
           

 
@app.route('/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))

    return jsonify(prediction)

if __name__ == '__main__':
    path = '/home/alon/Downloads/asdasdasd/a/'
    dModels={}
    fileList = os.listdir(path)
    for file in fileList:
       with open(path+file) as json_file:  
           data = json.load(json_file)       
           model =  Model(data)
           dModels[data["type"]]=model

    
    dExample={}
    dExample["area"]=5.5
    dExample["rooms"]=2
    dExample["years_since_build"]=1

    res= dModels["a"].predict(dExample)
    app.run(debug=True, use_reloader=True)

