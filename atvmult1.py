n = int(input("enter a number: "))
list_cities = []
for x in range(n):
    list_cities.append(input("enter the city: "))
list_cities.reverse()
for x in list_cities:
    print(x)