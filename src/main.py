"""Módulo responsável pelo gerenciamento e análise de cadastro de pessoas."""

from cadastro import CadastroPessoas

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


def cadastrar_pessoa(instancia_cadastro):
    """Cadastra uma nova pessoa."""
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o email: ")

    instancia_cadastro.cadastrar(nome, idade, email)

    if idade >= 18:
        print("Situação: Maior de idade.")
    else:
        print("Situação: Menor de idade.")


def exibir_pessoa(pessoa):
    """Exibe os dados detalhados de uma pessoa no índice especificado."""
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    if pessoa.getIdade() >= 18:
        print("Situação: Maior de idade.")
    else:
        print("Situação: Menor de idade.")

def consultar_pessoa(instancia_cadastro):
    """Solicita um nome e exibe as informações caso encontrado."""
    procurando = input("Nome para consultar: ")
    pessoa = instancia_cadastro.buscarPorNome(procurando)

    if pessoa is None:
        print("Não encontrado")
    else:
        exibir_pessoa(pessoa)


def alterar_pessoa(instancia_cadastro):
    """Atualiza as informações de uma pessoa existente."""
    procurado = input("Nome para alterar: ")
    pessoa = instancia_cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Não encontrado")
    else:
        novo_nome = input("Novo nome: ")
        nova_idade = int(input("Nova idade: "))
        novo_email = input("Novo email: ")
        instancia_cadastro.alterar(
            procurado,
            novo_nome,
            nova_idade,
            novo_email
        )

        print("Pessoa alterada!")
        exibir_pessoa(pessoa)


def listar_pessoas(instancia_cadastro):
    """Listagem completa das pessoas cadastradas."""
    pessoas = instancia_cadastro.listar()

    if len(pessoas) == 0:
        print("Nenhuma pessoa cadastrada.")

    for pessoa in pessoas:
        exibir_pessoa(pessoa)
        print("--------------------")

    print("Total: " + str(len(pessoas)))


def analisar_faixa_etaria(idade):
    """Classifica a faixa etária conforme a idade."""
    if idade < 12:
        print("Faixa etaria: Criança")
    elif idade < 18:
        print("Faixa etaria: Adolescente")
    elif idade < 60:
        print("Faixa etaria: Adulto")
    else:
        print("Faixa etaria: Idoso")


def analisar_contato(idade, email):
    """Verifica a validade do endereço de e-mail."""
    if idade >= 18 and "@" in email:
        print("Contato: Completo")
    elif idade >= 18:
        print("Contato: E-mail invalido")
    else:
        print("Contato: Menor de idade")


def analisar_email(email):
    """Identifica o provedor do serviço de e-mail."""
    if "@" not in email:
        print("E-mail inválido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    else:
        print("Provedor: Outro")


def analisar_pessoa(instancia_cadastro):
    """Executa a análise detalhada dos dados de uma pessoa."""
    procurado = input("Nome para analisar: ")
    pessoa = instancia_cadastro.buscarPorNome(procurado)

    if pessoa is None:
        print("Pessoa não encontrada")
    else:
        analisar_faixa_etaria(pessoa.getIdade())
        analisar_email(pessoa.getEmail())
        analisar_contato(
            pessoa.getIdade(),
            pessoa.getEmail()
        )

def executar():
    """Executar o menu principal do programa."""
    cadastro = CadastroPessoas()
    op = 0

    while op != 6:
        op = exibir_menu()
        if op == 1:
            cadastrar_pessoa(cadastro)
        elif op == 2:
            consultar_pessoa(cadastro)
        elif op == 3:
            alterar_pessoa(cadastro)
        elif op == 4:
            listar_pessoas(cadastro)
        elif op == 5:
            analisar_pessoa(cadastro)
        elif op == 6:
            print("Saindo...")
        else:
            print("Opcao invalida")
    print("Fim do programa")

if __name__ == "__main__":
    executar()
