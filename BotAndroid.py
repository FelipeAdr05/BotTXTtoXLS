import pandas as pd

arquivo = open('contactsGoogle.txt', 'r', encoding='utf-8')
lista = []

for i in arquivo.readlines():
    if i[0] == 'T':
        lista.append(i.rstrip('\n')[14:])

df = pd.DataFrame(lista)

df = df.rename({0: 'Telefones'}, axis = 1)

df.to_excel('PlanilhatelefonesAndroid.xlsx')