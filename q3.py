# 3.Write a python script to print first N natural numbers in reverse order
n=int(input("Enter the number upto you want to print:-"))
for i in range(n,0,-1):
    print(i,end=",")
