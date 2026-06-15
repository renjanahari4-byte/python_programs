
print("Smart Food Ordering and Delivery Management System")
Customer_name=(input("enter the Customer name: "))
mobile_number=int(input("enter the mobile number: "))
food_item_name=(input("enter food item name: "))
quantity=int(input("enter the Quantity: "))
price=int(input("enter price per item: "))
distance=int(input("enter the delivery distance: "))
premium_member=(input("premiunm menber(True/False): "))  

#Calculate Food Amount

def calculate_food_amount(quantity,price):
    total_food_amount=quantity * price
    return (f"quantity: {quantity}\nprice: {price}\ntotal amount :{total_food_amount}")
print(calculate_food_amount(quantity,price))

#Calculate Delivery Charge
distance=int(input("enter the delivery distance: "))
def calculate_delivery_charge(distance): 
    if distance<=5:
        delivery_charge=40
    else:
        delivery_charge=80
    return delivery_charge
print(calculate_delivery_charge(distance))

# Calculate Discount

def calculate_discount(bill_amount, premium_member):
    discount=0
    if premium_member==True and bill_amount>1000:
        discount=150
    return discount
print("dicount",calculate_discount(1200,True))

#Generate Bill 

def generate_bill(**kwargs): 
    print("complete bill summary")
    for key,value in kwargs.items():
     print(f"{key} : {value}")
generate_bill(customer_name="renjana",mobile_number=9207990522,food_item_name="fried rice",quantity=2,price=120,distance=5,premium_member=True)

#Use Positional Arguments 

def calculate_food_amount(quantity,price): 
    total_food_amount=quantity * price
    return total_food_amount
print(calculate_food_amount(2,120)) 

#Use keyword Arguments 

def generate_bill( customer_name, mobile,item):
    print(f"customer name: {customer_name}\nmobile: {mobile}\nitem: {item} ")
name="renjana" 
phone="9207990522"
food_item="fried_rice"
generate_bill( 
    customer_name=name, 
    mobile=phone, 
    item=food_item 
)

#Use Default Arguments

def restaurant_details(name="FoodHub"):
    print(f"restaraunt name: {name}")
restaurant_details("restaraunt")

# Use *args

def add_extra_items(*items): 
    print(f"extra items added {items}")
add_extra_items("burger","fried rice","chilly chicken" )

# Use**kwargs 

def customer_details(**details):
    print(" customer details: ")
    for key,value in details.items():  
        print(f"{key} : {value}")
customer_details(customer_age=20,city="tvm",customer_name="renjana")


def calculate_food_amount(quantity, price):
    food_amount = quantity * price
    return food_amount


def calculate_delivery_charge(distance):
    if distance <= 5:
        delivery_charge = 40
    else:
        delivery_charge = 80

    return delivery_charge


def calculate_discount(bill_amount, premium_member):
    if premium_member == "yes":
        discount = 150
    else:
        discount = 0

    return discount


def calculate_final_bill(food_amount, delivery_charge, discount):
    final_amount = food_amount + delivery_charge - discount
    return final_amount



quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
distance = int(input("Enter delivery distance: "))
premium_member = input("Premium member (yes/no): ")



food_amount = calculate_food_amount(quantity, price)
delivery_charge = calculate_delivery_charge(distance)
discount = calculate_discount(food_amount, premium_member)

final_bill = calculate_final_bill(
    food_amount,
    delivery_charge,
    discount
)


print("Food Amount:", food_amount)
print("Delivery Charge:", delivery_charge)
print("Discount Amount:", discount)
print("Final Bill Amount:", final_bill)

# print() vs return()

def display_offer():
    print("20% Discount Offer Available")

def get_offer():
    return "20% Discount Offer Available"


print("Using print():")
display_offer()

print("Using return:")
offer = get_offer()
print(offer)

# None as Return Value

def search_food(menu, item):
    if item in menu:
        return item
    else:
        return None


menu = ["burger", "pizza", "fried rice", "noodles"]

food = input("Enter food to search: ")

result = search_food(menu, food)

if result == None:
    print("Food not available")
else:
    print("Food found:", result)



# Datatype Verification

quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))
premium_status = bool(input("Premium membership (True/False): "))

print("Quantity datatype:", type(quantity))
print("Price datatype:", type(price))
print("Premium status datatype:", type(premium_status))




# Type Validation using isinstance()

print("Quantity is Integer:", isinstance(quantity, int))
print("Price is Float:", isinstance(price, float))
print("Premium status is Boolean:", isinstance(premium_status, bool))




# Memory Address Verification

food_amount = quantity * price
final_bill_amount = food_amount - 100

print("Food Amount:", food_amount)
print("Final Bill Amount:", final_bill_amount)

print("Food Amount Memory Address:", id(food_amount))
print("Final Bill Amount Memory Address:", id(final_bill_amount))