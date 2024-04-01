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
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):

    Soil_color : int
    Nitrogen : int
    Phosphorus : int
    Potassium : int
    pH : int
    Rainfall : int
    Temperature : int
    Crop : int

fertilizer_model = pickle.load(open('crop_ferti.sav','rb'))
# @app.get('/')
# async def scoring_endpoint():
#     return {"hello":"world"}

@app.post('/predict')
async def predict_fertilizer(data:model_input):
    # data = data.dict()

    input_data = data.model_dump_json()
    input_dictionary = json.loads(input_data)


    Soil_color = input_dictionary['Soil_color']
    Nitrogen = input_dictionary['Nitrogen']
    Phosphorus = input_dictionary['Phosphorus']
    Potassium = input_dictionary['Potassium']
    pH = input_dictionary['pH']
    Rainfall = input_dictionary['Rainfall']
    Temperature = input_dictionary['Temperature']
    Crop = input_dictionary['Crop']

    Prediction = fertilizer_model.predict([[Soil_color,Nitrogen,Phosphorus,Potassium,pH,Rainfall,Temperature,Crop]])
    return{
        'Fertilizer_prediction' : Prediction
    }
