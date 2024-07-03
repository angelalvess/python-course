import json
from app78 import PATH_FILE, Person

with open(PATH_FILE, 'r', encoding='utf-8') as file:
    persons = json.load(file)
    p1 = Person(**persons[0])
    p2 = Person(**persons[1])
    p3 = Person(**persons[2])


print(p1.name, p1.age)
print(p2.name, p2.age)
print(p3.name, p3.age)
