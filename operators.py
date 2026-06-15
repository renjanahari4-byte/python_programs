print("Arithemetic Operator")
price_per_book=500
quantity=25
total_price=price_per_book*quantity
average=price_per_book/quantity
extra_charge=50
final_price=total_price+extra_charge
discount=25
final_price-=discount 
reminder=final_price%quantity
floor_division=final_price//7
sqaured_value=final_price**2
print("price of one book is: ",price_per_book)
print("quantity of books: ",quantity)
print("total price of book: ",total_price)
print("average amnt of the book:",average)
print("extra charge: ",extra_charge)
print("final pp: ",final_price)
print("reminder: ",reminder)
print("floor division: ",floor_division)
print("square value: ",sqaured_value)


print("Assignment Operator")
score=100
score+=50
print(score)
score-=20
print(score)
score*=2
print(score)

print("Logical operator")
username="darsana"
password="kili123"
entered_username=input("enter the  username: ")
entered_password=input("enter the  password: ")
if entered_username==username and entered_password==password:
    print("login successfully")
else:
    print("invalid login")
    
day=input("Enter a day: ")
if day=="saturday" or day=="sunday":
    print("holiday")
else:
    print("working day")

logged_in=True
if not logged_in:
    print("you are not logged_in")
else:
    print("welcome login ")

print("membership operators")
movies=["athiradi","kattalan","love","pretham"]
movie=input("enter the movie: ")
if movie in movies:
    print("movie available ")
else:
    print("movie is not available ")


print("membership operators")
employees=["darsana","aardra","renjana"]
name=input("enter the employee name: ")
if name not in employees:
    print("access denied")
else:
    print("access granted")

print("identity operator")
value1=500
value2=500
print(value1 is value2)
print(value1 == value2)

value3=[100,110,120,130]
value4=[100,110,120,130]
print(value3 is value4)
print(value3 == value4)

languages=["python","java","c++"]
selected_language=languages[0]
print(selected_language is languages[0])
print(selected_language == "python")
print(selected_language is "Django")


list1=[10,20,30]
list2=[10,20,30]
print(list1 is list2)
list3 = list1
print(list1 is list3)

#bitwise operator

a=5
b=3
print(bin(a))
print(bin(b))
print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a<<1)
print(a>>1)






     

