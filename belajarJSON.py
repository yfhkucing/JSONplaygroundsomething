import json
import numpy as np
import joblib

iniString2 = '''{
    "code": 200,
    "msg": "query sukses",
    "data": [
        {
            "id": 1,
            "age": 20.0,
            "sex": 0.0,
            "cp": 1.0,
            "trestbps": 130.0,
            "chol": 200.0,
            "fbs": 0.0,
            "restecg": 0.0,
            "thalach": 172.0,
            "exang": 0.0,
            "oldpeak": 0.0,
            "slope": 1.0
        },
        {
            "id": 2,
            "age": 35.0,
            "sex": 0.0,
            "cp": 1.0,
            "trestbps": 130.0,
            "chol": 200.0,
            "fbs": 0.0,
            "restecg": 0.0,
            "thalach": 172.0,
            "exang": 0.0,
            "oldpeak": 0.0,
            "slope": 1.0
        },
        {
            "id": 3,
            "age": 40.0,
            "sex": 0.0,
            "cp": 1.0,
            "trestbps": 130.0,
            "chol": 200.0,
            "fbs": 0.0,
            "restecg": 0.0,
            "thalach": 172.0,
            "exang": 0.0,
            "oldpeak": 0.0,
            "slope": 1.0
        }
    ]
}'''

dicti = json.loads(iniString2)
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


def predict(value):
    model = joblib.load("randomForest_joblib.pkl")
    pre = value.reshape(1,-1)
    res = model.predict(pre)
    print(pre)
    print(res)
    

print(arr2)
print("ini spasi")

for i in range(m):
    predict(arr2[i])
    i=i+1

