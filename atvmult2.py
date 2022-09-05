list_names= []
for y in range(3):
    list_names.append(input("type your name: "))
list_size = []
for x in list_names:
    list_size.append(len(x))
print(list_size)