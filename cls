[1mdiff --git a/src/main.py b/src/main.py[m
[1mindex d58c530..9c06933 100644[m
[1m--- a/src/main.py[m
[1m+++ b/src/main.py[m
[36m@@ -1,5 +1,7 @@[m
 """Módulo responsável pelo gerenciamento e análise de cadastro de pessoas."""[m
 [m
[32m+[m[32mfrom cadastro import CadastroPessoas[m
[32m+[m
 def exibir_menu():[m
     """Exibe o menu de opções e retorna a escolha do usuário."""[m
     print("=========================")[m
[36m@@ -13,151 +15,140 @@[m [mdef exibir_menu():[m
     print("6 - Sair")[m
     return int(input("Escolha uma opcao: "))[m
 [m
[31m-def cadastrar_pessoa(nomes, idades, emails):[m
[31m-    """Cadastra uma nova pessoa adicionando dados às listas."""[m
[32m+[m[32mdef cadastrar_pessoa(cadastro):[m
[32m+[m[32m    """Cadastra uma nova pessoa."""[m
     nome = input("Informe o nome: ")[m
[31m-    nomes.append(nome)[m
     idade = int(input("Informe a idade: "))[m
[31m-    idades.append(idade)[m
     email = input("Informe o email: ")[m
[31m-    emails.append(email)[m
[32m+[m
[32m+[m[32m    cadastro.cadastrar(nome, idade, email)[m
[32m+[m
     if idade >= 18:[m
         print("Situação: Maior de idade.")[m
     else:[m
         print("Situação: Menor de idade.")[m
 [m
[31m-def buscar_pessoa(nome_busca, nomes):[m
[31m-    """Procura uma pessoa na lista e retorna seu índice ou -1."""[m
[31m-    pos = 0[m
[31m-    while pos < len(nomes):[m
[31m-        if nomes[pos] == nome_busca:[m
[31m-            return pos[m
[31m-        pos += 1[m
[31m-    return -1[m
[31m-[m
[31m-def exibir_pessoa(pos, nomes, idades, emails):[m
[32m+[m[32mdef exibir_pessoa(pessoa):[m
     """Exibe os dados detalhados de uma pessoa no índice especificado."""[m
[31m-    print("Nome: " + nomes[pos])[m
[31m-    print("Idade: " + str(idades[pos]))[m
[31m-    print("E-mail: " + emails[pos])[m
[32m+[m[32m    print("Nome: " + pessoa.getNome())[m
[32m+[m[32m    print("Idade: " + str(pessoa.getIdade()))[m
[32m+[m[32m    print("E-mail: " + pessoa.getEmail())[m
[32m+[m[32m    if pessoa.getIdade() >= 18:[m
[32m+[m[32m        print("Situação: Maior de idade.")[m
[32m+[m[32m    else:[m
[32m+[m[32m        print("Situação: Menor de idade.")[m
 [m
[31m-def consultar_pessoa(nomes, idades, emails):[m
[32m+[m[32mdef consultar_pessoa(cadastro):[m
     """Solicita um nome e exibe as informações caso encontrado."""[m
[31m-    nome_busca = input("Nome para consultar: ")[m
[31m-    pos = buscar_pessoa(nome_busca, nomes)[m
[31m-    if pos != -1:[m
[31m-        exibir_pessoa(pos, nomes, idades, emails)[m
[32m+[m[32m    procurando = input("Nome para consultar: ")[m
[32m+[m[32m    pessoa = cadastro.buscarPorNome(procurando)[m
[32m+[m
[32m+[m[32m    if pessoa is None:[m
[32m+[m[32m        print("Não encontrado")[m
     else:[m
[31m-        print("Usuário não encontrado")[m
[32m+[m[32m        exibir_pessoa(pessoa)[m
 [m
[31m-def alterar_pessoa(nomes, idades, emails):[m
[32m+[m[32mdef alterar_pessoa(cadastro):[m
     """Atualiza as informações de uma pessoa existente."""[m
[31m-    nome_alterar = input("Nome para alterar: ")[m
[31m-    pos = buscar_pessoa(nome_alterar, nomes)[m
[31m-    if pos != -1:[m
[31m-        nomes[pos] = input("Informe o novo nome: ")[m
[31m-        idades[pos] = int(input("Informe a nova idade: "))[m
[31m-        emails[pos] = input("Informe o novo email: ")[m
[31m-    else:[m
[31m-        print("Usuário não encontrado")[m
[32m+[m[32m    procurado = input("Nome para alterar: ")[m
[32m+[m[32m    pessoa = cadastro.buscarPorNome(procurado)[m
 [m
[31m-def listar_pessoas(nomes, idades, emails):[m
[32m+[m[32m    if pessoa is None:[m
[32m+[m[32m        print("Não encontrado")[m
[32m+[m[32m    else:[m
[32m+[m[32m        novo_nome = input("Novo nome: ")[m
[32m+[m[32m        nova_idade = int(input("Nova idade: "))[m
[32m+[m[32m        novo_email = input("Novo email: ")[m
[32m+[m[32m        cadastro.alterar([m
[32m+[m[32m            procurado,[m
[32m+[m[32m            novo_nome,[m
[32m+[m[32m            nova_idade,[m
[32m+[m[32m            novo_email[m
[32m+[m[32m        )[m
[32m+[m
[32m+[m[32m        print("Pessoa alterada!")[m
[32m+[m[32m        exibir_pessoa(pessoa)[m
[32m+[m
[32m+[m[32mdef listar_pessoas(cadastro):[m
     """Listagem completa das pessoas cadastradas."""[m
[31m-    pos = 0[m
[31m-    print("\nPessoas Cadastradas: ")[m
[31m-    while pos < len(nomes):[m
[31m-        exibir_pessoa(pos, nomes, idades, emails)[m
[31m-        print("-" * 30)[m
[31m-        pos += 1[m
[31m-[m
[31m-def classificar_faixa_etaria(idade):[m
[32m+[m[32m    pessoas = cadastro.listar()[m
[32m+[m
[32m+[m[32m    if len(pessoas) == 0:[m
[32m+[m[32m        print("Nenhuma pessoa cadastrada.")[m
[32m+[m
[32m+[m[32m    for pessoa in pessoas:[m
[32m+[m[32m        exibir_pessoa(pessoa)[m
[32m+[m[32m        print("--------------------")[m
[32m+[m
[32m+[m[32m    print("Total: " + str(len(pessoas)))[m
[32m+[m[41m    [m
[32m+[m[32mdef analisar_faixa_etaria(idade):[m
     """Classifica a faixa etária conforme a idade."""[m
     if idade < 12:[m
[31m-        return "Criança"[m
[31m-    if idade < 18:[m
[31m-        return "Adolescente"[m
[31m-    if idade < 30:[m
[31m-        return "Adulto Jovem"[m
[31m-    if idade < 60:[m
[31m-        return "Adulto"[m
[31m-    return "Idoso"[m
[31m-[m
[31m-def avaliar_email(email):[m
[32m+[m[32m        print("Faixa etaria: Criança")[m
[32m+[m[32m    elif idade < 18:[m
[32m+[m[32m        print("Faixa etaria: Adolescente")[m
[32m+[m[32m    elif idade < 60:[m
[32m+[m[32m        print("Faixa etaria: Adulto")[m
[32m+[m[32m    else:[m
[32m+[m[32m        print("Faixa etaria: Idoso")[m
[32m+[m
[32m+[m[32mdef analisar_contato(idade, email):[m
     """Verifica a validade do endereço de e-mail."""[m
[31m-    if email == "":[m
[31m-        return "Cadastro Incompleto: Sem o E-mail"[m
[31m-    if "@" not in email:[m
[31m-        return "E-mail inválido"[m
[31m-    return "E-mail utilizável"[m
[32m+[m[32m    if idade >= 18 and "@" in email:[m
[32m+[m[32m        print("Contato: Completo")[m
[32m+[m[32m    elif idade >= 18:[m
[32m+[m[32m        print("Contato: E-mail invalido")[m
[32m+[m[32m    else:[m
[32m+[m[32m        print("Contato: Menor de idade")[m
 [m
[31m-def identificar_provedor(email):[m
[32m+[m[32mdef analisar_email(email):[m
     """Identifica o provedor do serviço de e-mail."""[m
[31m-    if email.endswith("@gmail.com"):[m
[31m-        return "Gmail"[m
[31m-    if email.endswith("@outlook.com"):[m
[31m-        return "Outlook"[m
[31m-    if email.endswith("@hotmail.com"):[m
[31m-        return "Hotmail"[m
[31m-    if email.endswith("@utfpr.edu.br"):[m
[31m-        return "UTFPR"[m
[31m-    return "Outro"[m
[31m-[m
[31m-def definir_condicao_contato(idade, email):[m
[31m-    """Determina a aptidão para contato conforme idade e presença de e-mail."""[m
[31m-    if idade >= 18 and email != "":[m
[31m-        return "Cadastro apto para contato"[m
[31m-    if idade >= 18 and email == "":[m
[31m-        return "Maior de idade sem contato"[m
[31m-    if idade < 18 and email != "":[m
[31m-        return "Menor de idade com contato"[m
[31m-    return "Menor de idade sem contato"[m
[31m-[m
[31m-def analisar_pessoa(nomes, idades, emails):[m
[32m+[m[32m    if "@" not in email:[m
[32m+[m[32m        print("E-mail inválido")[m
[32m+[m[32m    elif email.endswith("@gmail.com"):[m
[32m+[m[32m        print("Provedor: Gmail")[m
[32m+[m[32m    elif email.endswith("@outlook.com"):[m
[32m+[m[32m        print("Provedor: Outlook")[m
[32m+[m[32m    else:[m
[32m+[m[32m        print("Provedor: Outro")[m
[32m+[m
[32m+[m[32mdef analisar_pessoa(cadastro):[m
     """Executa a análise detalhada dos dados de uma pessoa."""[m
[31m-    procurando = input("Nome para analisar: ")[m
[31m-    pos = buscar_pessoa(procurando, nomes)[m
[31m-    if pos == -1:[m
[32m+[m[32m    procurado = input("Nome para analisar: ")[m
[32m+[m[32m    pessoa = cadastro.buscarPorNome(procurado)[m
[32m+[m
[32m+[m[32m    if pessoa is None:[m
         print("Pessoa não encontrada")[m
[32m+[m[32m    else:[m
[32m+[m[32m        analisar_faixa_etaria(pessoa.getIdade())[m
[32m+[m[32m        analisar_email(pessoa.getEmail())[m
[32m+[m[32m        analisar_contato([m
[32m+[m[32m            pessoa.getIdade(),[m
[32m+[m[32m            pessoa.getEmail()[m
[32m+[m[32m        )[m
         return[m
 [m
[31m-    idade = idades[pos][m
[31m-    email = emails[pos][m
[31m-[m
[31m-    faixa_etaria = classificar_faixa_etaria(idade)[m
[31m-    print(f"Faixa etária: {faixa_etaria}")[m
[31m-[m
[31m-    status_email = avaliar_email(email)[m
[31m-    print(status_email)[m
[31m-[m
[31m-    provedor = identificar_provedor(email)[m
[31m-    print(f"Provedor: {provedor}")[m
[32m+[m[32mcadastro = CadastroPessoas()[m
 [m
[31m-    condicao_contato = definir_condicao_contato(idade, email)[m
[31m-    print(condicao_contato)[m
[32m+[m[32mOP = 0[m
 [m
[31m-if __name__ == "__main__":[m
[31m-    lista_nomes = [][m
[31m-    lista_idades = [][m
[31m-    lista_emails = [][m
[32m+[m[32mwhile OP != 6:[m
[32m+[m[32m    OP = exibir_menu()[m
 [m
[31m-    OP = 0[m
[31m-[m
[31m-    while OP != 6:[m
[31m-        OP = exibir_menu()[m
[31m-[m
[31m-        if OP == 1:[m
[31m-            cadastrar_pessoa(lista_nomes, lista_idades, lista_emails)[m
[31m-        elif OP == 2:[m
[31m-            consultar_pessoa(lista_nomes, lista_idades, lista_emails)[m
[31m-        elif OP == 3:[m
[31m-            alterar_pessoa(lista_nomes, lista_idades, lista_emails)[m
[31m-        elif OP == 4:[m
[31m-            listar_pessoas(lista_nomes, lista_idades, lista_emails)[m
[31m-        elif OP == 5:[m
[31m-            analisar_pessoa(lista_nomes, lista_idades, lista_emails)[m
[31m-        elif OP == 6:[m
[32m+[m[32m    if OP == 1:[m
[32m+[m[32m            cadastrar_pessoa(cadastro)[m
[32m+[m[32m    elif OP == 2:[m
[32m+[m[32m            consultar_pessoa(cadastro)[m
[32m+[m[32m    elif OP == 3:[m
[32m+[m[32m            alterar_pessoa(cadastro)[m
[32m+[m[32m    elif OP == 4:[m
[32m+[m[32m            listar_pessoas(cadastro)[m
[32m+[m[32m    elif OP == 5:[m
[32m+[m[32m            analisar_pessoa(cadastro)[m
[32m+[m[32m    elif OP == 6:[m
             print("Saindo...")[m
[31m-        else:[m
[32m+[m[32m    else:[m
             print("Opcao invalidaa")[m
 [m
     print("Fim do programa")[m
[1mdiff --git a/src/pessoa.py b/src/pessoa.py[m
[1mindex 12bf57f..e24604a 100644[m
[1m--- a/src/pessoa.py[m
[1m+++ b/src/pessoa.py[m
[36m@@ -2,24 +2,24 @@[m
 class Pessoa:[m
     """"Definição de metodos de acesso e modificadores de atributos da classe Pessoa."""[m
     def __init__(self, nome, idade, email):[m
[31m-        self._nome = nome[m
[31m-        self._idade = idade[m
[31m-        self._email = email[m
[32m+[m[32m        self.__nome = nome[m
[32m+[m[32m        self.__idade = idade[m
[32m+[m[32m        self.__email = email[m
 [m
     def getNome(self):[m
[31m-        return self._nome[m
[32m+[m[32m        return self.__nome[m
 [m
     def getIdade(self):[m
[31m-        return self._idade[m
[32m+[m[32m        return self.__idade[m
 [m
     def getEmail(self):[m
[31m-        return self._email[m
[32m+[m[32m        return self.__email[m
 [m
     def setNome(self, nome):[m
[31m-        self._nome = nome[m
[32m+[m[32m        self.__nome = nome[m
 [m
     def setIdade(self, idade):[m
[31m-        self._idade = idade[m
[32m+[m[32m        self.__idade = idade[m
 [m
     def setEmail(self, email):[m
[31m-        self._email = email[m
[32m+[m[32m        self.__email = email[m
