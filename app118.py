import json
from pprint import pprint

object_json = '''
{
    "name": "John",
    "age": 30,
    "city": "New York",
    "movies": [
        {
            "title": "The Shawshank Redemption",
            "year": 1994
        },
        {
            "title": "The Godfather",
            "year": 1972
        }
    ]
}
'''

filme = json.loads(object_json)
pprint(filme)

print(json.dumps(filme, indent=4))
