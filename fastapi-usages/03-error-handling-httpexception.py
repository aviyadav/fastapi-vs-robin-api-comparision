# Core
from fastapi import FastAPI, Request
# Error Handler
from fastapi import HTTPException

# Create App
app = FastAPI()

# Endpoints
@app.get("/health")
async def health(request: Request) -> str:
    return "Hello, world"

@app.post("/post")
async def post(request: Request):
    try :
        return ''
    except Exception as e :
        raise HTTPException(
                            status_code= 500, 
                            detail= 'ERROR',
                            headers= {},
                            )

# Start
# uvicorn app_fastapi:app