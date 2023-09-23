str = "iTproger"

print(str[3])
print(len(str))
print(str.count("r"))
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.isupper())
print(str.islower())
print(str.find('p'))

word = "footBAll, baskETBall, baseBAll"
hobby = word.split(', ')

print(hobby[1])

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

print(hobby)

result = ", ".join(hobby)
print(result)

word = 'football'
print(word[4:-1:2])

lis = [4, 7, 10, "Hello", True, 6.5]
print(lis[3])
print(lis[2:-1:2])
print(lis[::-1])
print(lis[::-2])

