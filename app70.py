import json

person = {
    "name": "John",
    "age": 36,
    "country": "Norway",
    "address": [
        {"street": "Oslo West 16",
         "city": "Oslo",
         "zipcode": "1234"
         },
        {"street": "Oslo West 16",
         "city": "Oslo",
         "zipcode": "1234"}
    ],
    "phone": "12345678"

}

with open("person.json", "w", encoding="utf-8") as file:
    json.dump(person, file, indent=4, ensure_ascii=False)
