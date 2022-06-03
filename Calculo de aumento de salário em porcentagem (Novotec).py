print('----Calcule o aumento do Salário----')

val = float(input('Insira o salário atual: ').replace(',','.'))
perc = float(input('Insira a porcentagem de aumento: ').replace(',','.'))

perc = perc/100
valsal = val * perc + val

print('O salário com aumento é R$ %.2f'%valsal)
