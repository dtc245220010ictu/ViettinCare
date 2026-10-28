---
name: product-retrieval
description: Retrieve product or ticket knowledge records using structured intent and parameterized SQL queries.
---
# Product / Record Retrieval Skill

## Objective
Retrieve matching items from the database using parameterized queries based on structured intent criteria (categories, keywords, price/priority range) without SQL injection.

## Inputs
- Structured intent JSON from question analysis
- Filter parameters (category, keywords, status, priority)

## Process
1. Build parameterized SQL statements (`?` placeholders).
2. Apply category filters.
3. Apply keyword search conditions across relevant fields.
4. Apply priority or price constraints.
5. Apply sorting and result limit (max 5 records).
6. Return empty list gracefully if no record matches.

## Rules
- Never use SQL string concatenation.
- Always use parameterized queries.
- Do not dump the entire database into memory.
- If no results are found, return `[]`.
