"""Módulo responsável pelo gerenciamento e análise de cadastro de pessoas."""

def exibir_menu():
    """Exibe o menu de opções e retorna a escolha do usuário."""
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
    """Cadastra uma nova pessoa adicionando dados às listas."""
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
    """Procura uma pessoa na lista e retorna seu índice ou -1."""
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_busca:
            return pos
        pos += 1
    return -1

def exibir_pessoa(pos, nomes, idades, emails):
    """Exibe os dados detalhados de uma pessoa no índice especificado."""
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])

def consultar_pessoa(nomes, idades, emails):
    """Solicita um nome e exibe as informações caso encontrado."""
    nome_busca = input("Nome para consultar: ")
    pos = buscar_pessoa(nome_busca, nomes)
    if pos != -1:
        exibir_pessoa(pos, nomes, idades, emails)
    else:
        print("Usuário não encontrado")

def alterar_pessoa(nomes, idades, emails):
    """Atualiza as informações de uma pessoa existente."""
    nome_alterar = input("Nome para alterar: ")
    pos = buscar_pessoa(nome_alterar, nomes)
    if pos != -1:
        nomes[pos] = input("Informe o novo nome: ")
        idades[pos] = int(input("Informe a nova idade: "))
        emails[pos] = input("Informe o novo email: ")
    else:
        print("Usuário não encontrado")

def listar_pessoas(nomes, idades, emails):
    """Listagem completa das pessoas cadastradas."""
    pos = 0
    print("\nPessoas Cadastradas: ")
    while pos < len(nomes):
        exibir_pessoa(pos, nomes, idades, emails)
        print("-" * 30)
        pos += 1

def classificar_faixa_etaria(idade):
    """Classifica a faixa etária conforme a idade."""
    if idade < 12:
        return "Criança"
    if idade < 18:
        return "Adolescente"
    if idade < 30:
        return "Adulto Jovem"
    if idade < 60:
        return "Adulto"
    return "Idoso"

def avaliar_email(email):
    """Verifica a validade do endereço de e-mail."""
    if email == "":
        return "Cadastro Incompleto: Sem o E-mail"
    if "@" not in email:
        return "E-mail inválido"
    return "E-mail utilizável"

def identificar_provedor(email):
    """Identifica o provedor do serviço de e-mail."""
    if email.endswith("@gmail.com"):
        return "Gmail"
    if email.endswith("@outlook.com"):
        return "Outlook"
    if email.endswith("@hotmail.com"):
        return "Hotmail"
    if email.endswith("@utfpr.edu.br"):
        return "UTFPR"
    return "Outro"

def definir_condicao_contato(idade, email):
    """Determina a aptidão para contato conforme idade e presença de e-mail."""
    if idade >= 18 and email != "":
        return "Cadastro apto para contato"
    if idade >= 18 and email == "":
        return "Maior de idade sem contato"
    if idade < 18 and email != "":
        return "Menor de idade com contato"
    return "Menor de idade sem contato"

def analisar_pessoa(nomes, idades, emails):
    """Executa a análise detalhada dos dados de uma pessoa."""
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

if __name__ == "__main__":
    lista_nomes = []
    lista_idades = []
    lista_emails = []

    OP = 0

    while OP != 6:
        OP = exibir_menu()

        if OP == 1:
            cadastrar_pessoa(lista_nomes, lista_idades, lista_emails)
        elif OP == 2:
            consultar_pessoa(lista_nomes, lista_idades, lista_emails)
        elif OP == 3:
            alterar_pessoa(lista_nomes, lista_idades, lista_emails)
        elif OP == 4:
            listar_pessoas(lista_nomes, lista_idades, lista_emails)
        elif OP == 5:
            analisar_pessoa(lista_nomes, lista_idades, lista_emails)
        elif OP == 6:
            print("Saindo...")
        else:
            print("Opcao invalidaa")

    print("Fim do programa")
