# def multiply(a=10,b=5):
#     return a*b

# print(multiply(2,5))

# result=multiply(12,12)
# print(result)
# print(multiply())

# ==============================================================
# Question-1> Write a function square(num) that returns the square of a number.​

# def square(num):
#     return num*num
# print(square(5))

# ================================================================

# Question->2:Write a function that takes a string and returns the count of vowels and
# consonants separately.

# def countVowAndConso(userInput):
#     #  define
#     vowels="aeiouAEIOU"
#     countVowels=0
#     countConsonant=0

#     for eachchar in userInput:
#         if(eachchar.isalpha()):
#             if(eachchar in vowels):
#                 countVowels+=1
#             else:
#                 countConsonant+=1
    
#     return countVowels,countConsonant

# print(countVowAndConso("Shailesh Yadav"))


# =================================================================
# Question:3->:Define a function convert_to_upper(word) that returns the uppercase
# version of the string.​

# def upper_case(userInput):
#     return userInput.upper()

# print(upper_case("shaileh"))


# =================================================================
# Question:4>​ Create a function full_name(fname, lname) that returns the full name
# joined with a space.

def full_name(fanme,lname):
    return fanme,lname

print(full_name("Shail","Yadav"))