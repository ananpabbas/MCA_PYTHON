y1=int(input("enter a year"))
y2=int(input("enter a year"))
for year in range(y1,y2+1):
    if(year%400==0)or(year%100!=0)and(year%4==0):
      print(year)
