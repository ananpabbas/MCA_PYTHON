list1=[1,2,3]
list2=[4,2,3]
if len(list1)==len(list2):
    print("lists are of same length:")
else:
    print("lists are not of same length:")
if sum(list1)==sum(list2):
    print("sum of lists are same")
else:
    print("sum of lists doesnt sum up of to same sum")
x=len(list1)
y=len(list2)
for i in range (x):
    for j in range (y):
        if list1[i]==list2[j]:
            print(list1[i],"occur in both")
        

