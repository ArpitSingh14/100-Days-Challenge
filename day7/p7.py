import json

student = {
    "name": "Arpit",
    "age": 20,
    "skills": ["Python", "SQL"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)