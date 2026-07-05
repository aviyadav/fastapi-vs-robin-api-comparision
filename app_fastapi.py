## File name : app_fastapi.py
# Core

from fastapi import FastAPI, Request

# Create the App

app = FastAPI()

# Endpoints

@app.get('/health')
async def health(request: Request) -> str:
    return "Hello, World"

@app.post("/post")
async def post(request: Request) -> str:
    return "Hello, world"
