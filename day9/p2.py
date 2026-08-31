class Student:
    def set_details(self, name, age):
        self.name = name
        self.age = age

student1 = Student()

student1.set_details("Arpit", 21)

print(student1.name)
print(student1.age)