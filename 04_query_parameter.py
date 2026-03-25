"""it uses for to what if a user want to see the data in a sorted order(assending/descending). it may be 
height ke assending order me , weight ke assencing order me or bmi ke asccending order me like this.
if the user not enter the order we must show as a default order."""



from fastapi import FastAPI, Path, HTTPException, Query
import json


app = FastAPI()


def load_data():
    with open('patients.json','r') as f:
        data = json.load(f)
        
    return data



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
    
    