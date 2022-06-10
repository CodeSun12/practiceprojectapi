import base64

import requests
import json

URL = "http://127.0.0.1:8000/register/"

files = {'media': open('/home/shakeeb/Downloads/tasks.png', 'rb',)}
headers = {'Content-Type': 'application/json'}

response = requests.post(
    url=URL,
    # headers=headers,
    data={
        'f_name': 'Hamza',
        'l_name': 'Khan',
        'email': 'hamza@gmail.com',
        "phone_no": 923144545458,
        'dob': '2022-05-10',
        'password': 0o23456,
        'cnic': 3660225252587,
        'role': 'Python Developer',
        'gender': 'Female',
    },
    files=files
)
data = response.json()
print(data)

