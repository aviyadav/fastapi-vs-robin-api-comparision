import requests

# GET
print('FASTAPI : ',requests.get('http://localhost:8000/health').content)
print('ROBYN : ',requests.get('http://localhost:8090/health').content)

# POST
print('FASTAPI : ',requests.post('http://localhost:8000/post').content)
print('ROBYN : ',requests.post('http://localhost:8090/post').content)