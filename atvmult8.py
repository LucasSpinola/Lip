n = int(input("type a number: "))
list_pair = []
for x in range(n):
    if x % 2 == 0 and x != 0:
        list_pair.append(x)
list_pair_copy = list_pair[:]
l1=int(input("type a number: "))
l2=int(input("type a number: "))
list_pair_copy.pop(l1)
list_pair_copy.pop(l2)
print(list_pair)
print(list_pair_copy)