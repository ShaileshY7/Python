import random

item_list=["Rock","Paper","Scissor"]

user_choice=input("Enter your choice (Rock,Paper,Scissor)=")
computer_choice=random.choice(item_list)

print(f"User choice={user_choice} and Computer choice={computer_choice}")

if user_choice==computer_choice:
    print("Both choose same= Match tie")

elif user_choice=="Rock":
    if computer_choice=="Paper":
        print("Paper covers rock = Computer Win")
    else:
        print("Roch smases scissor= You win")

elif user_choice=="Paper":
    if computer_choice=="Scissor":
        print("Scissor cut paper = Computer win")
    else:
        print("Paper covers Rock =You win")

elif user_choice=="Scissor":
    if computer_choice=="Paper":
        print("Scissor cut the paper = You win")
    else:
        print("Rock smases scissor = Computer win")