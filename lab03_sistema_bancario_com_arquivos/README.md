# Lab 03 – Persistindo Logs em Arquivo com Decoradores em Python

Este projeto faz parte do **Bootcamp DIO – Back-end com Python** e tem como foco a **evolução do decorador de log**, que anteriormente exibia informações apenas no console.

O objetivo agora é **persistir os logs em arquivo**, permitindo auditoria, rastreabilidade e análise posterior das operações realizadas no sistema.

📌 **Projeto base:**  
https://github.com/digitalinnovationone/trilha-python-dio/blob/main/05%20-%20Manipula%C3%A7%C3%A3o%20de%20arquivos/desafio/desafio_v1.py

---

## 🧩 Desafio

Modificar o decorador de log existente para que, ao invés de apenas imprimir informações no console, ele **registre os dados das operações em um arquivo de log**.

Esse arquivo deve armazenar informações completas sobre cada chamada de função, garantindo histórico persistente das execuções.

---

## 🛠️ Funcionalidades

### 🔔 Decorador de Log Persistente

O decorador deve registrar, para **cada chamada de função**, as seguintes informações:

- 📅 **Data e hora atual** no formato `dd/mm/yyyy HH:MM:SS`
- 🧠 **Nome da função executada**
- 📥 **Argumentos passados** para a função
- 📤 **Valor retornado** pela função
- 📄 Os registros devem ser salvos no arquivo **`log.txt`**
- ➕ Caso o arquivo já exista, os novos logs devem ser **adicionados ao final**
- 📌 Cada registro deve ser gravado em **uma nova linha**

---

## 🧠 Conceitos praticados

- **Decoradores em Python**
- Funções de alta ordem
- Manipulação de arquivos (`open`, `write`, `append`)
- Uso de `datetime` para registro de data e hora
- Boas práticas de logging
- Código limpo e reutilizável

---

## 🚀 Como executar

1. Clone o repositório:
```bash
  git clone https://github.com/alnbastos/labs_python_dio.git
```

2. Acesse o diretório:
``` bash
  cd labs_python_dio/lab03_sistema_bancario_com_arquivos/
```

3. Execute o script:
```bash
  python main.py
```

Após a execução, verifique o arquivo `log.txt` para visualizar os registros das operações realizadas.
