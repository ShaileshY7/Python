expenses=[]#list of expenses in term of dictionary
print("Welcome to exoenses tracker:")

while True:
    print("========Menu========")
    print("1. Add Expenses")
    print("2. View all Expenses")
    print("3. View Total karcha")
    print("4, Exit")

    choice=int(input("Enter your choice:"))

 # Add Expenses
    if choice==1:
        date=input("Kis date par kitna karcha huwa tha?:")
        category=input("Kis type karcha kiya? (Food,travel,Clothes,Fitnes):")
        description=input("Give more details:")
        amount=float(input("Enter the amount:"))

        expense={
            "date":date,
            "category":category,
            "description":description,
            "amount":amount
        }

        expenses.append(expense)
        print("\n Ya bro,Expenses added succesfully")

#  View all Expenses
    elif choice==2:
        
        if(len(expenses)==0):
            print("No Expenses Happen:")
        else:
            print("Ye hai apkee Expenses:")
            count=1
            for eachKarcha in expenses:
                print(f"Karcha Number {count}->{eachKarcha["date"]},{eachKarcha["category"]},{eachKarcha["description"]},{eachKarcha["amount"]}")
                count=count+1

# View Total karcha
    elif choice==3:
        total=0
        for eachKarcha in expenses:
            total=total+eachKarcha["amount"]
        print("\n Total Karcha:",total)


# Exit
    elif choice==4:
        print("Dhanyabad apne hamara system use kiya")
        break
    else:
        print("INVALID CHOICE")