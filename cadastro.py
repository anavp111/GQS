# Sistema de Cadastro de Pessoas - versao 2
# novos requisitos: menu, consulta, alteracao e listagem

def exibir_menu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Sair")
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

def analisar_pessoa(nomes, idades, emails):
    procurando = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurando)

    if pos == -1:
        print("Pessoa não encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

    if idade < 12:
        print("Faixa etária: Criança")
    elif idade < 18:
        print("Faixa etária: Adolescente")  
    elif idade < 30:
        print("Faixa etária: Adulto Jovem")
    elif idade < 60:
        print("Faixa etária: Adulto")
    else:
        print("Faixa etária: Idoso")

    if email == "":
        print("Cadastro Incompleto: Sem o E-mail")
    else:
        if "@" not in email:
            print("E-mail inválido")
        else:
            if email.endswith("@gmail.com"):
                print("Provedor: Gmail")
            elif email.endswith("@outlook.com"):
                print("Provedor: Outlook")
            elif email.endswith("@hotmail.com"):
                print("Provedor: Hotmail")
            elif email.endswith("@utfpr.edu.br"):
                print("Provedor: UTFPR")
            else:
                print("Provedor: Outro")

    if idade >= 18 and email != "":
        print("Cadastro apto para contato")
    elif idade >=18 and email == "":
        print("Maior de idade sem contato")
    elif idade < 18 and email != "":
        print("Menor de idade com contato")
    else:
        print("Menor de idade sem contato")
# ---------------------------------

nomes = []
idades = []
emails = []

op = 0

while op != 5:
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
        print("Saindo...")

    else:
        print("Opcao invalida")

print("Fim do programa")