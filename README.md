# 📘 Desafio Técnico – Desenvolvedor Python Júnior

## 1. Visão Geral (o fluxo)
Neste desafio, você deverá **consumir duas fontes de transações (APIs)**, cada uma com seu próprio formato de dados.  
Sua tarefa será:  

1. **Consumir** os dados das duas fontes  
2. **Normalizar** as transações em um **formato único**  
3. **Expor um endpoint** que:  
   - Consulte as duas fontes  
   - Transforme e unifique os dados  
   - Retorne as transações já processadas  

Pense nisso como construir um **pipeline de dados**:  
**[APIs de origem] → [Transformação/Normalização] → [API unificada]**

---

## 2. Requisitos
- **Consumir** duas APIs com schemas diferentes  
- **Transformar** os dados para um formato unificado (detalhes abaixo)  
- **Criar** um endpoint REST que execute o fluxo e retorne os dados processados  
- **Organizar** o projeto de forma limpa e estruturada (pastas, arquivos, módulos)  
- **Aplicar conceitos de POO**  

---

## 3. Fontes de Dados
### Fonte Interna (Internal Transaction Source)  
**Endpoint:**  
`GET https://68dc18d97cd1948060a975d9.mockapi.io/api/internal-transaction-source`  

**Exemplo de resposta:**  
```json
[
  {
    "id": "1",
    "tradeDate": "2025-09-30",
    "price": "603.80",
    "amount": "52.10",
    "accountNumber": "46649416",
  }
]
```

### Fonte Externa (External Transaction Source)

**Endpoint:**  
`GET https://68dc18d97cd1948060a975d9.mockapi.io/api/external-transaction-source`

**Exemplo de resposta:**
```json
[
  {
    "id": "1",
    "date": "2025-09-30T12:40:15.454Z",
    "price": "103.15",
    "quantity": 20,
    "account": "24975936",
  }
]
```

## 4. Schema Unificado (formato final)
Cada transação deve ser transformada no seguinte schema:

```json
{
  "id": "string",
  "date": "Date ISO 8601",
  "price": "decimal",
  "quantity": "decimal",
  "amount": "decimal",
  "accountNumber": "string",
  "source": "internal" | "external"
}
```
### Regras de mapeamento

- **Fonte Interna**
  - `id` → `id`
  - `tradeDate` → `date`
  - `price` → `price`
  - `amount` → `amount`
  - `quantity` → `amount` / `price`
  - `accountNumber` → `accountNumber`
  - `source` = `"internal"`

- **Fonte Externa**
  - `id` → `id`
  - `date` → `date`
  - `price` → `price`
  - `quantity` → `quantity`
  - `amount` → `quantity` * `price`
  - `account` → `accountNumber`
  - `source` = `"external"`

## 5. Endpoint Esperado

**`GET /transactions`**

Este endpoint deve:
- Consultar as duas fontes de dados
- Transformar e unificar os resultados no formato esperado
- Retornar a lista consolidada de transações


### Query Parameters
- `account-number`: filtra as transações pelo número da conta

**Exemplo de resposta:**

```json
[
    {
      "id": "1",
      "date": "2025-09-30",
      "price": 603.80,
      "quantity": 52.10,
      "amount": 31457.98,
      "accountNumber": "46649416",
      "source": "internal"
    },
    {
      "id": "1",
      "date": "2025-09-27",
      "price": 103.15,
      "quantity": 20,
      "amount": 2063.00,
      "account_id": "46649416",
      "source": "external"
    }
]
```
