n = int(input("type the city: "))
list_cities = []
for x in range(n):
    list_cities.append(input("type the city: "))
list_cities.sort()
for x in list_cities:
    print(x)