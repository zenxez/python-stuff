# Task 9

input_count = int(input("How many numbers?: "))
num_list = []

for num in range(input_count):
    input_number = int(input("Enter number: "))
    num_list.append(input_number * 2)

print(num_list)