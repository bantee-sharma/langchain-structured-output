from typing import TypedDict

class person(TypedDict):

    name : str
    age : int


new_person: person = {"name":"bantee","age":24}

print(new_person)