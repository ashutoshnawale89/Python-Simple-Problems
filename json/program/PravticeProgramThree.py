import json
""""""

json_Data = """{"userData": [
  {
    "name": "John Doe",
    "age": 30,
    "address": {
      "street": "123 Main Street",
      "city": "Anytown",
      "state": "CA"
    }
  },
  {
    "name": "Jane Doe",
    "age": 25,
    "address": {
      "street": "456 Elm Street",
      "city": "Sometown",
      "state": "NY"
    }
  }
]}"""
data = json.loads(json_Data)
print(data)
print("All Name of People in list ----------------")
for i in data["userData"]:
    print(i["name"])
print("All Age of People in list ----------------")
for i in data["userData"]:
    print(i["age"])
print("All Address of People in list ----------------")
for i in data["userData"]:
    print(i["address"])