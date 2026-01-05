# Lab 06 - Banco de Dados com SQLite3

Este projeto faz parte do **Bootcamp DIO - Back-end com Python** e tem como objetivo praticar o desenvolvimento de **sistemas com persistência de dados** utilizando **SQLite3**, aplicando conceitos como **modelagem de dados**, **relacionamentos entre entidades**, **criação de tabelas**, **inserção de dados** e **consultas**.

O projeto consiste em gerenciar **alunos** e **matérias**, incluindo um relacionamento **muitos-para-muitos** entre eles. Trata-se de um projeto **hands-on**, ideal para consolidar os conceitos de **banco de dados relacional** e **Python**.

---

## 🧩 Desafio

O desafio consiste em **criar uma aplicação em Python** que utilize SQLite para armazenar dados, aplicando o **Repository Pattern** para organizar o código e separar **camadas de acesso ao banco** da **lógica de negócio**.

O sistema deve permitir:

- Criar tabelas para alunos, matérias e a relação entre eles
- Inserir dados nas tabelas
- Consultar alunos, matérias e relacionamentos
- Garantir integridade referencial com **foreign keys**
- Evitar duplicidade de registros

---

## 🗂️ Modelagem de Dados

O projeto utiliza uma **Modelagem de Entidade e Relacionamento (MER)** com as seguintes entidades:

- **Aluno**
  - `id` (PK, autoincrement)
  - `nome`
  - `ra` (registro do aluno, único)
  - `ano_nascimento`
- **Matéria**
  - `id` (PK, autoincrement)
  - `nome`
- **Aluno_Materia** (tabela associativa N:N)
  - `aluno_id` (FK → alunos.id)
  - `materia_id` (FK → materias.id)
  - **Primary Key composta** (`aluno_id`, `materia_id`)

---

## 🛠️ Funcionalidades

### Funcionalidades base:
- Criar tabelas **alunos**, **materias** e **aluno_materia**
- Inserir alunos e matérias
- Vincular alunos às matérias
- Listar alunos, matérias e suas associações

---

### 🔥 Repository Pattern

O código está organizado em **repositórios**, seguindo o **Repository Pattern**:

- `DatabaseConnection` → gerencia a conexão SQLite
- `BaseRepository` → fornece métodos básicos (`execute`, `execute_many`, `get_all`)
- `AlunoRepository` → CRUD de alunos
- `MateriaRepository` → CRUD de matérias
- `AlunoMateriaRepository` → CRUD da relação muitos-para-muitos

Isso garante **separação de responsabilidades**, facilita **testes** e permite evoluir o projeto de forma modular.

---

## 🧠 Conceitos praticados

- Python **sqlite3**
- **Banco de dados relacional**
- **Modelagem de dados**
- Relacionamento **muitos-para-muitos**
- **Chaves primárias e estrangeiras**
- **Repository Pattern**
- Separação de camadas de acesso a dados e lógica de negócio

---

## 🚀 Como executar

1. Clone o repositório:
```bash
git clone https://github.com/alnbastos/labs_python_dio.git
```

2. Acesse o diretório do laboratório:
```bash
cd labs_python_dio/lab06_banco_dados/
```

3. Execute o script principal:
```bash
python main.py
```

4. Observe no console a saída das operações (inserção de alunos, matérias e relacionamentos).

---

## 📌 Observações

- O banco SQLite (`escola.db`) é criado automaticamente no diretório do projeto na primeira execução.
- As tabelas (`alunos`, `materias`, `aluno_materia`) são criadas automaticamente pelo código.
- **Foreign keys** estão ativadas para garantir a integridade referencial entre alunos e matérias.
- A estrutura atual permite **expansão futura**, como adicionar novas entidades, relacionamentos ou consultas mais complexas.
- O código segue o **Repository Pattern**, separando a lógica de acesso ao banco da lógica de negócio, tornando o projeto mais modular e testável.
