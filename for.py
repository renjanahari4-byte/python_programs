 # Employee Salary Report Generator
total_salary=0
for employee in range(1,6):
    salary=float(input(f"Enter Salary of Employee {employee}:"))
    total_salary+=salary
print("ttotal salary expenditiure",total_salary)

#Student Attendance Counter
present=0
absent=0
for student in range(1,11):
    Attendance=input(f"student {student} attendance (P/A) : ")
    if Attendance=="p":
        present+=1
    else:
        absent+=1
print("total present students : ",present)
print("total absent students : ",absent)

# Supermarket Billing System
total_amount=0
for item in range(1,6):
    price=int(input(f"item {item} price :" ))
    total_amount+=price
print("total bill amount : ",total_amount) 

# Cricket Score Analyzer 

total_runs=0
for ball in range(1,7):
    runs=int(input(f"ball {ball} Runs: "))
    total_runs+=runs
print("total runs scored: ",total_runs) 


#Library Book Collection Counter

total_books=0
for section in range(1,8):
    books=int(input(f"section {section} books: "))
    total_books+=books
print("total books in library : ",total_books)

# Online Exam Marks Calculator

total_marks=0
average_mark=0
for subject in range(1,6):
    mark=int(input(f"subject {subject} marks : "))
    total_marks+=mark
    average_mark=total_marks/subject
print("total mark : ",total_marks)
print("average mark : ",average_mark)

#Daily Temperature Monitor 

highest_temperature=0
for day in range(1,8):
    temparature=int(input(f"day {day} temparature : "))
    if temparature > highest_temperature:
        highest_temperature=temparature
print("highest_temperature : ",highest_temperature,"C")

# Mobile Recharge Collection System 

total_collection=0
for customer in range(1,11):
    recharge=int(input(f"customer {customer} recharge: " ))
    total_collection+=recharge
print("Total Collection: ",total_collection)

#Water Consumption Tracker

total_water=0
for day in range(1,8):
    Consumption=int(input(f"day {day} consumption : "))   
    total_water+=Consumption
print("total water consuption: ",total_water,"liters ")

#  Factory Production Report 

total_production=0
for month in range(1,13):
    Production=int(input(f"month {month} production : "))
    total_production+=Production
print("Total Annual Production: ",total_production,"units")