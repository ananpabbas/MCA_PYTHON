string=input("enter a string")
if len(string)>1:
    modified_string=string[-1]+string[1:-1]+string[0]
    print(modified_string)
else:
    modified_string=string
    print(modified_string)
