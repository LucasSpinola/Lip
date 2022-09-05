list_number = []
for x in range(4):
    list_number.append(int(input("type a number: ")))
for x in range(2):
    list_number.remove(max(list_number))
print(list_number)
