list_number_pair = []
n = int(input("type a number: "))
for x in range(n):
    if x % 2 == 0 and x != 0:
        list_number_pair.append(x)
for x in list_number_pair:
    print(x)