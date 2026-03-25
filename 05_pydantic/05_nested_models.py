"""Agar app pydantic me ek model ko dusre model ke andar me as a field use karte ho usko bolte he nested_models."""


from pydantic import BaseModel


class Adress(BaseModel):
    
    city : str
    state : str
    pin : str


class patient(BaseModel):
    
    name : str
    gender : str
    age : int
    address : Adress
    
address_dict = {'city':'jajpur','state':'odisha','pin':'12345'}

address1 = Adress(**address_dict)

patient_dict = {'name':'suvendu','gender':'male','age':20, 'address':address1}

patient1 = patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)