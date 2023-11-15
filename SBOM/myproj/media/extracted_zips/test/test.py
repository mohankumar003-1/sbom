import pandas
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name}, and I am {self.age} years old."


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
# This is a vulnerable Python script with a security issue
import os

user_input = input("Enter a filename: ")
file_path = f"/path/to/directory/{user_input}"

if os.path.exists(file_path):
    os.system(f"rm {file_path}")
    print(f"File {file_path} deleted.")
else:
    print("File not found.")


print(person1.introduce())
print(person2.introduce())
