"""__________PART1 & PART-2(OVERVIEW)__________"""

# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def hello():
#     return {"message": "Hello, World!"}

# @app.get("/about")
# def about():
#     return {"message": "This is a simple FastAPI application."}

# @app.get("/contact")
# def contact():
#     return {"message": "You can contact us at contact@example.com"}









"""__________PART-3(HTTP METHODS, GET METHOD)__________"""

# from fastapi import FastAPI               
# import json

# app = FastAPI()

# def load_data():
#     with open('patients.json', 'r') as f:
#         data = json.load(f)
#     return data

# @app.get("/")
# def hello():
#     return {"message": "Patient Management System API "}

# @app.get("/about")
# def about():
#     return {"message": "Fully functional API to manage patient records"}

# @app.get("/view")
# def view():
#     data = load_data()
#     return data










"""__________PART-4(PATH, QUERY PARAMETERS, STATUS CODES OF ERROR)__________"""

# from fastapi import FastAPI, Path, HTTPException, Query                # Path is used to validate the path parameters, HTTPException is used to raise HTTP errors, Query is used to validate the query parameters
# import json

# app = FastAPI()

# def load_data():
#     with open('patients.json', 'r') as f:
#         data = json.load(f)
#     return data

# @app.get("/")
# def hello():
#     return {"message": "Patient Management System API "}

# @app.get("/about")
# def about():
#     return {"message": "Fully functional API to manage patient records"}

# @app.get("/view")
# def view():
#     data = load_data()
#     return data

# @app.get('/patient/{patient_id}')
# def view_patient(patient_id: str = Path(..., description="The ID of the patient in the DB", example="P001")):       # ... means required path parameter
#     data = load_data()
#     if patient_id in data: 
#         return data[patient_id]
#     raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

# @app.get('/sort')
# def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi", example="age"),
#                   order: str = Query('asc', description="Sort in ascending or descending order", example="asc")):       # ... means required query parameter, asc is default value for order parameter 
#     valid_fields = ['height', 'weight', 'bmi']
#     if sort_by not in valid_fields:
#         raise HTTPException(status_code=400, detail=f"Invalid fields select from {valid_fields}")

#     if order not in ['asc', 'desc']:
#         raise HTTPException(status_code=400, detail="Invalid order select from ['asc', 'desc']")

#     data = load_data()

#     sort_order = True if order == 'desc' else False

#     sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

#     return sorted_data










"""__________PYDANTIC__________"""

#  Pydantic is used for data validation and type validation insteed of manual validation. 

"""_____________________PART-1(BaseModel)_____________________"""

# from pydantic import BaseModel


# class Patient(BaseModel): 
#     name: str
#     age: int

# def insert_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.age)
#     print("Inserted Successfully ✅")

# def update_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.age)
#     print("Updated Successfully ✅")

# patient_info = {'name': 'John Doe', 'age': 30}
# patient1 = Patient(**patient_info)

# insert_patient_data(patient1)
# update_patient_data(patient1)





"""_____________________PART-2(Type Validation, Optional Fields, Default Values, Typing module)_____________________"""

# from pydantic import BaseModel
# from typing import List, Dict, Optional

# class Patient(BaseModel): 
#     name: str
#     age: int
#     weight: float
#     married: bool = False
#     allergies: Optional[List[str]] = None
#     contact_details: Dict[str, str]

# def update_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies)
#     print("Updated Successfully ✅")

# patient_info = {'name': 'John Doe', 'age': 30, 'weight': 70.5, 'contact_details': {'email': 'john.doe@example.com', 'phone': '123-456-7890'}}
# patient1 = Patient(**patient_info)

# update_patient_data(patient1)





"""_____________________PART-3(Data Validation1)_____________________"""

"""
- EmailStr, AnyUrl, Field, Annotated
- Here Field method is used to add data validation
- We use annotaed to add metadata to the fields of the model. for this we use Fileds inside Annotated. We can also use EmailStr and AnyUrl to validate email and url respectively.
- We define both data validation and type validation using Annotated
"""

# from pydantic import BaseModel, EmailStr, AnyUrl, Field
# from typing import List, Dict, Optional, Annotated

# class Patient(BaseModel): 
#     name: Annotated[str, Field(max_length=50, title="Patient Name", description="The name of the patient", examples = ["John Doe"])]   # Here Annotated is used to add metadata to the field, Field is used to add validation constraints
#     email: EmailStr            # Here EmailStr is used to validate the email address format
#     linkedin_url: AnyUrl         # Here AnyUrl is used to validate the URL format
#     age: int = Field(gt=0, le=120)  # Here Field is used to add validation constraints
#     weight: Annotated[float, Field(gt=0, strict=True)]  # Here strict=True is used to ensure that the value is a float and not any thing else 
#     married: Annotated[bool, Field(default=None, description="Marital status of the patient")]  
#     allergies: Optional[List[str]] = Field(default=None, max_length=5)  # Here Field is used to add validation constraints
#     contact_details: Dict[str, str]

# def update_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.email)
#     print(patient.linkedin_url)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies)
#     print("Updated Successfully ✅")

# patient_info = {'name': 'John Doe', 'email': 'abc@gmail.com', 'linkedin_url': 'https://www.linkedin.com/12566', 'age': 30, 'weight': 70.5,'contact_details': {'phone': '123-456-7890'}}
# patient1 = Patient(**patient_info)

# update_patient_data(patient1)





"""_____________________PART-4(Data Validation2)_____________________"""
"""
- field_validator 
- field_validator is decorator is used for custom validation and transformation on the fields. 
- There are two modes for field_validator, before and after. By default mode is after. The before mode is used to validate the data before the type_validation and after mode is used to validate the data after the type_validation.
"""

from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): 
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]

    @field_validator('email')    # validate email for specific domains
    @classmethod
    def email_validator(cls, value):
         valid_domains = ['hdfc.com', 'icici.com']
         domain_name = value.split('@')[-1]
         if domain_name not in valid_domains:
             raise ValueError(f"Invalid email domain. Allowed domains are: {valid_domains}")
         return value 

    @field_validator('name')      # transform name to uppercase
    @classmethod
    def name_validator(cls, value): 
        return value.upper() 

    @field_validator('age', mode='after')      # default mode is after 
    @classmethod
    def age_validator(cls, value): 
        if 0<value< 100:
            return value
        raise ValueError("Age must be between 0 and 100")

       
    
def update_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Updated Successfully ✅")

patient_info = {'name': 'John Doe', 'email': 'abc@hdfc.com', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890'}}
patient1 = Patient(**patient_info)

update_patient_data(patient1)






"""_____________________PART-5(Data Validation3)_____________________"""
"""
- model_validator 
- model_validator is decorator is used for custom validation and transformation on multiple fields.
"""

from pydantic import BaseModel, EmailStr, AnyUrl, Field, model_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): 
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]
    

       
    
def update_patient_data(patient: Patient): 
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Updated Successfully ✅")

patient_info = {'name': 'John Doe', 'email': 'abc@hdfc.com', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890'}}
patient1 = Patient(**patient_info)

update_patient_data(patient1)
