#creating an empty list
my_list = []

#entering the no.of elements in the list
n = int(input("enter the number of elements: "))

#condition
for i in range(0, n):
    #input from the user to create the list
    ele = int(input())
    #adding an element into the list
    my_list.append(ele)
    #printing out the list
print(my_list)

'''
#printing out the positive number from the list 
for num in my_list:
   if num>=0:
       print(num)
'''    

"""
#creating an empty list to store the positive values
list = []
for num in my_list:
    if num>=0:
        #appending the values to the new list
        list.append(num)       
print(list)
"""