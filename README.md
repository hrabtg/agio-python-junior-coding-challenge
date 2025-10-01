# 📘 Desafio Técnico – Desenvolvedor Python

## 1. Visão Geral (o fluxo)
Neste desafio, você deverá **consumir duas fontes de transações (APIs)**, cada uma com seu próprio formato de dados.  

Sua tarefa será:  

1. **Consumir** os dados das duas fontes  
2. **Normalizar** as transações em um **formato único**  
3. **Expor um endpoint** que:  
   - Execute as etapas 1 e 2
   - Retorne as transações processadas  
   
>**Observação:** Não é necessário utilizar banco de dados. Todo o processamento deve ocorrer apenas em memória, durante a execução da aplicação.

## 2. Requisitos
- **Consumir** duas APIs com schemas diferentes  
- **Transformar** os dados para um formato unificado (detalhes abaixo)  
- **Criar** um endpoint REST que execute o fluxo e retorne os dados processados  
- **Organizar** o projeto de forma limpa e estruturada (pastas, arquivos, módulos)  
- **Aplicar conceitos de POO** 
> **Dica:** Estruture seu código de forma organizada, utilizando **classes, serviços e mappers** para separar responsabilidades e facilitar a manutenção.

## 3. Fontes de Dados
### 📌Fonte Interna (Internal Transaction Source)  
**Endpoint:**  
`GET https://68dc18d97cd1948060a975d9.mockapi.io/api/internal-transaction-source`  

**Exemplo de resposta:**  
```json
[
  {
    "tradeDate": "2025-09-30T17:30:13.229Z",
    "price": "603.80",
    "amount": "52.10",
    "accountNumber": "46649416",
    "id": "1"
  },
  {
    "tradeDate": "2025-09-29T22:50:41.834Z",
    "price": "10.43",
    "amount": "683.97",
    "accountNumber": "51582115",
    "id": "2"
  }
]
```

### 📌Fonte Externa (External Transaction Source)

**Endpoint:**  
`GET https://68dc18d97cd1948060a975d9.mockapi.io/api/external-transaction-source`

**Exemplo de resposta:**
```json
[
  {
    "date": "2025-09-30T13:38:57.274Z",
    "price": "506.95",
    "quantity": "997.44",
    "account": "86446586",
    "id": "1"
  },
  {
    "date": "2025-09-30T01:28:13.533Z",
    "price": "482.31",
    "quantity": "488.01",
    "account": "28634899",
    "id": "2"
  }
]
```

## 4. Schema Unificado (formato final)
Cada transação deve ser transformada no seguinte schema:

```json
{
  "id": "uuid",
  "date": "Date ISO 8601",
  "price": "decimal",
  "quantity": "decimal",
  "amount": "decimal",
  "account_number": "string",
  "source": "string (internal" | "external)"
  "external_id": "string"
}
```
### Regras de mapeamento

**Fonte Interna**
  - `id` → `external_id`
  - `tradeDate` → `date`
  - `price` → `price`
  - `amount` → `amount`
  - `quantity` → `amount` / `price`
  - `accountNumber` → `account_number`
  - `source` = `"internal"`

**Fonte Externa**
  - `id` → `external_id`
  - `date` → `date`
  - `price` → `price`
  - `quantity` → `quantity`
  - `amount` → `quantity` * `price`
  - `account` → `account_number`
  - `source` = `"external"`

## 5. Endpoint Esperado

**`GET /transactions`**

Este endpoint deve:
- Consultar as duas fontes de dados
- Transformar e unificar os resultados no formato esperado
- Retornar a lista consolidada de transações


**Query Parameters**
- `account_number`: filtra as transações pelo número da conta

**Exemplo de resposta**

```json
[
    {
      "id": "c3f5c3f0-6c0a-4e04-9a72-22c2f8a10a17",
      "date": "2025-09-30",
      "price": 603.80,
      "quantity": 52.10,
      "amount": 31457.98,
      "account_number": "46649416",
      "source": "internal",
      "external_id": "1"
    },
    {
      "id": "8a02e6be-2c1a-46f6-9f55-8bb7a15d528f",
      "date": "2025-09-27",
      "price": 103.15,
      "quantity": 20,
      "amount": 2063.00,
      "account_number": "46649416",
      "source": "external",
      "external_id": "3"
    }
]
```
## 6. Orientações para o desenvolvimento
1. **Clone** este repositório em sua máquina.
2. **Crie uma branch** a partir da `main` com o nome `python-challenge-{seu usuário git}` (ex.: `python-challenge-hrabtg`).

> Fique à vontade para realizar quantos commits achar necessário.
