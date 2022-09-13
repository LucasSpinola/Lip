list = []
n = int(input())
day = 0
for x in range(n):
    list.append(int(input()))
for indice, valor in enumerate(list):
    if valor>sum(list[0:indice]):
        day = indice
if(day!=0): print(f'dia {day}')
else:
    print('não há')
