# Lab 04 - Sistema Bancário Orientado a Objetos em Python

Este projeto faz parte do **Bootcamp DIO - Back-end com Python** e tem como objetivo praticar conceitos de **Programação Orientada a Objetos (POO)**, aplicando **classes, objetos, encapsulamento e abstração** em um sistema bancário simples.

---

## 🧩 Desafio

O desafio consiste em **atualizar a implementação do sistema bancário** (do Lab 01), substituindo o uso de **dicionários e listas simples** por uma modelagem baseada em **objetos**.

Os dados de **clientes, contas bancárias** e **transações** devem ser armazenados em **classes**, seguindo o modelo UML:
![Modelo UML](sistema_bancario_uml.png)

---

## 🛠️ Funcionalidades

### Funções já existentes:
- **Depositar**: realiza um depósito em uma conta bancária e registra a transação no histórico.
- **Sacar**: permite realizar saques, respeitando:
    - Saldo disponível
    - Limite por saque
    - Número máximo de saques diários
- **Exibir extrato**: mostra todas as transações registradas no histórico da conta, bem como o saldo atual.

### Novas funções a serem implementadas:
- **Criar usuário**: cadastra um novo cliente, armazenando informações como CPF, nome, data de nascimento e endereço.  
- **Criar conta corrente**: vincula uma conta bancária a um usuário existente, gerando número de conta e agência automaticamente.

---

## 🧠 Conceitos praticados

- **Programação Orientada a Objetos (POO)**
- Criação e uso de **classes e objetos**
- **Encapsulamento** de dados
- **Herança** e **polimorfismo**
- Uso de **métodos de instância**
- Organização do código seguindo um **modelo UML**
- Separação de responsabilidades entre classes

---

## 🚀 Como executar

1. Clone o repositório:
```bash
   git clone https://github.com/alnbastos/labs_python_dio.git
```

2. Acesse o diretório:
``` bash
    cd labs_python_dio/lab04_sistema_bancario_poo/
```

3. Execute o script:
```bash
    python main.py
```
