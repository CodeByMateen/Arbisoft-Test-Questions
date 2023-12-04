import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
  "userId": 1,
  "id": 101,
  "title": "Test Post",
  "body": "This is a test post."
}

response=requests.post(url,data=data)
if response.status_code==201:
  print("successful!")
  print(response.json())
else:
  print("unsuccessful!")
  print(response.json())