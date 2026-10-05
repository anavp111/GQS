# Contribuindo:
   
## Antes de enviar uma alteração   

1-Execute o programa: python src/main.py
2-Confira as mudanças: git status e git diff
3-Execute as análises: pylint src e radon cc src -s
4-Faça um commit com uma mensagem objetiva.   

## Convenções   
- Um commit representa uma alteração verificável.   
- Não inclua dados reais de pessoas no repositório.   
- Registre decisões e resultados relevantes no histórico Git.   

## Antes de iniciar   
Certifique-se de que está trabalhando com a versão atualizada do projeto:   

git switch main
git pull
git status

# Regras para o Pylint:

## 1. Regras de Ouro (Aprova ou Reprova)

* Nota Mínima: Seu código precisa tirar nota 9.0/10.
* Linhas Longas:O limite de caracteres por linha é amplo: 200 caracteres.
* Duplicação:Cuidado com "copia e cola". Apenas 2 linhas idênticas em sequência já acusam duplicidade de código (`min-similarity-lines=2`).

---

## 2. Nomenclatura (Naming Conventions)

* `snake_case`: Variáveis, argumentos, funções, métodos, atributos e nome de arquivos (`meu_modulo.py`).
* `UPPER_CASE`: Constantes globais e constantes dentro de classes (`TAXA_SERVICO = 0.1`).
* `PascalCase`: Apenas para nomes de Classes (`MinhaClasse`).
* Exceções Permitidas: Nomes curtos como `i`, `j`, `k`, `ex`, `Run` e `_` são aceitos. Evite nomes genéricos banidos como `foo`, `bar`, `baz`.

---

## 3. Limites de Complexidade (Seção Design)

Evite funções gigantes e classes sobrecarregadas. Respeite os tetos:

* Argumentos: Máximo 5 por função/método.
* Retornos: Máximo 6 `return` ou `yield` por função.
* Variáveis Locais: Máximo 15 por função.
* Comandos (Statements): Máximo 50 linhas de instrução executável por função.
* Atributos de Classe: Máximo 7 por classe.
* Métodos Públicos: Máximo 20 (e mínimo de 2) por classe.

---

## 4. Estilo e Boas Práticas de Código

* Docstrings: São obrigatórias para funções e classes públicas (se a função não começar com `_`).
* Exceções Genéricas: Nunca capture exceções abertas sem especificar o erro. Evite `except Exception:` ou `except BaseException:`.
* Sem Código na Mesma Linha: Não faça `if cond: retorno` nem `class MinhaClasse: pass` em uma única linha.
* Chamadas de Rede: Todas as chamadas do pacote `requests` (`requests.get`, `requests.post`, etc.) exigem obrigatoriamente o parâmetro `timeout`.
* Atributos em Classes: Defina todos os atributos de instância dentro do `__init__` ou `__post_init__`. Não crie atributos "de surpresa" em outros métodos.