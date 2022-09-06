life = "Die"
lifecopy = 'Die' 
life2 = "Life"
life2copy = 'Life'
print(life ==  lifecopy, life2 == life2copy) 
print(life == life2, lifecopy == life2copy)

print(life.lower(), life2.lower(), lifecopy.lower(), life2copy.lower())

v1 = 1;
v2 = 2;
print(v1 == 1, v2 == 2, v1 == 0, v2 == 0) 
print(v1 > 0, v2 > 1, v1 < 0, v2 < 1)
print(v1 >= 0, v2 >=1, v1 <= 0, v2 <=1)

print(f" {life} and {life2}")

list_life = ['Die' , 'Sky']
print(list_life.__contains__("Die"))
print("Die" in list_life)
print("Sky" not in list_life)