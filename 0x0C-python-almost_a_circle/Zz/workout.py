#!/usr/bin/python3
import json
def greeting(**kwargs):
    if kwargs is not None:
        for _ in kwargs:
            print(f"=> {_} : {kwargs[_]}")
    print(kwargs.items())
k = 0
i = k if k > 0 else 'A'
# print(f'i = {i} k = {k}')
greeting(name1 ="kwazaki", age1 = 32, name2 ="kopaiashii", age2 = 32)
# Output: name == yasoobrrr2


# Sample Python dictionary with non-string keys
data = {
    ('name', 'age'): {"John": 30},
    'city': "New York",
     'name': 'age',
     'John': '30'
}


# Serialize the dictionary, handling non-string keys and custom indentation
json_str = json.dumps(data, skipkeys=True, indent=2)


# Print the serialized JSON string
print(json_str)
with open ("json.txt", "w", encoding="utf-8") as FILE:
    FILE.write(json_str)