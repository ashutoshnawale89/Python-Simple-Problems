import json
"""Write a Python program to print the following:
The names of all the users
The emails of all the users"""

json_Data = '''{"users": [
    {
      "name": "John Doe",
      "email": "johndoe@example.com"
    },
    {
      "name": "Jane Doe",
      "email": "janedoe@example.com"
    }
  ]}'''
data = json.loads(json_Data)
print(data)
print("All User Name :    --------")
for i in data["users"]:
    print(i["name"])
print("All User Emails :    --------")
for i in data["users"]:
    print(i["email"])