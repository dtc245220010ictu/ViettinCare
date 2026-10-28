---
name: faq-retrieval
description: Retrieve relevant Knowledge Base / FAQ articles using structured intent and parameterized queries from the database.
---
# FAQ Retrieval Skill
## Objective
Retrieve top matching FAQ articles and official support procedures matching the customer's issue without querying the entire database or executing unsafe string concatenation.

## Inputs
- Structured intent JSON from Ticket Analyzer
- Keywords & Category

## Process
1. Build parameterized SQL with match score or keyword LIKE filters.
2. Filter by matching Category and Keywords.
3. Order by relevance score / priority.
4. Limit results (Top 3 most relevant articles, max 2000 tokens).
5. If no FAQ matches, return empty result gracefully.

## Rules
- Never use SQL string concatenation; always use parameterized queries.
- Do not dump all FAQs into the prompt.
- Do not invent FAQs not existing in the knowledge base.

## Output Format
```json
[
  {
    "id": 12,
    "title": "Hướng dẫn xử lý sự cố không nhận được email đặt lại mật khẩu",
    "category": "Tài khoản & Đăng nhập",
    "solution_summary": "Kiểm tra hòm thư Spam/Junk; xác minh email chính chủ; liên hệ quản trị viên cấp mã OTP khẩn cấp."
  }
]
```
