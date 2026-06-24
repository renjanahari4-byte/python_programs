

file=open("studentdetails.txt","w")
file.write("student details\n")
file.close()

name = input("Enter student name: ")
age = input("Enter age: ")
marks = input("Enter marks: ")

file = open("studentdetails.txt","a")

file.write(
    f"Name: {name}, Age: {age}, Marks: {marks}\n"
)

file.close()

print("Student Added Successfully")

attendance=int(input("enter attendance %:  "))
file = open("studentdetails.txt","a")
file.write(f"attendance {attendance} ")
file.close()

file = open("studentdetails.txt","r")
data=file.read()
print(data)
file.close()

file = open("studentdetails.txt","r")
data=file.readline()
print(data)
file.close()

file = open("studentdetails.txt","r")
data=file.readlines()
print(data)
file.close()


file=open("studentdetails.txt","w")

data=[
    "Student Report\n",
    "Name: Adhithya\n",
    "Marks: 90\n"
]

file.writelines(data)

file.close()

with open("studentdetails.txt", "r") as file:
    print(file.name)
    print(file.mode)
    print(file.closed)

with open("studentdetails.txt","r")as f:
    print("current position ",f.tell())
    f.read(6)
    print("after read position: ",f.tell())
    f.seek(4)
    print("after seek position: ",f.tell())
    print(f.read())

import os

with open("studentdetails.txt","r") as f:

    print("File name:", f.name)
    print("File mode:", f.mode)

if not os.path.exists("student_performance"):
        os.mkdir("student_performance")
        print("Directory created")

print("Directory contents:")
print(os.listdir())

if os.path.exists("studentdetails.txt"):
        print("File exists")

        os.rename(
            "studentdetails.txt",
            "students.txt"
        )

        print("File renamed")

import pickle
import json

try:

    file = open("students.txt", "r")

    data = file.read()

    print("Student File Data:")
    print(data)

    file.close()


except FileNotFoundError:

    print("File not found")


except PermissionError:

    print("Permission denied")


except ValueError:

    print("Invalid file mode")


finally:

    print("Operation completed")

file = open("student.dat", "wb")

file.write(b"Student Binary Data")

file.close()

print("\nBinary file created")

file = open("student.dat", "rb")

data = file.read()

print("Binary Data:")

print(data)

file.close()

student = {

    "name":"Adhithya",

    "age":20,

    "marks":90

}

file = open("student.pkl","wb")

pickle.dump(student,file)

file.close()


print("\nPickle file created")


file = open("student.pkl","rb")

data = pickle.load(file)

print("Pickle Data:")

print(data)

file.close()

student_json = {

    "name":"Adhithya",

    "course":"Python",

    "marks":90

}

file = open("student.json","w")

json.dump(student_json,file)

file.close()


print("\nJSON file created")


file = open("student.json","r")

data = json.load(file)

print("JSON Data:")

print(data)

file.close()