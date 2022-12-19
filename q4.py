#4.Write a python script to print first N odd natural numbers.
n=int(input("enter natural number:-"))
for i in range (1,n+1,2):
    print(i, end=",")
