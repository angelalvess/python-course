
import json

with open('person.json', 'r', encoding='utf-8') as file:
    person = json.load(file)
    print(person)
