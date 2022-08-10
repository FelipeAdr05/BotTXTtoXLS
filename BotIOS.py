import pandas as pd

arquivo = open('contactsIOS.txt', 'r', encoding='utf-8')
lista = []

for i in arquivo.readlines():
    if i[0] == 'T':
        lista.append(i.rstrip('\n')[35:])

df = pd.DataFrame(lista)

df = df.rename({0: 'Telefones'}, axis = 1)

df.to_excel('Planilha_telefones_IOS.xlsx')