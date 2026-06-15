''' 
def function_name(parameters):
    code to be executed 

def greeting(user_name,age):
    print(f"welcome {user_name} you are {age} years old" )

user_name=input("enter the name:")
age=int(input("enter age:"))
greeting(user_name,age) 

def addition(num1,num2):
    return num1+num2
num1=int(input("enter first number: "))
num2=int(input("enter second number:"))
print(addition(num1,num2)) # result=addition(num1+num2)
# print(result) 

def book_ticket(movie_name,customer_name,seat,ticket_price):
    total=seat*ticket_price
    return (f"{customer_name} booked {seat} tickets for {movie_name}\n total amount= {total}")
print(book_ticket("luca","adithya",3,150)) 

print("\n keyword arguments")
def customer_details(customer_name,customer_age,city):
    print(f" customer name: {customer_name}\n customer age: {customer_age}\n city: {city}")
customer_details(customer_age=20,city="tvm",customer_name="renjana")
#default arguments 

def booking_status(customer_name,status="conformed",screen="screen1"):
    print(f"\n{customer_name}'s booking status {status}: in {screen}")
booking_status("renjana")
booking_status("adhithya","pending","screens")

# multiple argument

def calculate_bill(*ticket_prices): # *args
    print(f"Ticket Prices: {ticket_prices}")
    print(f"total bill: {sum(ticket_prices)}")
calculate_bill(4,6,8,2,1)

# multiple keyword arguments

def passenger_info(**details): # ** keyword argument
    print("pasenger information")
    for key,value in details.items():
     print(f"{key} : {value}")
passenger_info(customer_name="renjana",customer_age=18,destination="tvm",seat=2,payment_status="confirmed")


#built_in functions
print(len("adthithya"))
print(sum([1,2]))
print(max([2,4,6,8,10]))
print(min([1,3,4,5,9]))
print(sorted([9,4,3,2,10]))
print(sorted([9,4,3,2,10],))

languages=["malayalam","English","Hindhi","German"]
print(sorted(languages))
print(sorted(languages,reverse=True))

print(sorted(languages,key=len))
print(sorted(languages,key=len,reverse=True))

#enumerate()

'''LEGB RULE=LOCAL ENCLOSING GLOBAL BUIT_IN''' 

def student_details():
    name="renjana" #local variable
    print("student name: ",name)
student_details()

#global variable
college_name="Emmanuel College Vazhichal"
def display():
    print("college name : ",college_name)
display()

def department():
    department_name="Computer Science" # enclosing variable
    def student():
        print("Department: ",department_name)
    student()
department()

#billing system

tax=50  #global variable
def shopping():
    discount=100  
    def bill():
        amount=1000  
        total_amount=amount-discount+tax
        print(f"Amount: {amount}\nDiscount: {discount}\nTax: {tax}\ntotal_amount: {total_amount}")
    bill()
shopping() 

#factorial of a number

def factorial(num):
    if num==1:
        return 1
    else: 
        return num*factorial(num-1)
print(factorial(5))    

 working 
5*factorial(4)
4*factorial(3)
3*factorial(2)
2*factorial(1)

1*2=2
factorial(2)=2

3*factorial(2) = 3*2=6
4*factorial(3) = 4*6=24
5*factorial(4) =5*24=120

factorial(5)
=5*factorial(4)
=5*(4*factorial(3))
=5*(4*(3*factorial(2)))
=5*(4*(3*(2*factorial(1))))

#direct way
number=int(input("enter a number: "))
factorial=1
for num in range(1,num+1):
    factorial=factorial*num
print(num)

def add(a,b):
    return a+b
print(add(3,4)) 

#lambda() syntax

lambda arguments:expression
    
add=lambda a,b:a+b 
print(add(5,4))

square=lambda num:num*num
print(square(5))

largest=lambda a,b: a if a>b else b
print(largest(2,10))'''































































































