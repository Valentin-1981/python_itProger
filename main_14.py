data = set('hello')

print(data)

data_2 = {5, 8, 9, 0, 5, 0}

print(data_2)

data_2.add(32)

data_2.update([True, 43, '34', '75'])
print(data_2)
data_2.remove(True)
print(data_2)
data_2.pop()
print(data_2)
data_2.clear()
print(data_2)

nums = [5, 7, 5, 3, 8, 3]
nums = set(nums)
print(nums)

new_data = frozenset([5, 8, 9, 0, 5, 0, True, 43, '34', '75'])
print(new_data)