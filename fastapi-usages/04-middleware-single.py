# Core
from fastapi import FastAPI, Request
# Schema
from fastapi import Request, Response
# Log
import logging

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
@app.post("/post")
async def post(request: Request, ) :
    return ''

# Start
# uvicorn app_fastapi:app