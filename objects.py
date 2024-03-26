# created a class
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display_info(self):
        print(f"I am {self.name}. I am a {self.age} year old {self.gender}.")

# instantiation
worker1 = Person("John", 21, "male")
worker1.display_info()