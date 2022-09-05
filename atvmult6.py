list_number = []
for x in range(3):
    list_number.append(int(input("type a number: ")))
list_number.remove(max(list_number))
list_number.remove(min(list_number))
print(list_number[0])