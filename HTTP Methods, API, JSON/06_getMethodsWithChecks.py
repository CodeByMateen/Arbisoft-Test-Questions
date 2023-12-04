import requests

# GET request with pagination
url = "https://jsonplaceholder.typicode.com/posts?_limit=2"
response = requests.get(url)
if response.status_code == 200:  # 200 OK indicates success for a GET request
  print("GET request successful!")
  print("Response:", response.json())
else:
  print("GET request failed. Status code:", response.status_code)
  print("Response:", response.text)

# GET request with pagination and filtering
url = "https://jsonplaceholder.typicode.com/posts?_limit=4&userId=3"
response = requests.get(url)
if response.status_code == 200:  # 200 OK indicates success for a GET request
  print("GET request successful!")
  print("Response:", response.json())
else:
  print("GET request failed. Status code:", response.status_code)
  print("Response:", response.text)

# GET request with pagination and filtering and sorting
url = "https://jsonplaceholder.typicode.com/posts?_limit=2&userId=2&_sort=id"
response = requests.get(url)
if response.status_code == 200:  # 200 OK indicates success for a GET request
  print("GET request successful!")
  print("Response:", response.json())
else:
  print("GET request failed. Status code:", response.status_code)
  print("Response:", response.text)

# GET request with pagination and filtering and sorting and sorting direction
url = "https://jsonplaceholder.typicode.com/posts?_limit=3&userId=2&_sort=id&_direction=desc"
response = requests.get(url)
if response.status_code == 200:  # 200 OK indicates success for a GET request
  print("GET request successful!")
  print("Response:", response.json())
else:
  print("GET request failed. Status code:", response.status_code)
  print("Response:", response.text)
