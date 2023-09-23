nums = [1, 3, 6, 7, 4, True, "Hello", 6.7, [5, 7]]

nums[0] = 50
nums[5] = 0.6

print(nums[3])
print(nums[-1][1])

numbers = [5, 2, 7]
numbers.append(100)
numbers.insert(1, 8)
b = [7, 5, 2]
numbers.extend(b)
numbers.sort()
numbers.reverse()
numbers.pop()
numbers.remove(100)
numbers.pop(0)
numbers.pop(-2)
# numbers.clear()
print(numbers.count(7))
print(len(numbers))
print(numbers)

Nums = [5, 2, 7, "string", False]

for el in Nums:
    el *= 2
    print(el)