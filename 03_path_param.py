from fastapi import FastAPI, Path, HTTPException
import json


app = FastAPI()


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        
    return data
        
        
@app.get("/")
def hello():
    return {"message":"patient management system API"}


@app.get("/about")
def about():
    return {"message":"A fully funcational API to manage your patient records"}        



@app.get('/view')
def view():
    data = load_data()
    
    return data





# Path Params
"""the path() function  is FASTAPI is used to provide metadata, data validation rulws, hints for path paramaeters in your API endpoints."""

# @app.get("/patient/{patient_id}")
# def view_patient(patient_id: str = Path(..., description = "ID of the patient in the DB", example = 'P001')):
#     data = load_data()
    
#     if patient_id in data:
#         return data[patient_id]
    
#     return {'error':'patient not found'}




# HTTPException
"""in this above code there was a error that if a user enter a patient but that 
does't exit in the database it return patieny not found but the status code return 200. 
but if a data is not found the status must be  return 404. sp to solve this type of error use a 
method called HTTPException."""


@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "ID of the patient in the DB", examples = 'P001')):
    data = load_data()
    
    if patient_id in data:
        return data[patient_id]
    
    raise HTTPException(status_code = 404, detail = 'patient not found')