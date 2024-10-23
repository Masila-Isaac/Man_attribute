class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hi, I'm {self.name}, a {self.age} year old {self.gender}.")

# Create an instance of the Person class
person1 = Person("Masila Isaac", 18, "male")

# Call the introduce method
person1.introduce()
