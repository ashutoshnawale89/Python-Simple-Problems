import json

"""Write a Python program to print the following:
The total price of all the products
The total quantity of all the products"""


data_JSON = '''{"products": [
                            { "name": "T-shirt","price": 10,"quantity": 10 },
                            {"name": "Hat","price": 5,"quantity": 5}
                            ]
                    }'''
data = json.loads(data_JSON)
print(data)
total_price = 0
total_quantity = 0
for i in data["products"]:
    total_quantity = total_quantity + i["quantity"]
    total_price = total_price + i["price"]
print("Total Price is: ",total_price)
print("Total Quantity is :",total_quantity)
