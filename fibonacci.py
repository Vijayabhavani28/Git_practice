num=int(input("enter number:"))
n,n1=0,1
for i in range(1,num+1):
    n2=n+n1
    print(n2)
    n = n1
    n1 = n2
print("fibonacci number is:",n2)