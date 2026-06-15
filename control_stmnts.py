# for loop
"""for variable in sequence: #to iterare a sequence
    code to be executed""" 

"""word=input("enter a word: ")
for letter in word:
    print(letter,end="")

for element in [1,2,3,4]:
    print(element)"""

#using range()

for variable in range(start,stop,skip):
    code to be executed

for item in range(11):
    print(item)

for element in range(5,16):
    print(element)

for element in range (10,26,5):
    print(element) 

for element in range(10,1,-1):
    print(element)

for element in range(17,3,-3):
    print(element)

number=int(input("enter a number:"))
i=0
for i in range(1,11):
    print(i,"*",number,"=",number*i)
    print(f"{i} * {number} = {number * i}")'''

# while loop
'''
while condition:
    condition to be executed 

value=1
while value<=10:
    print(value)
    value+=1 


value =1
sum=0
iterations =int(input("enter the no.of iterations: ")) 
while value<=iterations:
    sum += value
    value+= 1
print(sum) 

#reverse number
num=int(input("enter a number to be reversed : "))
reverse=0
while num>0:
    reminder=num%10
    reverse=reverse*10+reminder
    num//=10
print(reverse) '''
'''

number=165
165>0 is true
reminder =165%10 is 5
reverse=0*10+5=5
number=165//10=16
still number 16 is greater than 0

number =16
16>0 is true
reminder=16%10 is 6
reverse=5*10+6=56
number=16//10=1

number=1 
1>0 is true
reminder=1&10=1
reverse=56*10+1=561
number=1//10=0
exist while

#number of 9's from 1 to 100
count=0
for number in range(1,101):
    temp=number
    while temp>0:
        digit=temp%10
        if digit == 9:
            count+=1
        temp//=10    
print("total number of counts: ",count)

