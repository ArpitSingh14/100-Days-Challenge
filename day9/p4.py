class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")
        print(f"I am studying {self.course}")

    def study(self):
        print(f"{self.name} is studying")


student1 = Student("Arpit", 21, "Computer Science")

student1.introduce()
student1.study()