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

# from pydantic import BaseModel, EmailStr, field_validator
# from typing import List, Dict

# class Patient(BaseModel): 
#     name: str
#     email: EmailStr
#     age: int
#     weight: float
#     married: bool
#     allergies: List[str]
#     contact_details: Dict[str, str]

#     @field_validator('email')    # validate email for specific domains
#     @classmethod
#     def email_validator(cls, value):
#          valid_domains = ['hdfc.com', 'icici.com']
#          domain_name = value.split('@')[-1]
#          if domain_name not in valid_domains:
#              raise ValueError(f"Invalid email domain. Allowed domains are: {valid_domains}")
#          return value 

#     @field_validator('name')      # transform name to uppercase
#     @classmethod
#     def name_validator(cls, value): 
#         return value.upper() 

#     @field_validator('age', mode='after')      # default mode is after 
#     @classmethod
#     def age_validator(cls, value): 
#         if 0<value< 100:
#             return value
#         raise ValueError("Age must be between 0 and 100")

       
    
# def update_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.email)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies)
#     print("Updated Successfully ✅")

# patient_info = {'name': 'John Doe', 'email': 'abc@hdfc.com', 'age': '30', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890'}}
# patient1 = Patient(**patient_info)

# update_patient_data(patient1)






"""_____________________PART-5(Data Validation3)_____________________"""
"""
- model_validator 
- model_validator is decorator is used for custom validation and transformation on multiple fields.
"""

# from pydantic import BaseModel, EmailStr, model_validator
# from typing import List, Dict

# class Patient(BaseModel): 
#     name: str
#     email: EmailStr
#     age: int
#     weight: float
#     married: bool
#     allergies: List[str]
#     contact_details: Dict[str, str]
    
#     @model_validator(mode='after')      # default mode is after
#     @classmethod
#     def validate_emergency_contact(cls, model): 
#          if model.age > 60 and 'emergency' not in model.contact_details: 
#              raise ValueError("Emergency contact is required for patients above 60 years old")
#          return model
       
    
# def update_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.email)
#     print(patient.age)
#     print(patient.married)
#     print(patient.allergies)
#     print("Updated Successfully ✅")

# patient_info = {'name': 'John Doe', 'email': 'abc@hdfc.com', 'age': '70', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'emergency': '987-654-3210'}}
# patient1 = Patient(**patient_info)

# update_patient_data(patient1)





"""_____________________PART-6(Data Validation4)_____________________"""
"""
- computed_field
- computed_field is decorator is used to create a computed field in the model. A computed field is a field that is not stored in the database but is computed from other fields in the model.
"""

# from pydantic import BaseModel, EmailStr, computed_field
# from typing import List, Dict

# class Patient(BaseModel): 
#     name: str
#     email: EmailStr
#     age: int
#     weight: float #kg
#     height: float #mtr
#     married: bool
#     allergies: List[str]
#     contact_details: Dict[str, str]

#     @computed_field
#     @property
#     def bmi(self) -> float: 
#         bmi = round(self.weight/self.height**2, 2)
#         return bmi 
    
       
    
# def update_patient_data(patient: Patient): 
#     print(patient.name)
#     print(patient.email)
#     print(patient.age)
#     print(patient.married)
#     print('BMI:', patient.bmi)
#     print(patient.allergies)
#     print("Updated Successfully ✅")

# patient_info = {'name': 'John Doe', 'email': 'abc@hdfc.com', 'age': '70', 'weight': 70.5, 'height': 1.75, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'emergency': '987-654-3210'}}
# patient1 = Patient(**patient_info)

# update_patient_data(patient1)






"""_____________________PART-7(Data Validation5)_____________________"""
"""
- nested_model
- nested_model is decorator is used to create a nested model in the model. A nested model is a model that is used as a field in another model.
- here they improve the readability, reusability, nested models are validate independently no extra work needed.
"""

# from pydantic import BaseModel 

# class Address(BaseModel):
#     city: str
#     state: str
#     pin: str

# class Patient(BaseModel): 
#     name: str
#     gender: str 
#     age: int 
#     address: Address  # Here Address is a nested model

# address_dict = {'city': 'New York', 'state': 'NY', 'pin': '10001'}
# address1 = Address(**address_dict)
# patient_dict = {'name': 'John Doe', 'gender': 'male', 'age': 30, 'address': address1}
# patient1 = Patient(**patient_dict)

