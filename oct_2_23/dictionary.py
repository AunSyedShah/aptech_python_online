person = {
    "name": "taha",
    "age": 30,
    "skills": ["python", "javascript", "c++", "c#"],
    "address": {"street": "123 street", "city": "tehran", "country": "iran"},
    "is_male": True,
}
# print dictionary
print(person)
# access a key
print(person["name"])
# add an element to dictionary
person["job"] = "programmer"
# print to verify
print(person)
# delete an element from dictionary
del person["job"]
# access list inside dictionary
print(person["skills"][1])
# access dictionary inside dictionary
print(person["address"]["city"])