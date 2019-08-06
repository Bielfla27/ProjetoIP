import datetime
def datachek(cod_data):
    data = cod_data
    a = "aaaaaaaaaa"
    if len(data) == len(a):
        data2 = datetime.datetime.strptime(data, "%d/%m/%Y")
        data2 = '{}/{}/{}'.format(data2.day,data2.month,data2.year)
        if data == data2:
            return data
        elif data < data2:
            return data
    else:
        print("Data invalida")

dataAcesso = input('Digite a data de acesso no formato DD/MM/AAAA: ') #criar uma função para conferir hora
if dataAcesso == datachek(dataAcesso):
    print("achei")
else:
    print("errado")
