"""Dict 03"""


dct = {"Bill":"122326", "Jill":"2546885", "Dill":"905633"}

def find_contact(dct, number):
    result = []
    
    for name, phone in dct.items():
        if str(number) in phone:
            result.append((name, phone))
    return result

dct = {"Bill":"123456", "Jill":"23467885", "Dill":"905633"}

def find_contact2(dct, number):
    result = []

    for n, p in dct.items():
        if str(number) in p:
            result.append((n, p))
    return result

# if __name__ == "main":
#     print(find_contact(dct, "5"))


if __name__ == "__main__":
    print(find_contact2(dct, "33"))