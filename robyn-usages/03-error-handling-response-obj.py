# Core
from robyn import Robyn, Request, jsonify
# Error Handler
from robyn import Response

# Create App
app = Robyn(__file__)

# Endpoints
@app.post("/post")
async def post(request: Request) :
    try :
        return jsonify('')
    except Exception as e :
        return  Response(
                        status_code= 500,
                        description= jsonify({"detail": "Error"}),
                        headers= {},
                        )
        
# Start
app.start(port=8001)