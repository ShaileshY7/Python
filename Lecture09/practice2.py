# Create class Student that takes 3 marks and has a method average()

class Student:
    def __init__(self,name,listOfMarks):
        self.name=name
        self.listOfMarks=listOfMarks
    
    def average(self):
        sum=0
        for eachValue in self.listOfMarks:
            sum=sum+eachValue
        average=sum/3
        print("Average marks:",average)
student1=Student("Shailesh",[90,95,88])
student1.average()