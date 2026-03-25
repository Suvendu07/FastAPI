from fastapi import FastAPI, HTTPException, Query, Path
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal

app = FastAPI()


class patients(BaseModel):
    
    id : Annotated[str, Field(..., description="Id of the patient", examples=['P001'])]
    
    name : Annotated[str, Field(..., description="Name of the patient")]
    
    city : Annotated[str, Field(..., description="City where the patient is living")]
    
    age : Annotated[int, Field(..., description="Age of the patient")]
    
    gender : Annotated[Literal['male','female','other'], Field(..., description="Gender of the patient")]
    
    height : Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    
    weight : Annotated[float, Field(...,description="weight of the patient in kgs")]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height **2),2)
        return bmi
    
    
    @computed_field
    @property
    def verdict(self) -> str:
        
        if self.bmi < 18.5:
            return "Underweight"
        
        elif self.bmi < 25:
            return 'Normal'
        
        elif self.bmi < 30:
            return 'Noraml'
        
        else:
            return 'Obese'

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    
    return data


def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data, f)
        
        
        
        
@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "ID of the patient in the DB", examples = 'P001')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code = 404, detail = 'patient not found')




# Query() is a utility function provide by FASTPI to declare, validate and document query parameters in your API endpoint(its like the path() ).
@app.get("/sort")
def sort_patient(sort_by: str=Query(..., description = 'sort on the basis of height, weight, or bmi'),
                                    order : str = Query('asc', description='sort in desc or asce order')):
    
    valid_fields = ['height','weight','bmi']
    
    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400, detail = "invalid field select form {valid_fields}")
    
    if order not in ['asc','desc']:
        raise HTTPException(status_code = 400, detail = "Invalid order select between asc and desc")
    
    
    data = load_data()
    
    sort_order = True if order == 'desc' else False
    
    sorted_data = sorted(data.values(), key = lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    
    return sorted_data



@app.post('/create')
def create_patient(patient: patients):
    
    # load existing data
    data = load_data()
    
    # check if the patient already exists
    if patients.id in data:
        raise HTTPException(status_code = 400, detail = 'patient already exist')
    
    # new patient add to the database
    data['patient.id'] = patient.model_dump(exclude=['id'])
    
    
    # save into the json
    save_data(data)
    
    
    
    return JSONResponse(status_code = 201, content = {'message':'patient created successfuly'})