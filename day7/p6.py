import json
json_data = '{"name": "Arpit", "age": 20}'
student = json.loads(json_data)

print(student["name"])