# Lab 02 - Melhorando Sistema Bancário utilizando Iteradores, Geradores e Decoradores

Este projeto faz parte do **Bootcamp DIO - Back-end com Python** e evolui o sistema bancário desenvolvido no Lab 01, incorporando conceitos avançados de Python: **decoradores**, **geradores** e **iteradores personalizados**.

O objetivo é aprimorar a arquitetura do sistema, registrar operações automaticamente, facilitar navegação entre contas e permitir a geração de relatórios transacionais.

---

## 🧩 Desafio

Aprimorar o sistema bancário existente utilizando três recursos avançados de Python:

1. **Um decorador para registrar logs de transações**
2. **Um gerador para iterar sobre o histórico da conta**
3. **Um iterador personalizado para percorrer todas as contas do banco**

---

## 🛠️ Funcionalidades

### 🔔 Decorador de Log

Adiciona um **decorador** aplicando às funções de transação. Ele deve:

- Registrar (exibir) a **data e hora** da operação usando `datetime`
- Informar o **tipo de transação**

### 📄 Gerador de Relatórios

Adiciona um **gerador** responsável por percorrer as transações de uma conta.

O gerador deve:

- Permitir **filtro opcional por tipo**  
  (ex.: `"saque"`, `"deposito"`)
- Caso nenhum tipo seja informado: retornar **todas** as transações

### 🔁 Iterador Personalizado – `ContaIterador`

Adiciona um **iterador** capaz de percorrer todas as contas do banco.

Ele deve retornar informações como:

- Número da conta  
- Cliente vinculado  
- Saldo atual  
- Quantidade de transações

---

## 🧠 Conceitos praticados

- **Decoradores**
- Funções de alta ordem  
- **Geradores** com `yield`  
- Implementação de **iteradores personalizados**  
- Organização do código com **POO**  
- Estrutura modular e extensível  

---

## 🚀 Como executar

1. Clone o repositório:
```bash
   git clone https://github.com/alnbastos/labs_python_dio.git
```

2. Acesse o diretório:
``` bash
    cd labs_python_dio/lab02_sistema_bancario_iter_gen_dec/
```

3. Execute o script:
```bash
    python main.py
```