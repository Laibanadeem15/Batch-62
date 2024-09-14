name = input("Enter your name")
print(f"Hello,{name}! Let's explore your favourite number")

numbers = []
for i in range(1, 4):
    num = int(input(f"Enter your{i} favourite number"))
    numbers.append(num)
    num_check_list = []
for num in numbers:
    if num % 2 == 0:
        num_check_list.append("The {num} is even")
    else:
        num_check_list.append("The {num} is odd") 
    print()

for statement in num_check_list:
        print(statement)

        
for num in numbers:
    square = num ** 2
    print(f"The number {num} and its square: ({num}, {square})")

    total_sum = 0
for num in numbers:
    total_sum += num
print(f"Amazing! The sum of your favorite numbers is: {total_sum}")
is_prime == True 
if sum_of_num <= 1: 
    is_prime == False
for x in range (2, sum_of_num):
    if sum_of_num % x == 0: 
        is_prime = False
if is_prime == False:
    print(f"Great job! The number (sum_of_num) is not a prime number.")
else:
  print (f"Wow! The number (sum_of_num) is a prime number.")




