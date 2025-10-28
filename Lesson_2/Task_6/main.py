# Task 6

age = int(input("Age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
elif age < 100:
    print("Senior")
else:
    print("💀")