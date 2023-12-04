import requests

url = "https://jsonplaceholder.typicode.com/posts/16"

response=requests.delete(url)
if response.status_code == 200:
  print("successful!")
  print(response.json())
else:
  print("unsuccessful!")
  print(response.json())