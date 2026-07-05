# Core
from fastapi import (
    FastAPI, 
    Request,
    Response,
    Header, 
    HTTPException,
    )
# Schema
from pydantic import BaseModel
from typing import Annotated
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
app = FastAPI()

# Middleware
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("app_logger")
async def basic_middleware(request: Request, call_next):
    # Log before
    logger.info(f"Request started:")
    # Execute
    response: Response = await call_next(request)
    # Log After
    logger.info(f"Request End:")
    return response
app.middleware("http")(basic_middleware)

# Endpoints
@app.get("/health")
async def health(request: Request) -> str:
    return "Hello, world"

@app.post("/post")
async def post(
               request: Request, 
               body : Func1Body,
               headers : Annotated[Func1Header, Header()]
               ) -> Func1Response:
    try :
        return Func1Response(original= body, new_age= body.age + 1)
    except Exception as e :
        raise HTTPException(
                            status_code= 500, 
                            detail= 'ERROR',
                            headers= {},
                            )

# Start
# uvicorn app_fastapi:app