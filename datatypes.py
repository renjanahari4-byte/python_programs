student_name=input("Enter the student name: ")
student_id =int(input("Enter the student_id: "))
student_mark=float(input("Enter the student_mark: "))
is_present=bool(input("Is present or not(T/F): "))
language_known=(input("Enter the languages known: ")).split(",")


print("the student  name is  ",student_name)
print("the student  id is  ",student_id)
print("the student  mark is  ",student_mark)
print("present or not ", is_present)
print("languages known are" ,language_known)

print(type(student_name))
print(type(student_id))
print(type(student_mark))
print (type(is_present))
print (type(language_known))

num1=20
num2=20
print(id(num1))
print(id(num2))

list1=[5,10]
list2=[5,10]
print(id(list1))
print(id(list2))

print(isinstance(num1,int))
print(isinstance(list1,list))
print(isinstance(list1[0],int))
print(isinstance([10,20],list))