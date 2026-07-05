# Core
from robyn import (
    Robyn, 
    Request, 
    Response,
    jsonify,
    )
# Schema
from pydantic import BaseModel
# Log
import logging

# BODY
## Reqest
class Func1Body(BaseModel):
    username: str= 'a'
    age: int= 1
## Response
class Func1Response(BaseModel):
    original: Func1Body
    new_age: int= 11
# Header
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

# Middleware
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app_logger")
## Log before
@app.before_request()
async def hello_before_request(request: Request):
    logger.info(f"Request started:")
    return request
## Log After
@app.after_request()
def hello_after_request(response: Response):
    logger.info(f"Request End:")
    return response

# Endpoints
@app.get("/health")
async def health(request: Request) -> str:
    return jsonify("Hello, world")

@app.post("/post")
async def post(
               request: Request, 
               body : Func1Body,
               ) -> Func1Response:
    try :
        headers = Func1Header(**request.headers)
        return Func1Response(original= body, new_age= body.age +1)
    except Exception as e :
        return  Response(
                        status_code= 500,
                        description= jsonify({"detail": "Error"}),
                        headers= {},
                        )
        
# Start
app.start(port=8001)