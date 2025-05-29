from fastapi import FastAPI
from pydantic import BaseModel

# Here we have simple class showing our input information type and also what are them. 
class Todo(BaseModel):
    id: int 
    item: str 
