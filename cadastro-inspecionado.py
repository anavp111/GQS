# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

import email
from operator import pos


def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar pessoa")
    print("6 - Sair")

    return int(input("Escolha uma opcao: "))

def cadastrar_pessoa(nomes, idades, emails):
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if idade >= 18:
        print("Situação: Maior de idade.")
    else:
        print("Situação: Menor de idade.")

def buscar_pessoa(nome_busca, nomes):
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_busca:
            return pos
        pos += 1
    return -1

def exibir_pessoa(pos, nomes, idades, emails):
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])

def consultar_pessoa(nomes, idades, emails):
    nome_busca = input("Nome para consultar: ")
    pos = buscar_pessoa(nome_busca, nomes)
    
    if pos != -1:
        exibir_pessoa(pos, nomes, idades, emails)
    else:
        print("Usuário não encontrado")

def alterar_pessoa(nomes, idades, emails):
    nome_alterar = input("Nome para alterar: ")
    pos = buscar_pessoa(nome_alterar, nomes)
    
    if pos != -1:
        nomes[pos] = input("Informe o novo nome: ")
        idades[pos] = int(input("Informe a nova idade: "))
        emails[pos] = input("Informe o novo email: ")
    else:
        print("Usuário não encontrado")

def listar_pessoas(nomes, idades, emails):
    pos = 0
    print("\nPessoas Cadastradas: ")
    while pos < len(nomes):
        exibir_pessoa(pos, nomes, idades, emails)
        print("-" * 30) 
        pos += 1
#----------novos requisitos----------------
def classificar_faixa_etaria(idade):
    if idade < 12:
        return "Criança"
    elif idade < 18:
        return "Adolescente"
    elif idade < 30:
        return "Adulto Jovem"
    elif idade < 60:
        return "Adulto"
    else:
        return "Idoso"

def avaliar_email(email): 
    if email == "":
        return "Cadastro Incompleto: Sem o E-mail"
    elif "@" not in email:
        return "E-mail inválido"
    else:
        return "E-mail utilizável"

def identificar_provedor(email):
    if email.endswith("@gmail.com"):
        return "Gmail"
    elif email.endswith("@outlook.com"):
        return "Outlook"
    elif email.endswith("@hotmail.com"):
        return "Hotmail"
    elif email.endswith("@utfpr.edu.br"):
        return "UTFPR"
    else:
        return "Outro"

def definir_condicao_contato(idade, email):
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    elif idade >= 18 and email == "":
        return "Maior de idade sem contato"
    elif idade < 18 and email != "":
        return "Menor de idade com contato"
    else:
        return "Menor de idade sem contato"

    
def analisar_pessoa(nomes, idades, emails):
    procurando = input("Nome para analisar: ")
    pos = buscar_pessoa(procurando, nomes)

    if pos == -1:
        print("Pessoa não encontrada")
        return

    idade = idades[pos]
    email = emails[pos]

    faixa_etaria = classificar_faixa_etaria(idade)
    print(f"Faixa etária: {faixa_etaria}")

    status_email = avaliar_email(email)
    print(status_email)

    provedor = identificar_provedor(email)
    print(f"Provedor: {provedor}")

    condicao_contato = definir_condicao_contato(idade, email)
    print(condicao_contato)
#---------------------------------------------------------------
nomes = []
idades = []
emails = []

op = 0

while op != 6:
    op = exibir_menu()

    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    
    elif op == 2:
        consultar_pessoa(nomes, idades, emails)

    elif op == 3:
        alterar_pessoa(nomes, idades, emails)

    elif op == 4:
        listar_pessoas(nomes, idades, emails)
            
    elif op == 5:
        analisar_pessoa(nomes, idades, emails)

    elif op == 6:
        print("Saindo...")  

    else:
        print("Opcao invalida")

print("Fim do programa")