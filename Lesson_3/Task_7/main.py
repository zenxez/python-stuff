# Task 7

password = False

while not password:
    user_input = input("Password: ")
    if user_input == "12345678":
        print("Access granted.")
        password = True
    else:
        print("Wrong password.")
        