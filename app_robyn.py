## File name : app_robyn.py
# Core

from robyn import Robyn, Request, jsonify

# Create App

app = Robyn(__file__)

# Endpoints

@app.get("/health")
async def health(request: Request) -> str:
    return jsonify("Hello, World - from Robyn")

@app.post("/post")
async def post(request: Request) -> str:
    return jsonify("Hello, world from robyn")

# Start
app.start(port=8090)