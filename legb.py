password=(input("enter the pass word: "))
if (len(password)>=8 and
    ("A" in password or "B" in password or "C" in password or 
     "D" in password or "E" in password) and
    ("0" in password or "1" in password or "2" in password or 
     "3" in password or "4" in password or "5" in password or 
     "6" in password or "7" in password or "8" in password or "9" in password)):
    print("strong password")
elif (len(password))>=6:
    print("medium password")
else:
    print("weak password") 

