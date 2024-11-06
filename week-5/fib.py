num= int(input("enter the range for fibonnaci series:"))
a=0
b=1
print(f"{a} {b}",end=" ")
for i in range(3,num+1):
    c=a+b
    print(f"{c}",end=" ")
    a=b
    b=c
                                                                              
