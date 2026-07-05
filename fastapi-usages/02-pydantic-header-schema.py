# Core
from fastapi import FastAPI, Request
# Schema
from pydantic import BaseModel
# Header
from fastapi import Header
from typing import Annotated

# Headers
## Common
class CommonHeader(BaseModel):
    x_user_name: str= 'a'
    x_user_age: int= 1

## Specific    
class SpecificFunc1Header(BaseModel):
    x_user_age: int= 2
    x_user_number: int= 3

## Combine  
class Func1Header(CommonHeader, SpecificFunc1Header):
    pass

# Create App
app = FastAPI()

# Endpoints
@app.post("/post")
async def post(request: Request, 
               headers : Annotated[Func1Header, Header()]) :
    return ''

# Start
# uvicorn app_fastapi:app