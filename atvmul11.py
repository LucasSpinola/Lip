list_number = []
n = int(input("type a number: "))
for x in range(1,n+1):
    list_number.append(x)
list_number_copy = list_number[:]
l1 = int(input("type a number: "))
l2 = int(input("type a number: "))
list_number_copy.remove(l1)
list_number_copy.remove(l2)
print(list_number_copy)
print(list_number)