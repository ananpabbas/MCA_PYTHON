list=['1','2','3','4','5','6','7']
len=len(list)
temp=list[0]
list[0]=list[len-1]
list[len-1]=temp
print(list)
