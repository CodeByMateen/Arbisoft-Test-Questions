import requests

url = "https://jsonplaceholder.typicode.com/posts/64"

data = {
    "userId": 1,
    "id": 101,
    "title": "Test Post Updated",
    "body": "This is an updated test post."
}

response = requests.patch(url,json=data)
if response.status_code == 200:
  print("successful!")
  print(response.json())
else:
  print("unsuccessful!")
  print(response.json())
