print("PETROL PUMP BILLING SYSTEM")
Customer_name=input("enter the customer name: ")
Vehicle_number=(input("enter the vehicle no: "))
fuel_type=(input("petrol/desiel: "))
liter=float(input("no.of liters filled: "))
price_per_liter=float(input("enter the price per liter: "))
premium_card=(input("did the customer have premium card T/F: "))
premium_card=premium_card=="T"
print("***********************")

total_fuel_amount=liter*price_per_liter
GST=total_fuel_amount*0.05
final_amount=total_fuel_amount+GST
print("total fuel amount: ",total_fuel_amount)
print("GST : ",GST)
print("final amount: ",final_amount)


print("***********************")

final_amount+=0
print(final_amount)
final_amount-=0
print(final_amount)
final_amount*=1
print(final_amount)

print("***********************")

if premium_card and final_amount>3000:
    final_amount-=200

print("***********************")

print(type(Vehicle_number))
print(type(fuel_type))
print(type(liter))
print(type(premium_card))

print("***********************")

isinstance(liter,float)
isinstance(premium_card,str)

print("***********************")

print(id(final_amount))
print(id(total_fuel_amount))

print("***********************")

print("Customer name: ",Customer_name)
print("vehicle name: ",Vehicle_number)
print("fuel type: ",fuel_type)
print("how many liters filled: ",liter)
print("total fuel amount: ",total_fuel_amount)
print("GST : ",GST)
print("premium_card: ",premium_card)
print("final amount: ",final_amount)
