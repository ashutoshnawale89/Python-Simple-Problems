# Example JSON data
import json

json_data = '''
{
  "name": "John Doe",
  "age": 30,
  "email": "johndoe@example.com",
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "country": "USA"
  },
  "languages": ["Python", "JavaScript", "Java"]
}
'''

# Parsing JSON data
data = json.loads(json_data)
print(data)
# Accessing top-level fields
name = data['name']
age = data['age']
email = data['email']
print(f"Name: {name}, Age: {age}, Email: {email}")

# # Accessing nested fields
street = data['address']['street']
city = data['address']['city']
country = data['address']['country']
print(f"Address: {street}, {city}, {country}")
#
# # Accessing elements in a list
languages = data['languages']
for language in languages:
    print(f"Language: {language}")

data1 = json.e