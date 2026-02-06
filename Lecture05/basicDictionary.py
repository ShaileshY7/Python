student={
    "name":"shailesh Yadav",
    "roll no":226,
    "city":"Ballia",
    # "name":"Shail"
}
# print(student["city"])
# student["college"]="Ims Engineering College"
# student["name"]="Shailesh"
# student.pop("city")
print(student.keys())#name,rool no,city
print(student.values())#shailesh yadav,226,ballia
print(student.items())#it print full dictionary
print(student.get("name"))#shailesh yadav
student.update({"city":"Ghaziabad"})
print(student)#update city in dictionary