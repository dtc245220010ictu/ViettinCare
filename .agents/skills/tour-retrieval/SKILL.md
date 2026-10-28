---
name: tour-retrieval
description: Retrieve service, itinerary, or support ticket records using structured intent criteria and parameterized database queries.
---
# Retrieval Skill (Tour / Support Services)

## Objective
Execute safe, parameterized database queries to retrieve domain items (service tours, tickets, FAQs) that match user preferences and constraints.

## Inputs
- Structured query criteria (category, keywords, dates, status, price)

## Process
1. Validate input parameters against allowed filter fields.
2. Formulate SQL `SELECT` using parameterized bindings.
3. Apply filters:
   - Category / Destination
   - Status / Priority
   - Keyword LIKE matches
4. Apply sorting and limit results.
5. Format retrieved records into clean dictionary objects.

## Rules
- Strictly parameterized SQL only (no raw string injection).
- Handle zero-match scenarios gracefully.
