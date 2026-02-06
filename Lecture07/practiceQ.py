# Question:1->Write a function to calculate the factorial of a number.​

# def fact(n):
#     if(n==1):
#         return 1
#     return n*fact(n-1)
# print(fact(5))

# =================================================================
# Question:2-> Write a recursive function to print numbers from 1 to N.​

# def print1ton(n):
#     if(n==0):
#         return
#     print1ton(n-1)
#     print(n)
# print1ton(5)

# ===============================================================
# Write a function that checks if a number is prime.​

# def primenum(n):
#     if(n<=1):
#         print("Not prime Nummber")
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not Prime Number")
#             return
#     print("Prime Number")
# primenum(5)

# =======================================================
# Question:4->Write a recursive function to find the sum of first N natural numbers.

# def sum1ton(n,sum):
#     if(n==0):
#         return sum
#     return sum1ton(n-1,sum+n)
# print(sum1ton(10,0))

# ====================================================
# question:5->Write a function greet_user(name) that prints a personalized message for
# Saumya Singh.​

# def greet_user(name):
#     print(f"{name} is hardworking")
# greet_user("shailesh")

# ============================================================
# Write a recursive program to print the reverse of a string.​

# s="shailesh"
# rev=""
# for ch in s:
#     rev=ch+rev
# print(rev)

# def rev(s):
#     if(s==""):
#         return s
#     return rev(s[1:])+s[0]
# print(rev("python"))

# ==============================================================
# Question:7->Write a function to return the largest of 3 numbers.

# def largest(a,b,c):
#     if(a>b and a>c):
#         print("a is largest")
#         if(b>a and b>c):
#             print("b is largest")
#     else:
#         print("c is largest")

# largest(3,2,5)


# =========================================================================
# ​ Question:8->Write a recursive function to print even numbers from 2 to N.​

# def printeven(n):
#     if(n<2):
#         return
#     if(n%2==0):
#          print(n)
#     return printeven(n-1)
# printeven(20)    
    

# =======================================================================================
# Question:9->Write a function that returns both the sum and average of 5 inputs.​

# def sumandaveraage(a,b,c,d,e):
#     sum=0
#     avg=0
#     sum=(a+b+c+d+e)
#     avg=(a+b+c+d+e)/5

#     return sum,avg

# sum,avg=sumandaveraage(1,2,3,4,5)
# print(sum,avg)

# ===============================================================
# Question:10->Write a program to count vowels in a string using a function.

# def countvowels(userInput):

#     vowels="aeiouAEIOU"
#     countvowels=0

#     for ch in userInput:
#         if(ch.isalpha()):
#             if(ch in vowels):
#                 countvowels+=1
#     return countvowels

# vowels=countvowels("Shailesh")
# print(vowels)
