# Task 8

has_ticket = input("Do you have ticket? (yes/no): ")
is_vip = input("Are yoy VIP? (yes/no): ")

has_ticket = has_ticket == "yes"
is_vip = is_vip == "yes"

if has_ticket or is_vip:
    print("You can enter.")
else:
    print("You can not enter.")