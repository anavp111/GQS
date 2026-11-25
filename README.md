# Cadastro de Pessoas

Aplicacao em Python para cadastrar, consultar, alterar, listar e analisar
pessoas por meio de um menu no terminal.

## Objetivo e organizacao dos arquivos

O objetivo do projeto e praticar a separacao de responsabilidades em um
sistema de cadastro. As principais funcionalidades sao:

- cadastro de nome, idade e e-mail;
- consulta pelo nome;
- alteracao dos dados;
- listagem das pessoas;
- classificacao por faixa etaria e analise do e-mail.

Estrutura do repositorio:

| Caminho | Responsabilidade |
|---|---|
| `src/main.py` | Menu da aplicacao e leitura das informacoes pelo terminal |
| `src/cadastro.py` | Operacoes de cadastro recebidas pela interface |
| `src/pessoa.py` | Entidade Pessoa e seus atributos |
| `src/repositorio_pessoas.py` | Contrato abstrato do repositorio |
| `src/repositorio_pessoas_memoria.py` | Implementacao do repositorio em memoria |
| `tests/test_cadastro.py` | Testes automatizados das operacoes |
| `infra/compose.yaml` | Servicos MySQL principal e replica |
| `requirements.txt` | Dependencias Python utilizadas pelo projeto |
| `pytest.ini` | Configuracao do pytest |
| `contributing.md` | Convencoes e passos de contribuicao |
| `cadastro-inspecionado.py` | Versao historica baseada em listas |

## Requisitos e ambiente Python

- Python 3.9 ou versao Python 3 compativel;
- Docker Engine ou Docker Desktop;
- Docker Compose;
- Git, opcional para obter e versionar o projeto.

Crie um ambiente virtual e instale as dependencias:

```powershell
cd C:\GQS\GQS_forked
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Para executar os testes:

```powershell
python -m pytest
```

## Docker, conteineres e replicacao

O arquivo `infra/compose.yaml` cria dois conteineres MySQL 8.4.13:

| Servico | Funcao | Porta no computador |
|---|---|---|
| `principal` | Banco principal | `127.0.0.1:3307` |
| `replica` | Replica para leitura ou demonstracao | `127.0.0.1:3308` |

Os dados sao preservados em dois volumes Docker:

- `principal-data`;
- `replica-data`.

Inicie a infraestrutura:

```powershell
docker compose -f infra/compose.yaml up -d
```

Confira o estado e os logs:

```powershell
docker compose -f infra/compose.yaml ps
docker compose -f infra/compose.yaml logs -f
```

Pare os conteineres sem excluir os dados:

```powershell
docker compose -f infra/compose.yaml down
```

Para remover tambem os volumes:

```powershell
docker compose -f infra/compose.yaml down -v
```

Os conteineres recebem configuracoes de binlog, GTID e server ID para
replicacao. Entretanto, o Compose nao cria automaticamente um usuario de
replicacao nem executa `CHANGE REPLICATION SOURCE`. A configuracao completa
da replica deve ser realizada por comandos MySQL apos a inicializacao.

Na situacao atual, o Docker disponibiliza a infraestrutura MySQL, mas a
aplicacao Python nao possui codigo de conexao com MySQL.

## Tabela pessoa e variaveis de ambiente

A entidade utilizada pela aplicacao pode ser representada pela seguinte tabela
conceitual:

| Coluna | Tipo sugerido | Descricao |
|---|---|---|
| `id` | `INTEGER` ou `BIGINT`, chave primaria | Identificador unico da pessoa |
| `nome` | `VARCHAR(255)` | Nome da pessoa |
| `idade` | `INTEGER` | Idade da pessoa |
| `email` | `VARCHAR(255)` | Endereco de e-mail |

A classe `Pessoa` representa esta estrutura em tres atributos:

- `nome`;
- `idade`;
- `email`.

No Compose, a unica variavel de ambiente configurada nos dois servicos e:

| Variavel | Servicos | Valor atual | Uso |
|---|---|---|---|
| `MYSQL_ROOT_PASSWORD` | `principal` e `replica` | `root_lab_2026` | Define a senha do usuario root do MySQL |

Os volumes Docker nao fazem parte das variaveis de ambiente. Eles garantem
que os arquivos de dados do MySQL sejam mantidos entre reinicializacoes dos
conteineres.

Importante: `root_lab_2026` e uma senha destinada a ambiente de laboratorio.
Nao use essa senha nem um usuario root em producao.

## Executar e escolher a persistencia

Execute o sistema no terminal:

```powershell
python src/main.py
```

O menu oferece cadastrar, consultar, alterar, listar e analisar pessoas. Na
implementacao atual, `CadastroPessoas` utiliza
`RepositorioPessoasMemoria` por padrao. Os dados existem apenas enquanto o
processo Python permanece aberto e sao perdidos ao encerrar o programa.

A escolha de persistencia pode ser feita pela interface `RepositorioPessoas`:

- memoria: implementacao pronta em `src/repositorio_pessoas_memoria.py`;
- banco de dados: seria implementada em uma nova classe que satisfaz
  `RepositorioPessoas`, usando MySQL e um driver como `mysql-connector-python`
  ou `PyMySQL`.

Exemplo de uso da persistencia em memoria:

```python
from pessoa import Pessoa
from repositorio_pessoas_memoria import RepositorioPessoasMemoria

repositorio = RepositorioPessoasMemoria()
repositorio.cadastrar(Pessoa("Ana", 20, "ana@example.com"))
```
