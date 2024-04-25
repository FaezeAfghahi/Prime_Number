
"""
Detect Prime numbers

"""

num = int(input("please enter your number:"))
count = 0
for i in range (1,num+1):
    if num % i == 0:
        count+=1
if count ==2:
    print("This number is Prime")
else:
    print("This number is not Prime")
    
