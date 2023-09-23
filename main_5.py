if 5 == 5:
    print("Yes")
    print("!!!")

user_data = int(input("Введите число:"))

if user_data != 5:
    print("Мы на месте")
    if user_data > 6:
        print("Number is bigger than 6")

isHappy = False

if isHappy:
    print("User is happy!")
elif user_data == 5:
    print("Number is 5")
else:
    print("User is unhappy!")

isHappy = False

if not isHappy:
    print("User is not happy!")

isHappy = True
if isHappy and user_data == 7:
    print("Мы у цели!")

data = input()

number = 5 if data == "Five" else 0

print(number)