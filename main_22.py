class Cat:
    def __init__(self, name = None, age = None, isHappy = None):
        # self.name = name
        # self.age = age
        # self.isHappy = isHappy

        self.set_data(name, age, isHappy)

        self.get_data()

    # def __init__(self):
    #     pass

    name = None
    age = None
    isHappy = None

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, 'age:', self.age, 'isHappy:', self.isHappy)

cat1 = Cat()
cat1.set_data('Barsik', 23, True)

cat2 = Cat()
cat2.name = 'Жопен'
cat2.age = 43
cat2.isHappy = False

print(cat1.name)
print(cat2.name)

cat1.get_data()
cat2.get_data()

cat1 = Cat('Joseph', 34, True)
cat1.set_data()
cat1.get_data()

cat3 = Cat("Grisha", 65, True)
cat3.get_data()

cat3.set_data('Gosha', 87)