# print(patient1)
# print(patient1.name)    
# print(patient1.address.city)





"""_____________________PART-8(Serialization)_____________________"""
"""
- Exporting pydantic model to python dictonaries or json .
- For this pydantic gives built in methods.
- Helpful in -> building api's using fast-api, debugging, login.
"""

# from pydantic import BaseModel 

# class Address(BaseModel):
#     city: str
#     state: str
#     pin: str

# class Patient(BaseModel): 
#     name: str
#     gender: str = 'male' 
#     age: int 
#     address: Address  # Here Address is a nested model

# address_dict = {'city': 'New York', 'state': 'NY', 'pin': '10001'}
# address1 = Address(**address_dict)
# patient_dict = {'name': 'John Doe', 'age': 30, 'address': address1}
# patient1 = Patient(**patient_dict)

# temp1 = patient1.model_dump()  # model_dump() method is used to convert the pydantic model to python dictonary
# temp1_1 = patient1.model_dump(include={'name', 'age'})  # model_dump() method is used to convert the pydantic model to python dictonary with only included fields
# temp1_2 = patient1.model_dump(exclude={'name', 'age'})  # model_dump() method is used to convert the pydantic model to python dictonary with excluded fields
# temp1_3 = patient1.model_dump(exclude={'address': {'state'}})  # model_dump() method is used to convert the pydantic model to python dictonary with only excluded fields in nested model
# temp1_4 = patient1.model_dump(exclude_unset=True)  # model_dump() method is used to convert the pydantic model to python dictonary with only fields that are set (not default values)
# temp2 = patient1.model_dump_json()  # model_dump_json() method is used to convert the pydantic model to json string


# print(temp1, type(temp1))  
# print(temp1_1, type(temp1_1))  
# print(temp1_2, type(temp1_2))  
# print(temp1_3, type(temp1_3))  
# print(temp1_4, type(temp1_4))  
# print(temp2, type(temp2))  









"""__________PART-5(POST request with Pydantic)__________"""

# from fastapi import FastAPI, Path, HTTPException, Query                # Path is used to validate the path parameters, HTTPException is used to raise HTTP errors, Query is used to validate the query parameters
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, Field, computed_field 
# from typing import Annotated, Literal                    # Here Literal is used to restrict the values of a field to a specific set of values
# import json

# app = FastAPI()

# class Patient(BaseModel):
#     id: Annotated[str, Field(..., description="ID of the patient", example="P001")]
#     name: Annotated[str, Field(..., description="Name of the patient")]
#     city: Annotated[str, Field(..., description="City of the patient where he/she lives")] 
#     age: Annotated[int, Field(..., description="Age of the patient", gt=0, le=120)]
#     gender: Annotated[Literal["male", "female", "others"], Field(..., description="Gender of the patient")]
#     height: Annotated[float, Field(..., description="Height of the patient in meters", gt=0)] 
#     weight: Annotated[float, Field(..., description="Weight of the patient in kilograms", gt=0)]

#     @computed_field
#     @property
#     def bmi(self) -> float:
#         bmi = round(self.weight / self.height ** 2, 2)
#         return bmi  

#     @computed_field
#     @property
#     def verdict(self) -> str:
#         if self.bmi < 18.5:
#             return "Underweight"
#         elif 18.5 <= self.bmi < 25:
#             return "Normal weight"
#         elif 25 <= self.bmi < 30:
#             return "Overweight"
#         else:
#             return "Obesity"

# def load_data():
#     with open('patients.json', 'r') as f:
#         data = json.load(f)
#     return data

# def save_data(data):
#     with open('patients.json', 'w') as f:
#         json.dump(data, f, indent=4)

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

# @app.post('/create') 
# def create_patient(patient: Patient):
#     # load existing data
#     data = load_data()

#     # check if patient ID already exists
#     if patient.id in data:
#         raise HTTPException(status_code=400, detail=f"Patient with ID {patient.id} already exists")

#     # new patient add to the database
#     data[patient.id] = patient.model_dump(exclude={'id'})

#     # save the python dictonary to json file
#     save_data(data)

#     return JSONResponse(status_code=201, content={"message": f"Patient with ID {patient.id} created successfully", "patient": patient.model_dump()}) 










