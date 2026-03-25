def insert_data(name, age):
    print(name)
    print(age)
    print("insert")
insert_data('suvendu','twenty')
"""In this above function the age should be int. But if a user
pass the age as a string it run.we can't data validation here. we must be need the age as a int."""




# solve this use TYPEHINT
def insert_data(name:str, age:int):
    print(name)
    print(age)
    print("insert")
insert_data("suvendu",20)
# insert_data("suvendu","twenty")
"""now it will be run, but after the typehints if a user pass
the age as a string it will be also run without causing any error.

bcz of python typehint are not strong."""




def insert_data(name:str, age:int):
     if type(name) == str and type(age) == int:
         print(name)
         print(age)
         print("insert")
     else:
        raise TypeError("Incorrect data type")
insert_data("suvendu",20)

def update_data(name:str, age:int):
     if type(name) == str and type(age) == int:
         print(name)
         print(age)
         print("update")
     else:
        raise TypeError("Incorrect data type")
update_data("suvendu",20)
"""now it will be work as correctly, if you pass wrong data type
it show erro.But this way is not good/scalable. bcz of if there are more than
one function just like above update_data() you write the same logic multiple time 
in each function."""




def insert_data(name:str, age:int):

    if type(name) == str and type(age) == int:
        """if a user want to data validation like he want the age should in between 10 to 20
    he must be write the logic in each function each time."""
        if age < 0:
            raise ValueError("age can't be -ve")
        else:
            print(name)
            print(age)
            print("insert")
    else:
        raise TypeError("Incorrect data type")
insert_data("suvendu",20)




"""So python not support typevalidation. you can do it manually.
so to solve this type of problem use 'Pydantic' for data validation/type validation."""





# PYDANTIC
"""Typevalidation"""

from pydantic import BaseModel

class patient(BaseModel):
    
    name : str 
    age : int
    
def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('insert')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('update')


patient_info = {'name':'suvendu','age':20}

patient_1 = patient(**patient_info)

update_data(patient_1)
insert_data(patient_1)
"""Now app kitne v function bana lo bas ek hi bar declare karna padega whithou
write each time the typevalidation."""




from pydantic import BaseModel
from typing import List, Dict, Optional

class patient(BaseModel):
    
    name : str 
    age : int
    weight : float
    married : bool
    """Add option field bcz if use forget to pass this it show error. so if we add optional it will be run even if you forget pass this."""
    allergies : Optional[List[str]] = None
    """Use List insted of using list bcz List use for 2 lavel validation like we must be declare the inside the allergies all are must be string insted of declare it is a hole string."""
    contact_details : Dict[str, str]
    
def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('insert')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('update')


patient_info = {'name':'suvendu','age':20, 'weight' : 75.2, 'married':True, 'allergies':['pollen','dust'], 'contact_details':{'email':'abcd@gmail.com','phone':'12345'}}

patient_1 = patient(**patient_info)

update_data(patient_1)
insert_data(patient_1)




# DATA VALIDATION
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class patient(BaseModel):
    
    name : Annotated[str, Field(description="abcd", max_digits=5)]
    """Field is also use for add meta data but it work with the combination of annoted and field."""
    email : EmailStr
    age : int = Field(gt = 0, le = 100)
    """for add more data validation use 'Field'. """
    linkdin : AnyUrl
    weight : float = Field(gt = 0, lt = 50)
    married : bool
    allergies : Optional[List[str]] = None
    contact_details : Dict[str, str]
    
def insert_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('insert')

def update_patient(patient: patient):
    print(patient.name)
    print(patient.age)
    print('update')


patient_info = {'name':'suvendu','age':20, 'email':'abcd@gmail.com', 'weight' : 75.2, 'linkdin':'http://linkdin.com/suvendukhuntia','married':True, 'allergies':['pollen','dust'], 'contact_details':{'phone':'12345'}}

patient_1 = patient(**patient_info)

update_data(patient_1)
insert_data(patient_1)