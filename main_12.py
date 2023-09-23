country = {4: 3}
print(country[4])

Country = {'code': 'RU', 'name': 'Russian', 'population': 144}
print(Country['name'])
print(Country)
print(Country.items())
print(Country.get('name'))


for key in Country:
    print(key)

for key, value in Country.items():
    print(key, " - ", value)
Country['code'] = None
print(Country)
print(Country.keys())
print(Country.values())
Country.pop('name')
Country.popitem()
print('Items', Country)

_Country = dict(code = 'RU', name = 'Russian')

print(_Country['name'])
_Country.clear()
print('items', _Country)

