#conditional sstmnts
#simple if
"""if condition:
    code to be executed
else:
    code to be executed"""

#if-elif-else

"""if condition:
    code to be executed
elif:
    code to be executed
else:
    code to be executed """

#program to check whether a number is +ve or -ve 

num=int(input("enter a number: "))
if num>0:
    print("positive number")
else:
    print("negative number")

#check the word is vowel or consonant

word=input("enter a word: ")
if (word=="a" or word=="i" or word=="e" or word=="o" or word=="u" or word=="A" or  word=="I" or  word=="E" or  word=="O" or  word=="U"):
    print("vowel") 
else:
    print("consonant")

Vowel_check=input("enter a character: ")
if Vowel_check in 'aeiouAEIOU':
    print("vowel")
else:
    print("consonant")
#odd or even
odd_even=int(input("enter a number : "))
if odd_even%2==0:
    print("even number")
else:
    print("odd number")

#age
age=int(input("enter your age: "))
if age<=13:
    print("child")
elif age<18:
    print("teenager")
elif age<=18:
    print("adult")
else:
    print("senior citizen")"""

