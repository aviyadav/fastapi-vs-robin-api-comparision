# Core
from robyn import Robyn, Request, jsonify
# Schema
from pydantic import BaseModel

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
app = Robyn(__file__)

# Endpoints
@app.post("/post")
async def post(request: Request):
    headers = Func1Header(**request.headers)
    return ''

# Start
app.start(port=8001)