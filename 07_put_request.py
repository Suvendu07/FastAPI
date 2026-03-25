from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, computed_field
from fastapi.responses import JSONResponse
from typing import Optional, Annotated, Literal
import json


def load_data():
    with open("patients.json",'r') as f:
        data = json.load(f)
    
    return data

def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data, f)
        
        
        
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


class PatientUpdate(BaseModel):
    
    name : Annotated[Optional[str], Field(default=None)]
    city : Annotated[Optional[str], Field(default=None)]
    age : Annotated[Optional[int], Field(default=None)]
    gender : Annotated[Optional[Literal['male','female']], Field(default=None)]
    height : Annotated[Optional[float], Field(default=None, gt=0)]
    weight : Annotated[Optional[float], Field(default=None, gt=0)]
    
    
    
app = FastAPI()


@app.put("/edit/{patient_id}")

def update_patient(patient_id : str, patient_update : PatientUpdate):
    
    data = load_data()
    
    if patient_id not in data:
        return HTTPException(status_code = 404, detail = 'patient not found')
    
    existing_patient_info = data[patient_id]
    
    updated_patient_info = patient_update.model_dump(exclude_unset=True)
    
    for key, value in updated_patient_info.items():
        existing_patient_info[key] = value
        
        
    """ existing_patient_info -> pydantic object -> updated bmi + verdict"""
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = patients(**existing_patient_info)
    
    
    """ -> pydantic object -> dict """
    existing_patient_info = patient_pydantic_obj.model_dump(exclude='id')
    
    
    # Add this dict to data
    data[patient_id] = existing_patient_info
    
    
    # save data
    save_data(data)
    
    return JSONResponse(status_code = 200,content = {'message':'patient updated'})


@app.delete("/delete/{patient_id}")

def delete_patient(patient_id : str):
    
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code = 404, detail = "patient not found")
    
    del data[patient_id]
    
    save_data(data)
    
    return JSONResponse(status_code = 200, content = {'message':'patient deleted'})