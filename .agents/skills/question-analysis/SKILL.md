---
name: question-analysis
description: Analyze natural language user queries to extract structured intent, entities, keywords, and constraints.
---
# Question Analysis Skill

## Objective
Analyze customer inquiries or support requests expressed in natural language and transform them into a structured intermediate representation (JSON).

## Inputs
- Natural language query from customer or user
- Conversation context (optional)

## Process
1. Sanitize text: strip PII and sensitive tokens.
2. Identify user intent:
   - Search/inquiry
   - Issue report / bug
   - Billing / payment question
   - Account / login support
3. Extract entities and constraints:
   - Category
   - Priority / urgency
   - Keywords
4. Output structured JSON.

## Output Format
```json
{
  "category": "Tài khoản & Đăng nhập",
  "keywords": ["đổi mật khẩu", "reset", "email"],
  "priority": "High"
}
```

## Rules
- Do not invent entities or constraints not mentioned in the query.
- Never pass unmasked credentials into downstream AI contexts.
