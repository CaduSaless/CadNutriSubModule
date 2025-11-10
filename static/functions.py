import random
from database.cadastros import cadastros
import sqlite3

def verifica_cpf(n):
    i = n
    n_aux = int(n/10)
    ultimo = i%10
    i = 1
    soma12 = ultimo
    soma11 = 0
    while i < 11:
        soma11 += (n_aux%10)*i
        i += 1
        soma12 += (n_aux%10)*i
        n_aux = int(n_aux/10)
    if soma12%11 == 0 and soma11%11 == 0:
        return True
    
    return False


def formata_cpf(data):
    aux = data.split('.')
    final = aux[2].split('-')
    aux[2] = f'{final[0]}{final[1]}'
    for i in aux:
        if i.isdigit() == False:
            return ''
    final = ''.join(aux)
    return final

#{'nome': 'Carlos Eduardo de Souza Sales', 'CPF': '03973457123', 'genero': 'masculino', 'raca': 'branco', 'etnia': 'Guaicurus', 'nascimento': '2006-11-06', 'escolaridade': 'EM', 'email': 'cadubss2@gmail.com'}

def verifica_user(user):
    try:
        aux = {
        'nome': user['nome'],
        'CPF': user['CPF'],
        'email': user['email'],
        'raca': user['raca'],
        'etnia': user['etnia'],
        'escolaridade': user['escolaridade'],
        'nascimento': user['nascimento'],
        'genero': user['genero']
        }
    except:
        return 0
    return aux

def salva_user(user):
    db = sqlite3.connect('./database/banco_nutri.db')
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO Pessoa (nome, cpf, raca, sexo, escolaridade, email, data_nascimento) VALUES ('{user['nome']}',{user['CPF']},'{user['raca']}','{user['genero']}','{user['escolaridade']}','{user['email']}','{user['nascimento']}')")
    db.commit()
    cursor.execute(f"SELECT id_Pessoa FROM Pessoa WHERE cpf = {user['CPF']}")
    c = cursor.fetchone()
    cursor.execute(f"INSERT INTO Etnia_Pessoa (id_Pessoa, id_Etnia) VALUES ({c[0]},{user['etnia']})")
    db.commit()
    db.close()
    return c[0]


def code_etnia(etnia):
    db = sqlite3.connect('./database/banco_nutri.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT id_Etnia FROM Etnia WHERE nome_Etnia = '{etnia}'")
    c = cursor.fetchone()
    db.close()
    return c[0]

def vetor_etnia():
    db = sqlite3.connect('./database/banco_nutri.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT nome_Etnia FROM Etnia")
    c = cursor.fetchall()
    vetor = []
    for item in c:
        vetor.append(item[0])
    db.close()
    return vetor

def to_dict_user(cod):
    db = sqlite3.connect('./database/banco_nutri.db')
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM Pessoa WHERE id_Pessoa = {cod} ")
    user = cursor.fetchone()
    cursor.execute(f"SELECT id_Etnia FROM Etnia_Pessoa WHERE id_Pessoa = {cod} ")
    etnia = cursor.fetchone()
    cursor.execute(f"SELECT nome_Etnia FROM Etnia WHERE id_Etnia = {etnia[0]} ")
    etnia = cursor.fetchone()
    
    aux = {
        'Código': user[0],
        'nome': user[1],
        'CPF': user[2],
        'raca': user[3],
        'genero': user[4],
        'escolaridade': user[5],
        'email': user[6],
        'nascimento': user[7],
        'etnia': etnia[0]
    }
    print(aux)
    db.close()
    return aux

def add_etnia(nome):
    db = sqlite3.connect('./database/banco_nutri.db')
    cursor = db.cursor()
    cursor.execute(f"INSERT INTO Etnia (nome_Etnia, descricao) VALUES ('{nome}','att')")
    db.commit()
    db.close()