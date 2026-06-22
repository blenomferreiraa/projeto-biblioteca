# Sistema de Biblioteca em Python

Este projeto é um sistema simples de gerenciamento de biblioteca desenvolvido em Python.

O objetivo principal deste projeto é validar, na prática, os conhecimentos adquiridos até o momento no curso de Python. Ele não foi criado como um sistema profissional ou definitivo, mas como um exercício de consolidação dos conceitos estudados, incluindo lógica de programação, estruturas de dados, funções, modularização e programação orientada a objetos.

## Objetivo do Projeto

O sistema simula uma biblioteca onde é possível cadastrar livros, cadastrar usuários, buscar registros, editar informações, excluir dados e controlar empréstimos e devoluções.

Todo o funcionamento acontece em memória durante a execução do programa. Ou seja, os dados cadastrados não são salvos em banco de dados ou arquivo externo quando o programa é encerrado.

## Funcionalidades

O menu principal permite executar as seguintes ações:

1. Cadastrar livro
2. Buscar livro
3. Editar livro
4. Excluir livro
5. Emprestar livro
6. Devolver livro
7. Cadastrar usuário
8. Buscar usuário
9. Editar usuário
10. Excluir usuário
11. Sair do sistema

## Funcionalidades de Livros

O sistema permite cadastrar livros com as seguintes informações:

- Título
- Autor
- Categoria
- Faixa etária
- Status de disponibilidade
- ID gerado automaticamente

Também é possível:

- Buscar um livro pelo título
- Listar livros cadastrados
- Editar título, autor, categoria e faixa etária
- Excluir livros disponíveis
- Impedir a exclusão de livros emprestados
- Controlar o status de empréstimo e devolução

## Funcionalidades de Usuários

O sistema permite cadastrar usuários com:

- Nome
- Idade
- ID gerado automaticamente
- Lista de livros emprestados

Também é possível:

- Buscar usuário pelo nome
- Exibir informações do usuário
- Editar nome e idade
- Excluir usuários sem livros emprestados
- Impedir a exclusão de usuários que ainda possuem livros emprestados
- Registrar livros pegos e devolvidos pelo usuário

## Regras de Empréstimo

O sistema possui regras básicas para empréstimo de livros:

- O livro precisa existir no cadastro
- O usuário precisa existir no cadastro
- O livro precisa estar disponível
- Livros com faixa etária adulta exigem usuário com pelo menos 18 anos
- Livros classificados como jovem exigem idade mínima definida no código
- Ao emprestar, o livro fica indisponível
- Ao devolver, o livro volta a ficar disponível

## Estrutura do Projeto

```text
Biblioteca/
├── main.py
└── dependencias/
    ├── biblioteca.py
    ├── livro.py
    └── usuario.py
```

### `main.py`

Arquivo principal do programa.

Responsável por:

- Exibir o menu no terminal
- Ler a opção escolhida pelo usuário
- Validar entradas principais
- Chamar os métodos da classe `Biblioteca`
- Controlar o loop principal do sistema

### `dependencias/biblioteca.py`

Contém a classe `Biblioteca`.

Responsável por:

- Armazenar a lista de livros
- Armazenar a lista de usuários
- Cadastrar, buscar, editar, listar e excluir livros
- Cadastrar, buscar, editar, listar e excluir usuários
- Controlar empréstimos e devoluções
- Aplicar regras de negócio da biblioteca

### `dependencias/livro.py`

Contém a classe `Livro`.

Responsável por representar um livro no sistema, com atributos como:

- ID
- Título
- Autor
- Categoria
- Faixa etária
- Disponibilidade

Também possui métodos para editar informações, emprestar e devolver o livro.

### `dependencias/usuario.py`

Contém a classe `Usuario`.

Responsável por representar um usuário da biblioteca, com atributos como:

- ID
- Nome
- Idade
- Lista de empréstimos

Também possui métodos para editar dados, pegar livros emprestados e entregar livros.

## Bibliotecas Utilizadas

Este projeto utiliza apenas recursos da biblioteca padrão do Python.

### `itertools`

A biblioteca `itertools` é utilizada nas classes `Livro` e `Usuario` para gerar IDs automáticos com `itertools.count()`.

Exemplo de uso no projeto:

```python
id_livro = itertools.count(start=1)
```

Esse recurso permite criar uma sequência automática de números para identificar livros e usuários.

## Conceitos de Python Praticados

Este projeto foi desenvolvido para praticar conceitos estudados no curso, como:

- Strings
- Números inteiros
- Listas
- Estruturas condicionais com `if`, `elif` e `else`
- Tratamento de erros com `try` e `except`
- Funções e métodos
- Formatação de strings com f-strings
- Manipulação de strings com métodos como `title()`, `strip()`, `lower()`, `replace()`, `isalnum()` e `isalpha()`
- Loops `while` e `for`
- Uso de listas para armazenar objetos
- Iteração em listas
- Funções como `len()`
- Classes
- Objetos
- Métodos
- Encapsulamento básico com atributos protegidos por `_`
- Uso de `@property`
- Modularização com arquivos separados
- Importação de classes entre módulos

## Observações Importantes

Este projeto foi feito apenas para validar os conhecimentos adquiridos até o momento no curso de Python.

Por esse motivo, algumas escolhas foram mantidas simples de propósito, como:

- Uso do terminal como interface
- Dados armazenados apenas em memória
- Ausência de banco de dados
- Ausência de interface gráfica
- Ausência de testes automatizados
- Ausência de bibliotecas externas

Essas limitações fazem parte do escopo atual do estudo e podem ser evoluídas futuramente conforme novos conteúdos forem aprendidos.

## Possíveis Melhorias Futuras

Algumas melhorias possíveis para versões futuras incluem:

- Salvar dados em arquivos `.txt`, `.json` ou `.csv`
- Utilizar banco de dados
- Criar testes automatizados
- Melhorar a organização das validações
- Criar uma interface gráfica
- Adicionar relatórios
- Utilizar Pandas para análise de dados da biblioteca
- Aplicar herança entre classes, se fizer sentido para a evolução do projeto
- Criar métodos setters com `@property.setter`
- Usar dicionários para organizar buscas e registros

## Como Executar

Para executar o projeto, abra o terminal na pasta principal do projeto e rode:

```bash
python main.py
```

Em seguida, utilize o menu exibido no terminal para navegar pelas funcionalidades.

## Status do Projeto

Projeto em desenvolvimento para fins de estudo e validação de aprendizado.
