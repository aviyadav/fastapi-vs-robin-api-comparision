# Core
from robyn import Robyn, Request, jsonify
# Schema
from pydantic import BaseModel

# Body
class Func1Body(BaseModel):
    username: str= 'a'
    age: int= 1
    
class Func1Response(BaseModel):
    original: Func1Body
    new_age: int= 11

# Create App
app = Robyn(__file__)

# Endpoints
@app.post("/post")
async def post(request: Request, body : Func1Body) -> Func1Response:
    return Func1Response(original= body, new_age= body.age +1)

# Start
app.start(port=8001)