import json
import numpy as np
import joblib
import requests

r = requests.get("https://belajarflaskkrestapi.herokuapp.com/")
s = r.headers['Content-Type']
t = r.text


dicti = json.loads(t)
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
    return str(res)
        

    #print(arr2)
    #print("ini spasi")

for i in range(m):
    predict(arr2[i])
    i=i+1
