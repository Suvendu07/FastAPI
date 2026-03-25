"""Field validator work on two mode
one is after mode and another is before mode.

field validator ka kam ye hi ek single field ke upper data validator karne ka."""
from pydantic import BaseModel, Field, AnyUrl, EmailStr, field_validator
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    name : str
    email : EmailStr
    age : int
    weight : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]
    
    """field validator :-
    let take a examples 
    suppose you want to accept only email of hdfc and icici bank. except this eamil 
    it will be error. so to solve this type of problem use field validaot."""
    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        
        valid_domains = ['hdfc.com','icici.com']
        
        domain_name = value.split('@')[-1]
        
        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value
    
    
    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    

def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('insert')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('update')


patient_info = {'name':'suvendu','age':20, 'email':'abcd@icici.com', 'weight' : 75.2, 'linkdin':'http://linkdin.com/suvendukhuntia','married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'12345'}}

patient_1 = patient(**patient_info)

insert_patient(patient_1)
update_patient(patient_1)