# Lab 07 - Banco de Dados com SQLAlchemy

Este projeto faz parte do **Bootcamp DIO - Back-end com Python** e tem como objetivo praticar o uso de **ORM (Object-Relational Mapping)** com **SQLAlchemy**, substituindo o acesso direto via `sqlite3` por uma abordagem mais abstrata, organizada e orientada a objetos.

O foco deste laboratório é compreender como o **SQLAlchemy ORM** mapeia classes Python para tabelas do banco de dados, bem como a definição de **relacionamentos**, **sessões**, **consultas** e **persistência de dados** utilizando SQLite como banco de dados.

---

## 🧩 Descrição do Projeto

O projeto implementa um pequeno sistema de gerenciamento de **usuários** e **endereços**, onde:

- Um **Usuário** pode possuir **vários endereços**
- Cada **Endereço** pertence a apenas **um usuário**

Esse relacionamento é do tipo **um-para-muitos (1:N)** e é modelado diretamente através do SQLAlchemy ORM.

---

## 🗂️ Modelagem de Dados (ORM)

A modelagem é feita por meio de **classes Python**, que representam tabelas no banco de dados.

### Entidades

#### User (`user_account`)
- `id` (PK)
- `name`
- `fullname`

#### Address (`address`)
- `id` (PK, autoincrement)
- `email_address`
- `user_id` (FK → user_account.id)

### Relacionamentos

- `User.addresses` → relacionamento **1:N** com `Address`
- `Address.user` → relacionamento inverso com `User`
- Uso de `back_populates` para navegação bidirecional
- Cascade configurado como `all, delete-orphan`

---

## 🧠 Conceitos praticados

- **SQLAlchemy ORM**
- Mapeamento objeto-relacional (ORM)
- Definição de modelos com `declarative_base`
- Relacionamentos `one-to-many`
- Chaves primárias e estrangeiras
- Sessões (`Session`)
- Criação automática de tabelas com `metadata.create_all`
- Consultas usando `select`, `where`, `order_by` e `join`
- Execução de queries via **Session** e **Connection**

---

## 🛠️ Tecnologias utilizadas

- Python 3
- SQLAlchemy
- SQLite (em memória)

---

## 🚀 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/alnbastos/labs_python_dio.git
```

2. Acesse o diretório do laboratório:
```bash
cd labs_python_dio/lab07_sqlalchemy/
```

3. Instale a dependência (caso necessário):
```bash
poetry install
```

4. Execute o script principal:
```bash
python main.py
```

---

## 📌 Estrutura geral do código
- Definição da base ORM com `declarative_base`
- Criação das classes `User` e `Address`
- Configuração do relacionamento entre as entidades
- Criação do engine SQLite
- Criação automática das tabelas
- Inserção de dados utilizando `Session`
- Consultas com SQLAlchemy Core e ORM
- Exibição dos resultados no console

---

## 📖 Observação
Este laboratório tem caráter **didático**, focado no aprendizado dos principais conceitos do **SQLAlchemy ORM**, servindo como base para projetos maiores que envolvam persistência de dados, relacionamentos complexos e aplicações backend mais robustas.
