
user_input = input("Enter a list of integers separated by spaces: ")

numbers =  user_input.split()

for i in range(len(numbers)):
    if int(numbers[i]) > 100:
       numbers[i]='over'
    
print("list is", numbers)
