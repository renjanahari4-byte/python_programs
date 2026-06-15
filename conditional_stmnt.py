#Smart ATM Authentication system 
stored_pin=1234
balance=6000
pin=int(input("enter the pin: "))
if pin==stored_pin:
    withdrawal_amount=float(input("enter the withdrawal amount: "))
    if balance>=withdrawal_amount:
        print("withdrawal successfull")
        Remaining_balance=balance-withdrawal_amount
        print("remaining balance: ",Remaining_balance)

    else:
        print("insufficient balance")
else:
    print("incorrect password")

#online shopping discount calculator
Purchase_amount=float(input("enter purchase amount: "))
premium_member=(input(" premium member(yes/no): "))

if Purchase_amount<=5000:
    discount=Purchase_amount*0.05
    print("discount applied: ",discount)
else:
    discount=Purchase_amount*0.10
    print("discount applied: ",discount)

final_amount=Purchase_amount-discount

if premium_member=="yes":
    final_amount-=200
print("final_amount: ",final_amount)

#university Admision Eligibilty Checker
higher_secondry_mark=float(input("enter higher secondsry mark: "))
mathematics_percentage=float(input("Enter Mathematics Percentage: "))
Entrance_Exam=float(input("Enter Entrance Exam Score: "))
if (higher_secondry_mark>=65 and
    mathematics_percentage>=60 and
    Entrance_Exam>=70):
    print("admission status: eligible " )
    print("enter the suggested course:computer science ")
else:
    print("not eligible")

#Loan Approval System 
Age=int(input("enter age: "))
salary=float(input("enter salary: "))
credit_score=int(input("enter the credit score: "))
existing_loan=input("existing loan (yes/no):" )
if (Age>=18 and salary>=25000 and credit_score>=700 and existing_loan== "no"):
    print("Approved")
else:
    print("Denied")

#Hospital patient priority system 
Age=int(input("enter age: "))
condition=(input("enter condition (critical/severe/mild): "))
if condition=="critical":
    print("Priority Category: Emergency")
elif condition=="severe":
    print("Priority Category: High Priority")
else:
    print("Priority Category: low Priority")

#employee bonus management system 
service=int(input("Enter Years of Service:"))
performance_rating=(input("Enter Performance Rating: "))
attendance_percentage=int(input("Enter Attendance Percentage "))

salary = float(input("Enter Salary: "))

if (service >= 5 and
    performance_rating == "Excellent" and
    attendance_percentage >= 90):

    bonus_percentage = 20
    bonus_amount = salary * 0.20

    print("Bonus Percentage:", bonus_percentage, "%")
    print("Bonus Amount: ", bonus_amount)

else:
    print("No Bonus")

#smart traffic fine system 

helmet = input("Helmet Worn (yes/no): ")
seatbelt = input("Seatbelt Used (yes/no): ")
speed = input("Speed Limit Violated (yes/no): ")
license = input("Valid License (yes/no): ")

fine = 0

if helmet == "no":
    fine += 500

if seatbelt == "no":
    fine += 500

if speed == "yes":
    fine += 1000

if license == "no":
    fine += 2000

print("Total Fine: ", fine)

# Cinema Ticket Booking System 

age = int(input("Enter Age: "))
seat_type = input("Seat Type (Normal/Premium): ")
day_type = input("Day Type (Weekday/Weekend): ")
student = input("Student (yes/no): ")

if seat_type == "Normal":
    ticket_cost = 200
else:
    ticket_cost = 350

if student == "yes":
    ticket_cost -= 70

print("Final Ticket Cost: ₹", ticket_cost)

# Scholarship Eligibility System

family_income = float(input("Enter Family Income: "))
academic_percentage = float(input("Enter Academic Percentage: "))
attendance_percentage = float(input("Enter Attendance Percentage: "))

if (family_income <= 200000 and
    academic_percentage >= 90 and
    attendance_percentage >= 95):

    print("Scholarship Status: Full Scholarship")

else:
    print("Scholarship Status: Not Eligible")

#Student Performance Analytics System

mark1 = float(input("Enter Mark 1: "))
mark2 = float(input("Enter Mark 2: "))
mark3 = float(input("Enter Mark 3: "))
mark4 = float(input("Enter Mark 4: "))
mark5 = float(input("Enter Mark 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
percentage = total / 5

if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

if percentage >= 40:
    result = "Pass"
    promotion = "Eligible"
else:
    result = "Fail"
    promotion = "Not Eligible"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)
print("Result:", result)
print("Promotion Status:", promotion)