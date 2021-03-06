num = [1,2,3,4,5]
# numlist

numlist.reverse()
numlist.sort()

mystring = "julian"
for i in list(mystring):
	print(i)

l = list(mystring)
# l
# ['j', 'u', 'l', 'i', 'a', 'n']
t = tuple(mystring)
# t
# ('j', 'u', 'l', 'i', 'a', 'n')


# Dicts
pybites = {'julian': 30, 'bob': 33, 'mike': 33}

people = {}
people['julian'] = 30
# people
# {'julian': 30}

pybites.keys()
dict_keys(['julian', 'bob', 'mike'])

pybites.values()
dict_values([30, 33, 33])

pybites.items()
dict_items([('julian', 30), ('bob', 33), ('mike', 33)])

for keys in pybites.keys():
	print(keys)
# julian
# bob
# mike

for values in pybites.values():
	print(values)
# 30
# 33
# 33

for keys, values in pybites.items():
	print(keys + str(values))
# julian30
# bob33
# mike33

for keys, values in pybites.items():
	print('%s is %d years of age' % (keys, values))
# julian is 30 years of age
# bob is 33 years of age
# mike is 33 years of age