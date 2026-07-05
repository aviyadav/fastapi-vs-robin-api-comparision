# Core
from robyn import Robyn, Request, jsonify
# Schema
from robyn import Response
# Log
import logging

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
## Log after
@app.after_request()
def hello_after_request(response: Response):
    logger.info(f"Request End:")
    return response

# Endpoints

@app.post("/post")
async def post(request: Request):
    return jsonify('')
        
# Start
app.start(port=8001)