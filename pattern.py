"""
num = int(input("enter the number of rows: "))
for i in range(1,num+1):
    print("*"*i)
"""

num = int(input("enter the number of rows: "))

    #top to bottom star
for i in range(1,num+1):
    print(" "*(num-i)+"* "*i)
    
    #bottom to top star 
for i in range(num,0,-1):
    print(" "*(num-i)+"* "*i)
"""
    #top to bottom star
for i in range(1,num+1):
    print(" "*(num-i)+"* "*i) """