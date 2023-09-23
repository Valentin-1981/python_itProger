for i in range(1, 6, 2):
    print(i)

word = "Hello world!"

for i in word:
    if i == "!":
        print("Yes")

y = 5

while y < 15:
    print(y)
    y += 2

for i in range(1, 11):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

isHasCar = True

while isHasCar:
    if input("Enter data:") == "Stop":
        isHasCar = False
