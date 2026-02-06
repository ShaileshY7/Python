# ​ Read only the first line of bio.txt.​

# file=open("/home/shailesh/Python/Lecture08/bio.txt","r")
# line1=file.readline()
# print(line1)
# file.close()
# ================================================
# to not write file.close() weusenthis syntax that i write below
# with open("/home/shailesh/Python/Lecture08/bio.txt","r") as f:
#     line1=f.readline()
#     print(line1)

# =====================================================================
# ​ Print how many lines are present in notes.txt.​
# with open("/home/shailesh/Python/Lecture08/intro.txt","r") as f:
#     listOfLines=f.readlines()
#     print(listOfLines)
#     print(len(listOfLines))


# remaining file
import os
# os.rename("/home/shailesh/Python/Lecture08/certificate.txt","/home/shailesh/Python/Lecture08/shailesh.txt")
os.remove("/home/shailesh/Python/Lecture08/shailesh.txt")
