# Exercise 3: JSON Handling with the json Library
import json
 
user_data= {"name": "John", "age": 30, "city": "New York"}

user_data["age"] = 22 

with open("modify.json", mode="r") as f:
    user_data = json.load(f) 

with open("modify.json", mode="w", newline="") as f:
    json.dump(user_data, f) 
    