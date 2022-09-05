list_odd = []
n = int(input("type a number: "))
for x in range(n+1):
    if x % 2 != 0:
        list_odd.append(x)
v1 = int(input("type a number: "))
v2 = int(input("type a number: "))
print(sum(list_odd[v1:v2+1]))
