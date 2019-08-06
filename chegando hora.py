import datetime
def horachek(cod_hora):
    n = cod_hora
    hora = "HH:MM"
    k = 0
    if len(n) == len(hora) and n[2:3] == hora[2:3]:
       # print (n)
        now = datetime.datetime.strptime(n, "%H:%M")
        k += 1
    if k == 1:
        return n
    try:
        n = input('')
        return n
    except ValueError:
            print ('A entrada digitada é inválida!')
            return (-1)

horaAcesso = input('Digite a hora do acesso no formato HH:MM: ')
if horaAcesso == horachek(horaAcesso):
    print('certo')

