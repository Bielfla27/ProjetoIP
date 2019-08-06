import uuid
import hashlib

def Matriculachek(cod_mat):
    acesso = open('Professores.txt', 'r')
    texto = acesso.readlines()
    k = 2
    while k < len(texto):
        n_matricula = ((texto[k])[11:len(texto[k])-1]) #estou pegando o numero da Matricula da lista.
        print (k)
        if cod_mat == n_matricula:
            return True
        k+=3
    return False
    acesso.close()

def check(hashed_password,user_password):
    senha1 = hashed_password
    aa, salt = senha1.split(':')
    return aa == hashlib.sha256(salt.encode()+user_password.encode()).hexdigest()

def Senhachek(cod_mat,cod_senha):
    acesso = open('Professores.txt', 'r')
    a = cod_senha
    texto = acesso.readlines()
    k = 2
    while k < len(texto):
        n_matricula = ((texto[k])[11:len(texto[k])-1]) #estou pegando o numero da Matricula da lista.
        print (k)
        if cod_mat == n_matricula:
            break
        k+=3
    k -= 1
    senha1 = ((texto[k])[7:len(texto[k])-1])
    if check(senha1,a) == True:
        #print("Achei")
        k += len(texto)
        return True

matricula = input('Digite a Matricula: ')
if Matriculachek(matricula) == True:
    senha = input("Digite sua senha: ")
    if Senhachek(matricula,senha) == True:
        print("Senha correta\n")
    else:
        print("senha incorreta")