"""__________PART-6(PUT and DELETE request with Pydantic)__________"""

# from fastapi import FastAPI, Path, HTTPException, Query                # Path is used to validate the path parameters, HTTPException is used to raise HTTP errors, Query is used to validate the query parameters
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, Field, computed_field 
# from typing import Annotated, Literal, Optional                    # Here Literal is used to restrict the values of a field to a specific set of values
# import json

# app = FastAPI()

# class Patient(BaseModel):
#     id: Annotated[str, Field(..., description="ID of the patient", example="P001")]
#     name: Annotated[str, Field(..., description="Name of the patient")]
#     city: Annotated[str, Field(..., description="City of the patient where he/she lives")] 
#     age: Annotated[int, Field(..., description="Age of the patient", gt=0, le=120)]
#     gender: Annotated[Literal["male", "female", "others"], Field(..., description="Gender of the patient")]
#     height: Annotated[float, Field(..., description="Height of the patient in meters", gt=0)] 
#     weight: Annotated[float, Field(..., description="Weight of the patient in kilograms", gt=0)]

#     @computed_field
#     @property
#     def bmi(self) -> float:
#         bmi = round(self.weight / self.height ** 2, 2)
#         return bmi  

#     @computed_field
#     @property
#     def verdict(self) -> str:
#         if self.bmi < 18.5:
#             return "Underweight"
#         elif 18.5 <= self.bmi < 25:
#             return "Normal weight"
#         elif 25 <= self.bmi < 30:
#             return "Overweight"
#         else:
#             return "Obesity"

# class PatientUpdate(BaseModel):
#     name: Annotated[Optional[str], Field(default=None)]
#     city: Annotated[Optional[str], Field(default=None)]
#     age: Annotated[Optional[int], Field(default=None, gt=0, le=120)]
#     gender: Annotated[
#         Optional[Literal["male", "female", "others"]],
#         Field(default=None)
#     ]
#     height: Annotated[Optional[float], Field(default=None, gt=0)]
#     weight: Annotated[Optional[float], Field(default=None, gt=0)]

# def load_data():
#     with open('patients.json', 'r') as f:
#         data = json.load(f)
#     return data

# def save_data(data):
#     with open('patients.json', 'w') as f:
#         json.dump(data, f, indent=4)

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

# @app.post('/create') 
# def create_patient(patient: Patient):
#     # load existing data
#     data = load_data()

#     # check if patient ID already exists
#     if patient.id in data:
#         raise HTTPException(status_code=400, detail=f"Patient with ID {patient.id} already exists")

#     # new patient add to the database
#     data[patient.id] = patient.model_dump(exclude={'id'})

#     # save the python dictonary to json file
#     save_data(data)

#     return JSONResponse(status_code=201, content={"message": f"Patient with ID {patient.id} created successfully", "patient": patient.model_dump()}) 

# @app.put('/edit/{patient_id}')
# def edit_patient(patient_id: str, patient_update: PatientUpdate): 
#     data = load_data()

#     if patient_id not in data:
#         raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

#     existing_patient_info = data[patient_id]

#     updated_patient_info =  patient_update.model_dump(exclude_unset=True)

#     for key, value in updated_patient_info.items():
#         existing_patient_info[key] = value

#     # existing_patient_info  -> pydantic object -> updated bmi + verdict
#     existing_patient_info['id'] = patient_id  # Add the patient ID to the existing patient info
#     patient_pydantic_obj = Patient(**existing_patient_info)

#     # pydantic object -> python dictonary
#     existing_patient_info = patient_pydantic_obj.model_dump()

#     # add this dictionary to data
#     data[patient_id] = existing_patient_info

#     # save the updated data to the JSON file
#     save_data(data)

#     return JSONResponse(status_code=200, content={"message": f"Patient with ID {patient_id} updated successfully", "patient": patient_pydantic_obj.model_dump()})

# @app.delete('/delete/{patient_id}')
# def delete_patient(patient_id: str):
#     #load_data 
#     data = load_data()

#     if patient_id not in data:
#         raise HTTPException(status_code=404, detail=f"Patient with ID {patient_id} not found")

#     del data[patient_id]

#     save_data(data)

#     return JSONResponse(status_code=200, content={"message": f"Patient with ID {patient_id} deleted successfully"}) 