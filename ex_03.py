"""Dict"""

dct1 = {}
dct2 = dict()
dct3 = {str(i): i**2 for i in range(10)}

print(dct1)
print(dct2)
print(dct3)

print(dct3.keys())
print(dct3.values())
print(dct3.items())

print(dct3['4'])

try:
    print(dct3['10'])
except KeyError as e:
    print(f"Key {e} not in dict")

print(dct3.get('10'))

dct3.update({"10": 10**2})

print(dct3)

dct3.update(last=100**2)

print(dct3)