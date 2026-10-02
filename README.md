# Python Learning

Repositório com meus estudos de Python, acompanhando as aulas do curso **[Python do zero ao avançado - com projetos reais](https://www.udemy.com/)** da Udemy.

A ideia é registrar, em arquivos pequenos e diretos, os conceitos vistos em cada aula, servindo como material de consulta e revisão.

## Estrutura

```
python_learning/
├── main_entry.py            # Menu interativo para executar os exemplos
├── basics.py                # Fundamentos: input, tipos, operadores e condicionais
├── strings_examples.py      # Manipulação e formatação de strings
├── loops.py                 # while, for, range e o jogo da forca
├── collections_examples.py  # Listas, enumerate e gerenciador de lista de compras
├── functions_examples.py    # Funções, *args e closures
├── lambda.py                # Funções lambda e funções como parâmetro
├── em_des.py                # Empacotamento e desempacotamento
├── list.py                  # List comprehension
├── dictionary.py            # Dicionários: quiz de perguntas e respostas
├── set.py                   # Sets e suas operações
└── questions/
    └── q_1.py               # Exercício: verificar se um número é par ou ímpar
```

## Conteúdo

### Fundamentos

| Arquivo | Assunto |
| --- | --- |
| [`basics.py`](./basics.py) | `input`, conversão de tipos, prioridade de operadores, métodos de verificação de string (`isalpha`, `isnumeric`, ...), calculadora de IMC e comparação de números com `if/else` |
| [`strings_examples.py`](./strings_examples.py) | `len`, fatiamento (`[::-1]`), operador `in`, indexação, códigos de formatação (`s`, `d`, `f`, `x`) e operadores de atribuição (`+=`, `-=`, ...) |
| [`loops.py`](./loops.py) | `while` aninhado, `for` com `range`, `break`/`continue` e um **jogo da forca** |

### Coleções

| Arquivo | Assunto |
| --- | --- |
| [`collections_examples.py`](./collections_examples.py) | Listas, `enumerate`, `append`, `del` e um **gerenciador de lista de compras** |
| [`list.py`](./list.py) | List comprehension: geração de listas com `range`, mapeamento de dicionários, expressões condicionais e filtros |
| [`dictionary.py`](./dictionary.py) | Lista de dicionários, `dict.get` e um **quiz de perguntas e respostas** com placar de acertos e erros |
| [`set.py`](./set.py) | Criação de sets, `add` e operações de união (`\|`), interseção (`&`), diferença (`-`) e diferença simétrica (`^`); exercício de encontrar o primeiro valor repetido em cada linha de uma matriz |

### Funções

| Arquivo | Assunto |
| --- | --- |
| [`functions_examples.py`](./functions_examples.py) | Definição de funções, `return`, `*args`, operador ternário e closures |
| [`lambda.py`](./lambda.py) | Funções `lambda`, ordenação com `sort(key=...)` e funções recebidas como parâmetro |
| [`em_des.py`](./em_des.py) | Empacotamento e desempacotamento: troca de variáveis (`a, b = b, a`), merge de dicionários com `**` e funções com `*args` e `**kwargs` |

### Exercícios

| Arquivo | Enunciado |
| --- | --- |
| [`questions/q_1.py`](./questions/q_1.py) | Pedir um número inteiro ao usuário e informar se é par ou ímpar, repetindo enquanto ele quiser continuar |

## Como executar

Pré-requisito: [Python 3.12+](https://www.python.org/downloads/) (o `dictionary.py` usa aspas duplas dentro de f-strings, recurso disponível a partir dessa versão).

### Menu interativo

O `main_entry.py` reúne os exemplos de `basics.py`, `strings_examples.py`, `loops.py`, `collections_examples.py` e `functions_examples.py` em um menu numerado:

```bash
python main_entry.py
```

### Arquivos individuais

Os demais arquivos podem ser executados diretamente:

```bash
python list.py
python em_des.py
python lambda.py
python set.py
python dictionary.py
python questions/q_1.py
```

## Progresso

- [x] Variáveis, tipos e `input`
- [x] Operadores aritméticos e de atribuição
- [x] Condicionais (`if/elif/else` e ternário)
- [x] Strings: fatiamento, métodos e formatação
- [x] Laços de repetição (`while`, `for`, `range`)
- [x] Listas e `enumerate`
- [x] Dicionários
- [x] Sets
- [x] Funções, `*args`, `**kwargs` e closures
- [x] Empacotamento e desempacotamento
- [x] List comprehension
- [x] Funções `lambda`
- [ ] Próximos tópicos do curso...

## Objetivo

- Consolidar os fundamentos da linguagem
- Evoluir até tópicos avançados
- Construir os projetos reais propostos no curso
