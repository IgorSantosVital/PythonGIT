cont = 0
result= 0
for c in range(1,501,2):
    if c % 3 == 0:
        cont += 1
        result += c
print('A soma de todos os {} valores é {}'.format(cont, result))