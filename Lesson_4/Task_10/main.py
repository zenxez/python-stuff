# Task 10

list_1 = ["Nika", "Luka", "Ana"]
list_2 = ["Nika", "Saba", "Luka"]
list_3 = list_1 + list_2
common_list = []

for name in list_3:
    if list_3.count(name) > 1:
        common_list.append(name)
        list_3.remove(name)

print(f"List_1 = {list_1}\nList_2 = {list_2}\nCommon: {common_list}")