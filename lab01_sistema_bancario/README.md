# Lab 01 - Sistema Bancário com Funções em Python

Este projeto faz parte do **Bootcamp DIO - Back-end com Python** e tem como objetivo praticar conceitos fundamentais de **funções**, **estruturas de dados** e **organização de código** em Python, simulando um sistema bancário simples.

---

## 🧩 Desafio

O desafio consiste em **refatorar** o código desenvolvido em aula, **separando a lógica em funções** específicas.  
As funções devem permitir ao usuário realizar operações bancárias básicas, além de criar e gerenciar contas e usuários.

---

## 🛠️ Funcionalidades

### Funções já existentes:
- **Depositar**: adiciona um valor ao saldo e registra a operação no histórico.  
- **Sacar**: permite retirar um valor do saldo, respeitando limites de saque e número máximo diário.  
- **Exibir extrato (histórico)**: mostra todas as transações realizadas e o saldo atual.

### Novas funções a serem implementadas:
- **Criar usuário**: cadastra um novo cliente, armazenando informações como CPF, nome, data de nascimento e endereço.  
- **Criar conta corrente**: vincula uma conta bancária a um usuário existente, gerando número de conta e agência automaticamente.

---

## 🧠 Conceitos praticados

- Definição e reutilização de **funções**  
- **Listas** e **dicionários** para armazenar dados  
- **Parâmetros e retorno de função**  
- Organização do código em **módulos reutilizáveis**  
- Interação com o usuário via **input() e print()**

---

## 🚀 Como executar

1. Clone o repositório:
```bash
   git clone https://github.com/alnbastos/labs_python_dio.git
```

2. Acesse o diretório:
``` bash
    cd labs_python_dio/lab01_sistema_bancario/
```

3. Execute o script:
```bash
    python main.py
```