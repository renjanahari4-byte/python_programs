print("PETROL PUMP BILLING SYSTEM")
Customer_name=input("enter the customer name: ")
Vehicle_number=int(input("enter the vehicle no: "))
fuel_type=bool(input("petrol/desiel: "))
liter=float(input("no.of liters filled: "))
price_per_liter=float(input("enter the price per liter: "))
premium_card=bool(input("did the customer have premium card T/F"))

print("***********************")

total_fuel_amount=liter*price_per_liter
GST=total_fuel_amount*0.05
final_amount=total_fuel_amount+GST

print("***********************")

final_amount+=0
final_amount-=0
final_amount*=1

print("***********************")

if premium_card and final_amount>3000:
final_amount-=200

print("***********************")

print(type(Vehicle_number))
print(type(fuel_type))
print(type(liter))
print(type(premium_card))

print("***********************")

isinstance(liter(float))
isinstance(premium_card(bool))

print("***********************")

print(id(final_amount))
print(id(total_fuel_amount))

print("***********************")

print("Customer name: ",Customer_name)
print("vehicle name: ",Vehicle_number)
print("fuel type: ",fuel_type)
print("how many liters filled: ",liter)
print("vehicle name: ",Vehicle_number)
print("total fuel amount: ",total_fuel_amount)
print("vehicle name: ",Vehicle_number)
print("GST : ",GST)
print("final amount: ",final_amount)
