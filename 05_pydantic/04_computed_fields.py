"""It is use for to crete dynamic value with the help of combining two fields value.

let take a examples to understand this :- 
we assigned a new filed called BMI, but the bmi value can't defined by user,it will be cal. dynamically with the help of combining two field like weight and height."""

from pydantic import BaseModel, Field, EmailStr, computed_field
from typing import List, Dict

class patient(BaseModel):
    name : str
    age : int
    email : EmailStr
    weight : float
    height : float
    married : bool
    allergies : List[str]
    contact_details : Dict[str, str]
    
    
    @computed_field
    @property
    def calculate_bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi



def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print("BMI:", patient.calculate_bmi)
    print('update')


patient_info = {'name':'suvendu','age':90, 'email':'abcd@icici.com', 'weight' : 75.2, 'height': 1.72, 'linkdin':'http://linkdin.com/suvendukhuntia','married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'12345','emergency':'12345'}}

"""if the patient age > 60 and it not contain a emergency number it show error, if there is emergency contact number it run."""

patient_1 = patient(**patient_info)

update_patient(patient_1)