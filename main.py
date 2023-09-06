# write your code here
person = {
    "name": "swiper",
    "age": "17",
    "hobbies": ["swiping"]

}
print (person["name"])
print (person["age"])

person["age"] = "18"
person["country"] = "Kuwait"
print (person)

person["hobbies"].append("repenting")

def check_hobbies(person):
    if len(person["hobbies"])>=2:
        print(f'wow you are astonishing')

check_hobbies(person)


