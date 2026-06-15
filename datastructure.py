#string
'''
user_name="renjana"
#0 1 2 3 4 5 6
#r e n j a n a
#-7 -6 -5 -4 -3 
print("username: ",user_name)
print(user_name[3])
print(user_name[-5])
print(user_name[7])

data="python is a programming language"
print(data[1:8])
print(data[0:9])
print(data[:6])
print(data[10:-2])
print(data[10:2:-2])
print(data[::-2])

string="blue car"
print(string.upper())
print(string.lower())
print(string.capitalize())
print(string.title())

print(string.startswith("blu"))
print(string.endswith("r"))
print(string.replace("blue","red"))
#string[1]="a"
#print(string)
print(id(string))
uppercase=string.upper()
print(id(uppercase))

#list mutable

details=["renjana",20,"thirumala"]
details.insert(2,"graduate")
details.append("emmanuel clg")
details.extend("python")
details.append(["english","mal","korean"])
details.extend(["java","c++","sql"])
print(details[12])
details.pop(3)
details.reverse()
print(details)

student1 ={"English","hindhi","malayalam"}
student2 ={"English","hindhi","german"}
student3 ={"English","korean","malayalam"}

print(student1.union(student2))
print(student1.intersection(student2))
print(student1.difference(student2))

print(student1|student2)
print(student1 & student2)
print(student1 - student2)

set1={1,2,3}
set2={4,5,6}
set3={7,8,9}
print(set1.isdisjoint(set2))

#frozen set
fs1=frozenset("renjana")
fs2=frozenset([12,34,56])
fs3=frozenset((87,65,54))

print(fs1)
print(fs2)
print(fs3)

#dictionary

student = { 
    "name":"Renjana",
    "Age" : 20,
    "place": "Thirumala"
     }
print(student)
print(student["name"])


print(student)
print(student["name"])
print(student.get("marks"))
student["marks"]=79
student.pop("Age")
del student["name"]
student.update({"palce":"poojapura","marks":80})
print(student)


info=dict(city="TVM",location="keralam")
print(info.keys())
print(info.values())
print(info)'''

#try out updation for multiple insertions

employee={
    "emp1" : {"name" : "renjana","age" : 20 },
    "emp2" : {"name" : "adhithya","age" : 20 },
    "emp3" : {"name" : "darsana","age" : 21 },
    "emp4" : {"name" : "aardra","age" : 21 },
    "emp5" : {"name" : "gouri","age" : 20 }
 }
print(employee["emp3"]["age"])