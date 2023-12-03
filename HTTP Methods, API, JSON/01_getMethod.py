# payments = requests.get("https://www.jsonkeeper.com/b/9QRZ")

import requests

'''Get Method'''

users = requests.get( "https://gist.github.com/CodeByMateen/220c5a5ff75548f819dd821e7fdc557d/raw"
)

print(users)  # prints status code 200

users = users.json()
# print(users)  # print all users

# print([user for user in users if user.get('id') > 4 and user.get('id') < 8])  # print users with particular conditions

print([user for user in users if user.get('name') == 'Danish Ali']) # Danish data will be printed
