import requests
import json

try:
    print("Testing API...")
    url = "http://localhost:8000/analyze"
    payload = {"url": "https://github.com/fastapi/fastapi"}
    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, json=payload, headers=headers)
    
    print(f"Status Code: {response.status_code}")
    try:
        print("Response JSON:")
        print(json.dumps(response.json(), indent=2))
    except:
        print("Response Text:")
        print(response.text)
        
except Exception as e:
    print(f"Error: {e}")
