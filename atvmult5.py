list_number = []
for x in range(4):
    list_number.append(int(input("type a number: ")))
for x in range(2):
    list_number.remove(min(list_number))
for x in list_number:
    print(x)
