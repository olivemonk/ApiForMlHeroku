from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle 
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"].index,
    allow_headers=["*"],
    )


class modelInput(BaseModel):

    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

#loading the save model
diabetes_model = pickle(open("diabetes_model.sav",'rb'))

@app.post('/diabetes_predictions')
def diabetes_pred(input : modelInput):
    input_data = input.json
    input_dict = json.load(input_data)

    preg = input_dict['Pregnancies']
    glu = input_dict['Glucose']
    bp = input_dict['BloodPRessure']
    st = input_dict['SkinThickness']
    ins = input_dict['Insulin']
    bmi = input_dict['BMI']
    dfg = input_dict['DiabetesPedigreeFunction']
    age = input_dict['Age']

    input_list = [preg,glu,bp,st,ins,bmi,dfg,age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0]==0:
        return "The person is not Diabetic"
    else:
        return "Preson is Daibetic"