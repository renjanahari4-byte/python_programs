#Smart ATM authentication system 
Customer_name=input("enter the customer name: ")
ATM_card_number=int(input("enter the ATM card number: "))
pin_number=int(input("enter the pin number: "))
Account_type=bool(input("the account type is? savings/current? "))
Available_balance = float(input("available balance: "))
withdrawal_amount = float(input("enter withdrawal amount: "))

print("*********************")

#memberintrship operator
valid_Account_types=["savings","current"]
Account_type=input("enter the account type: ")
if Account_type in valid_Account_types:
    print("valid account type")
else:
    print("invalid account type")

print("*********************")

#comparison operators
stored_pin=1234
pin=int(input("enter the pin number: "))
print("pin verified: ",stored_pin==pin)
Available_balance=5000
withdrawal_amount=int(input("enter the withdraawal amount: "))
print("sufficient balance: ",withdrawal_amount<=Available_balance)
print("available balance is greater than zero: ",Available_balance<0)

print("*********************")

# logical operator

if stored_pin==pin and withdrawal_amount<=Available_balance and Account_type in valid_Account_types:
    print("successfull")
else:
    print("failed")

#identity operators
account1=["savings","current"]
account2=["savings","current"]
account2 == account1
print("account1 is account2: ",account1 is account2)#error
account2 == account1
print("account1 is not account2: ",account1 is not account2)#error

print("*********************")

#arithmetic operators

Remaining_balance=Available_balance - withdrawal_amount
print("remaining balance is: ",Remaining_balance)

print("*********************")

#assignment operators

Remaining_balance-=500
print(Remaining_balance)
Remaining_balance+=1000
print(Remaining_balance)
Remaining_balance*=1
print(Remaining_balance)

print("*********************")

#type function
print("datatype of balance: ",type(Available_balance))
print("datatype of customer name: ",type(Customer_name))
print("datatype of pin: ",type(pin))
print("datatype of withdrawal amount: ",type(withdrawal_amount))
print("datatype of account type: ",type(Account_type))

print("*********************")

#isinstance()

print("is available balance is float? ",isinstance(Available_balance,float))
print("is withdrawal amount is float? ",isinstance(withdrawal_amount,float))
print("is customer name is string? ",isinstance(Customer_name,str))


print("*********************")

#id()

print("the memory address of available balance is: ",id(Available_balance))
print("the memory address of remaining balance is: ",id(Remaining_balance))
print("the memory address of account type is: ",id(Account_type))


print("*********************")
