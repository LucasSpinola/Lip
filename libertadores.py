classification_brasileirao = [ 'Palmeiras', 'Flamengo', 'Fluminense', 'Corinthians', 'Athetico-PR', 'Internacional', 'Atlético-MG', 'América-MG', 'Santos', 'Bragantino', 'Goias', 'Fortaleza', 'São Paulo', 'Botafogo', 'Ceará SC', 'Coritiba', 'Cuiabá', 'Avaí', 'Atlético-GO', 'Juventude' ];
list_lowered = classification_brasileirao[-4:];
classification_libertadores = classification_brasileirao[0:6];
time_biggest_name = max(classification_brasileirao, key=len);
list_half = classification_brasileirao[0:10];
list_half_rtrue = classification_brasileirao[20:9:-1];
print(f"List of teams that will go to the série B: {list_lowered}\n");
print(f"Team with the biggest name: {time_biggest_name}\n");
print(f"List of teams that will go to the libertadores: {classification_libertadores}\n");
for n in list_half:
    print(n, "X", list_half_rtrue[list_half.index(n)]);

# lip 