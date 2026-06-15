Customer_name=(input("enter the Customer name: "))
food_item_name=(input("enter food item name: "))
quantity=int(input("enter the Quantity: "))
price=int(input("enter price per item: "))
distance=int(input("enter the delivery distance: "))

print(Customer_name,type(Customer_name))
print(quantity,type(quantity))

print(id(Customer_name))
print(id(quantity))

total=price*quantity
if distance<=5:
    delivery_charge=40
else:
    delivery_charge=80
final_amount=delivery_charge+total
print(final_amount)
