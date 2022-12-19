#7.Write a python script to print first N even natural numbers in reverse order.
n=int(input("enter the value of n:-"))
for i in range (2*n,1,-2):
    print(i, end=",")
