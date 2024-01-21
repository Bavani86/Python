"""
child:age is less than 12
teen ager:age is between 13 to 19
old age:age is between 40 to 60
young age:age is between 20 to 40
"""
#take user input
age=int(input("please enter the age:"))
if age<12:
    print("child")

elif age>13 and age<20:
    print("teen ager")

elif age>20 and age<40:
    print("young age")

elif age>40 and age<60:
    print("old age")