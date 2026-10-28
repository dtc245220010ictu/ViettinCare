---
name: database-design
description: Design normalized relational database schema for ticket management, customers, support staff, comments, and AI audit logs.
---
# Database Design Skill
## Objective
Design a normalized, robust relational database schema (MySQL/PostgreSQL/SQLite) that supports ticket lifecycle, role-based access control, conversation logs, FAQ knowledge base for RAG, and AI recommendation audit logs.

## Inputs
Read:
- docs/requirements.md
- docs/architecture.md

## Process
1. Requirements Analysis for Data Entities
2. Identify Entities:
   - `users`: Support staff, admins, team leads
   - `customers`: Customer profiles & contact info
   - `tickets`: Support tickets with category, priority, status, assigned agent
   - `ticket_comments`: Conversation exchanges between customer & staff
   - `faqs`: Knowledge base articles / FAQ entries for RAG retrieval
   - `ai_logs`: Audit trail for AI suggestions, latency, token usage, human approval decisions
3. Define Relationships (1-N, N-N).
4. Normalization (Reach 3NF).
5. Define Primary Keys, Foreign Keys, Unique Constraints, Default values, and Check Constraints.
6. Define Indexes for performance (search on ticket status, customer_id, assigned_to, created_at, fulltext on FAQ).
7. Generate SQL Schema (`database/schema.sql`).
8. Verification against functional requirements.

## Rules
- Do not write application source code.
- Always include foreign key constraints with appropriate ON DELETE actions.
- Include audit timestamps (`created_at`, `updated_at`) on all major tables.
- Store sensitive credentials hashed (bcrypt), never plaintext.

## Outputs
Create:
- docs/database-design.md
- database/schema.sql

## Verification
Verify normalization, constraints, index coverage, and compliance with FR-001 through FR-011.

