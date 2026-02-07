#Question-1> Create class Student with name, class, marks. Add method get_percentage().

class Student:

    def __init__(self,name,Class,listofmarks):
        self.name=name
        self.Class=Class
        self.listofmarks=listofmarks

    def get_percentage(self):
        sum=0
        totalMarks=500
        for eachvalue in self.listofmarks:
            sum=sum+eachvalue
        percentage=(sum/totalMarks)*100
        print("Percentage is :",percentage)

student1=Student("Shailesh","10",[95,67,67,90,85])
student1.get_percentage()

# question:2->Create class FoodOrder with item name, quantity, price. Add method to calculate
# bill.

class FoodOrder:

    def __init__(self,foodname,quantity,price):
        self.foodname=foodname
        self.quantity=quantity
        self.price=price

    def total_bill(self):
        print("Total bill:",self.quantity*self.price)

order=FoodOrder("Shaiesh",5,250)
order.total_bill()