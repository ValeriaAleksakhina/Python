class Human:
    def __init__(self, name: str, age: int, is_work: bool):
        self.name = name
        self.age = age
        self.is_work = is_work



    def greetings(self):
        print(f'{self.name} говорит "Hello"')


    def good_bye(self):
        print(f'{self.name} говорит "Bye Bye"')


    def __str__(self):
        return(f'Это человек с именем {self.name}, возраста {self.age}')



stone = Human('Кирилл', 38, True)
rudolf = Human('Rudolf', 18, True)

print(stone.name)
print(stone.age)

stone.name = 'Kirill'
print(stone.name)

stone.greetings()
stone.good_bye()

print(stone)
