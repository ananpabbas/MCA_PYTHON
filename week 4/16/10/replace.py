s=input("enter a string :")
result=s[0]+s[:].replace(s[0],'$')
print(result)
