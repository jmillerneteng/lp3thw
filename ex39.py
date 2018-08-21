states = {
    'Washington': 'WA',
    'Missouri': 'MO',
    'California': 'CA',
    'Arizona': 'AZ',
    'Texhas': 'TX'
}

states['Oregon'] = 'OR'

cities = {
    'WA': 'Bellvue',
    'CA': 'SanFran',
    'MO': 'STL'
}

cities['WA'] = 'Seattle'
cities['WA'] = 'Spokane'
cities['OO'] = 'Portland'
cities['MO'] = 'Misery'
cities['CA'] = 'San Jose'
cities['AZ'] = 'Phonix'
cities['TX'] = "BigD"

print('-' * 10)
print("Washington state has: ", cities['WA'])
print("Arizonaz state has: ", cities['AZ'])


print('-' * 10)
print("Oregon's abbrev is", states['Oregon'])
print("Missouri's abbrev is", states['Missouri'])

print('-' * 10)
print("Washington has: ", cities[states['Washington']])
print("Missouri has", cities[states['Missouri']])


print('*' * 10)

for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('!' * 20)

state_get = "TX"
state = states.get(state_get)
if not state:
    print("Sorry, TX not legit")

city = cities.get((state_get), 'Does not compute here, should see this below')
print(f"The city for the state 'tx' is: {city}")

