"""model_validator is use for ek sath multiple field ko combine 
karke data validation kar sakte ho.while it is not possible in field validator."""

from pydantic import BaseModel, Field, EmailStr, model_validator
from typing import List, Dict

class patient(BaseModel):

    """To understand model_validator let take a examples :-
    if the age is > 60 then in the contact details contains must having a emergency number(it means that the name dependent upon the contact_details)."""
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]
    
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls, model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model
    
# def insert_patient(patient: patient):
#     print(patient.name)
#     print(patient.age)
#     print('insert')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('update')


patient_info = {'name':'suvendu','age':90, 'email':'abcd@icici.com', 'weight' : 75.2, 'linkdin':'http://linkdin.com/suvendukhuntia','married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'12345','emergency':'12345'}}

"""if the patient age > 60 and it not contain a emergency number it show error, if there is emergency contact number it run."""

patient_1 = patient(**patient_info)

# insert_patient(patient_1)
update_patient(patient_1)