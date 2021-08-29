import requests
from datetime import datetime

USERNAME = ''
TOKEN = ''

pixela_endpoint = 'https://pixe.la/v1/users'

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Create account
user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

# Graph post req (create graph)
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
    "id": "graph1",
    "name": "Workout Graph",
    "unit": "minutes",
    "type": "int",
    "color": "momiji",
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)

# Post a pixel

post_today = True
if post_today:
    today = datetime.now()
    today = today.strftime("%Y%m%d")
else:
    today = datetime(year=2021, month=2, day=18)

pixel_json = {
    "date": today,
    "quantity": "5",
}

post_pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/graph1'
response_post = requests.post(url=post_pixel_endpoint, headers=headers, json=pixel_json)
print(response_post.text)

# Update a pixel (change)
new_pixel_data = {
    "quantity": "0"
}
response_update = requests.put(url=f'{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}', headers=headers, json=new_pixel_data)
print(response_update.text)

# Delete a pixel
response_delete = requests.delete(url=f'{pixela_endpoint}/{USERNAME}/graphs/graph1/{today}', headers=headers)
print(response_delete.text)