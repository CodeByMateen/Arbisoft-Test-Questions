  import requests

  url = "https://jsonplaceholder.typicode.com/posts"

  data = {
      "userId": 1,
      "id": 101,
      "title": "Test Post",
      "body": "This is a test post."
  }

  # POST request
  response = requests.post(url, data=data)

  # Check the status code
  if response.status_code == 201:  # 201 Created indicates success for a POST request
    print("POST request successful!")
    print("Response:", response.json())
  else:
    print("POST request failed. Status code:", response.status_code)
    print("Response:", response.text)

  # GET request
  response = requests.get(url)
  if response.status_code == 200:  # 200 OK indicates success for a GET request
    print("GET request successful!")
    print("Response:", response.json())
  else:
    print("GET request failed. Status code:", response.status_code)
    print("Response:", response.text)

  # PUT request
  url = "https://jsonplaceholder.typicode.com/posts/101"
  data = {
      "userId": 1,
      "id": 101,
      "title": "Test Post Updated",
      "body": "This is an updated test post."
  }
  response = requests.put(url, data=data)
  if response.status_code == 200:  # 200 OK indicates success for a PUT request
    print("PUT request successful!")
    print("Response:", response.json())
  else:
    print("PUT request failed. Status code:", response.status_code)
    print("Response:", response.text)

  # DELETE request
  url = "https://jsonplaceholder.typicode.com/posts/101"
  response = requests.delete(url)
  if response.status_code == 200:  # 200 OK indicates success for a DELETE request
    print("DELETE request successful!")
    print("Response:", response.json())
  else:
    print("DELETE request failed. Status code:", response.status_code)
    print("Response:", response.text)

  # PATCH request
  url = "https://jsonplaceholder.typicode.com/posts/101"
  data = {
      "userId": 1,
      "id": 101,
      "title": "Test Post Updated",
      "body": "This is an updated test post."
  }
  response = requests.patch(url, data=data)
  if response.status_code == 200:  # 200 OK indicates success for a PATCH request
    print("PATCH request successful!")
    print("Response:", response.json())
  else:
    print("PATCH request failed. Status code:", response.status_code)
    print("Response:", response.text)

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
  url = "https://jsonplaceholder.typicode.com/posts?_limit=2&userId=1"
  response = requests.get(url)
  if response.status_code == 200:  # 200 OK indicates success for a GET request
    print("GET request successful!")
    print("Response:", response.json())
  else:
    print("GET request failed. Status code:", response.status_code)
    print("Response:", response.text)

  # GET request with pagination and filtering and sorting
  url = "https://jsonplaceholder.typicode.com/posts?_limit=2&userId=1&_sort=id"
  response = requests.get(url)
  if response.status_code == 200:  # 200 OK indicates success for a GET request
    print("GET request successful!")
    print("Response:", response.json())
  else:
    print("GET request failed. Status code:", response.status_code)
    print("Response:", response.text)

  # GET request with pagination and filtering and sorting and sorting direction
  url = "https://jsonplaceholder.typicode.com/posts?_limit=2&userId=1&_sort=id&_direction=desc"
  response = requests.get(url)
  if response.status_code == 200:  # 200 OK indicates success for a GET request
    print("GET request successful!")
    print("Response:", response.json())
  else:
    print("GET request failed. Status code:", response.status_code)
    print("Response:", response.text)
