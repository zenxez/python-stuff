# Task 9

age = int(input("Age: "))
student = input("Are you a student? (yes/no): ")

adult = age >= 18
student = student == "yes"

if adult and student:
    print("Discount 50%")
elif not adult and student:
    print("Discount 25%")
else:
    print("No discount :(")