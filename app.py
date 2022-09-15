import json
import numpy as np
import joblib
from urllib import request
from flask import Flask,request

app = Flask(__name__)
dicti = json.loads(request.data)
data = dicti["data"]
list = []

@app.route('/',methods=['POST'])

def jalan():
    dicti = json.loads(request.data)
    data = dicti["data"]
    list = []
    
    for data in dicti["data"]:
        list.insert(0,data["age"])
        list.insert(1,data["sex"]) 
        list.insert(2,data["cp"]) 
        list.insert(3,data["trestbps"]) 
        list.insert(4,data["chol"]) 
        list.insert(5,data["fbs"]) 
        list.insert(6,data["restecg"]) 
        list.insert(7,data["thalach"]) 
        list.insert(8,data["exang"]) 
        list.insert(9,data["oldpeak"]) 
        list.insert(10,data["slope"])    

    m = len(dicti["data"])
    n = len(data) - 1

    arr = np.array(list) 
    arr2 = arr.reshape(m,n)
    model = joblib.load("randomForest_joblib.pkl")


    def predict(value):
        
        pre = value.reshape(1,-1)
        res = model.predict(pre)
        #print(pre)
        print(res)
        

    print(arr2)
    print("ini spasi")

    for i in range(m):
        predict(arr2[i])
        i=i+1

if __name__=='__main__':
    app.run(debug=True)
