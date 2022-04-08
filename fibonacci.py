#fibonacci numbers

n = int(input("enter the number for fibonacci series: "))

#first two terms 
n1 , n2 = 0,1
count = 0

#checking if the number of terms is valid
if n <= 0:
    print("please enter a positive number")

#if there is only one term, return n1
elif n == 1:
        print("fibonacci sequence upto", n, ":")
        print(n1)

#generate fibonacci series
else: 
    print("fibonacci series: ")
    while count < n:
        print(n1)
        nth = n1 + n2
        
        #update values
        n1 = n2
        n2 = nth 
        count += 1