# prime number
'''
n=int(input("enter a number : "))
if n<=1:# 0 and 1 are not prime 
    print("not a prime number")
else:
    is_prime=True #Assume the number is prime first
    for i in range (2,n):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print("prime number")
    else:
        print("not a prime")

#try out with count and floor division
# fibanocci series 
num=int(input("Enter the limit "))
a=0
b=1
for i in range (num):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
# palindrome 
num=int(input("enter a number to be reversed : "))
temp=num
reverse=0
while num>0:
    reminder=num%10
    reverse=reverse*10+reminder
    num//=10
if temp==reverse:
    print("palindrome")
else:
    print("not palindrome")

#count number of digits

num=int(input("enter the number"))
count=0
temp=abs(num)
while temp>0:
        count+=1
        temp=temp//10
print(count)

# sum of digits sum=sum+digit
num=int(input("enter the number : "))
temp=abs(num)
sum_digit=0
while temp>0:
    digit=temp%10
    sum_digit+=digit
    temp//=10
print(sum_digit)

#product of number

num = int(input("Enter the number: "))
temp = abs(num)

product_digit = 1

while temp > 0:
    digit = temp % 10
    product_digit *= digit
    temp //= 10

print(product_digit)

# ATM
pin=int(input("enter the pin number: "))
stored_pin=1234
Available_balance=5000
attempts=0
while attempts<3:
    if stored_pin==pin:
        print("pin verified: ")
        while True:
            print("\n1.Balance Check\n2.Withdraw\n3.Deposit\n4.Exit")
            choice=int(input("enter the choice : "))
            if choice==1:
                print(Available_balance) 
            elif choice==2:
                 withdrawal_amount=int(input("enter the withdraawal amount: "))
                 if withdrawal_amount<=Available_balance:
                     Available_balance-=withdrawal_amount
                 else:
                    print("insufficient balance")
            elif choice==3:
                withdrawal_amount=int(input("Amount to be deposited"))
                Available_balance+=withdrawal_amount
                print("Amount deposited succefully")
            elif choice==4:
                print("Thankyou")
                break
            else:
                print("invalid choice")   
        break 
    else:
        attempts+=1
        print("incorrect pin")
else:
    print("account blocked")
#seat availability system
available_seat=47
while available_seat>0:
        print("available seats",available_seat)
        seat=int(input("enter the no.of tickets"))
        if seat<=available_seat:
            available_seat-=seat
            print("booking succesfull")
            remaining_seat=available_seat
            print("remaining seats",remaining_seat)
        else:
            print("sorryy there were no available seats")
        choice=input("do you want to continue (Yes/No): ")
        if choice=="No":
             break
print("Booking is closed")

# electricity code consumption.....
#FizzBuzz
start_value=int(input("enter the start value "))
end_value=int(input("enter the end value "))
for i in range(start_value,end_value):
    if i%3==0 and i%5==0:
        print("fizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#find the largest and smallest number in a list 
numbers=[]
n=int(input("Enter the elements to be inserted "))
for i in range(n):
    num=int(input(f"enter the number {i+1}: "))
    numbers.append(num)
largest=numbers[0]
smallest=numbers[0]
for num in numbers:
    if largest<num:
        largest=num
    if num<smallest:
        smallest=num
print(f"lagest number in the list is {largest}")
print(f"smallest number in the list is {smallest}")'''

'''
10,12,21,3,8
largest=10
small=10
num=10
num=15
10>15 False
10<15
largest=15'''

#separate +ve and -ve numbers from the list

''' "10 20 30 40 50"
using split "10" "20 "30" 

numbers=tuple(map(int,input("Enter The Numbers To Be Inserted : " ).split()))
element=int(input("Enter The Element To Be Count : "))
count=0
for item in numbers:
    if item==element:
        count+=1
print("Tuple Elemnts Are ",numbers)
print(f"Occurence of {element} is : {count}")

input=1 2 3  4 5 6
target =6
output=[1,5][2,4][3,3]


numbers=tuple(map(int,input("Enter The Numbers To Be Inserted : " ).split()))
target=int(input("Enter The Target Sum : "))
for i in range (len(numbers)):
    for j in range(i,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print((numbers[i],numbers[j]))'''

#Reverse a dictionary

data={"a":1,"b":2,"c":3}
reverse_data={}
keys=list(data.keys())
for key in keys[::-1]:
    reverse_data[key]=data[key]
print(reverse_data)





