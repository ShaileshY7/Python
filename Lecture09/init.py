class Student:
    collegeName="IMS Engineering College"
    def __init__(self,name,course):
        self.name=name
        self.course=course

student1=Student("Shailesh","B.tech")
print("Student1 name-",student1.name)
print("Student1 course-",student1.course)

student2=Student("Ragini","MBA")
print("Student2 name-",student2.name)
print("Student2 course-",student2.course)