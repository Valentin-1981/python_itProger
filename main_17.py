file = open("./data/text.txt", 'w')
file.write('Hello\n')
file.write('!!!')
file.close()

data = input('Введите текст: ')
file_2 = open("./data/text2.txt", 'a')
file_2.write(data + '\n')
file_2.write('!!!')
file_2.close()

file = open('./data/text.txt', 'r')
print(file.read(3))
for line in file:
    print(line, end='')
file.close()
