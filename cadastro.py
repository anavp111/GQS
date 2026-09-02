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

nomes = []
idades = []
emails = []
 
op = 0

while op != 5:
    op = exibir_menu()
 
    if op == 1:
        cadastrar_pessoa(nomes, idades, emails)
    
    elif op == 2:
        nome_busca = input("Nome para consultar: ")
        pos = 0
        achou = 0
        while pos < len(nomes):
            if nome_busca == nomes[pos]:
                print("Nome: " + nomes[pos])
                print("Idade: " + str(idades[pos]))
                print("E-mail: " + emails[pos])
                achou = 1
            pos = pos + 1
        if achou == 0:
            print("Usuário não encontrado")
    elif op == 3:
        nome_alterar = input("Nome para alterar: ")
        pos = 0
        achou = 0
        while pos < len(nomes):
            if nome_alterar == nomes[pos]:
                nomes[pos] = input("Informe o novo nome: ")
                idades[pos] = int(input("Informe a nova idade: "))
                emails[pos] = input("Informe o novo email: ")
                achou = 1
            pos = pos + 1
        if achou == 0:
            print("Usuário não encontrado")

    elif op == 4:
        pos = 0
        while pos < len(nomes):
            print("Nome: " + nomes[pos])
            print("Idade: " + str(idades[pos]))
            print("E-mail: " + emails[pos])
            pos = pos + 1
    elif op == 5:
        print("Saindo...")
 
    else:
        print("Opcao invalida")
 
print("Fim do programa")