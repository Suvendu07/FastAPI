"""It is use for to export pydantic to json, dict"""

from pydantic import BaseModel

class Address(BaseModel):
    city : str
    state : str
    pin : str
    
class Patient(BaseModel):
    
    name : str
    gender : str
    age : int
    address : Address
    
address_dict = {'city':'jajpur','state':'odisha','pin':'12345'}

address1 = Address(**address_dict)

patient_dict = {'name':'suvendu','gender':'male','age':20, 'address':address1}

patient1 = Patient(**patient_dict)


temp = patient1.model_dump()
print(temp)
print(type(temp))

temp1 = patient1.model_dump_json()
print(temp1)
print(type(temp1))