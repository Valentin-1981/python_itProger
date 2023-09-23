def test_func(word):
    print(word, end = "")
    print('!')

test_func('Halo')
test_func(5)
test_func(5.6)

def summa(a, b):
    res = a + b
    print('Result: ', res)

summa(5, 7)
summa('H', 'i')

def Summa(a, b):
    res = a + b
    return res

res = Summa(2.5, 3.5)
print('Result', res)

res = Summa('H', 'i')
print('Result:', res)