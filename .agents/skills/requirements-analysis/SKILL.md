---
name: requirements-analysis
description: Analyze software requirements and transform natural-language requirements into structured functional requirements, non-functional requirements, user stories, acceptance criteria, and traceability information for customer support systems.
---
# Requirements Analysis Skill
## Objective
Analyze customer support management requirements systematically and produce a structured specification suitable for subsequent architecture, database, implementation, and testing activities.

## Inputs
Read the following project artifacts when available:
- customer requirements (docs/customer-requirement.md)
- business requirements & support SLAs
- existing requirements documentation
- project constraints (human-in-the-loop review, PII sanitization)

## Process
### 1. Identify stakeholders
Identify all stakeholders relevant to the customer support system (Customers, Support Agents, Team Leaders, System Administrators).
### 2. Identify actors
Identify actors interacting with the system.
### 3. Identify functional requirements
Convert explicit business needs into functional requirements.
Use IDs:
- FR-001: Authentication & RBAC (Admin, Team Lead, Agent)
- FR-002: Customer profile management
- FR-003: Ticket creation and lifecycle management (Status: New, In Progress, Waiting Customer, Closed)
- FR-004: Ticket assignment to support agents
- FR-005: Ticket conversation history and attachment tracking
- FR-006: Ticket search, filter & categorization
- FR-007: Basic SLA and resolution statistics dashboard
- FR-008: AI ticket classification & priority recommendation
- FR-009: AI draft response suggestion based on FAQ/KB
- FR-010: AI ticket conversation history summarization
- FR-011: Human-in-the-loop approval mechanism for AI draft responses
### 4. Identify non-functional requirements
Identify requirements related to:
- performance (response time < 2s for CRUD, < 4s for AI generation)
- security (RBAC, PII data masking before sending to external LLM, SQL injection prevention)
- reliability (Graceful fallback when AI provider is unavailable)
- usability (Intuitive split-view UI for ticket and AI assistant)
- maintainability (Modular services architecture)
- scalability
Use IDs: NFR-001, NFR-002, etc.
### 5. Identify business rules
List business rules explicitly stated:
- Support agent MUST approve/edit AI draft responses before sending to customer.
- PII (passwords, payment data, personal secrets) must be masked before sending to external LLM.
- AI must NOT make unauthorized promises (no unauthorized refund commitment without human approval).
Do not invent business rules.
### 6. Identify assumptions
Separate assumptions from actual requirements.
### 7. Identify ambiguities
Identify requirements that are ambiguous, incomplete, contradictory, or not testable.
### 8. Create user stories
Use:
As a <role>,
I want <capability>,
so that <benefit>.
### 9. Create acceptance criteria
Each important user story must have testable acceptance criteria (Given - When - Then).
### 10. Traceability
Every user story must be traceable to one or more requirements.

## Rules
- Do not write source code.
- Do not design the database.
- Do not design the architecture.
- Do not invent undocumented business rules.
- Clearly distinguish requirements from assumptions.
- Clearly identify missing information.

## Outputs
Create or update:
- docs/requirements.md
- docs/user-stories.md
- docs/acceptance-criteria.md
- docs/requirements-issues.md

## Verification
Before completing the task verify:
- all functional requirements have IDs;
- all non-functional requirements have IDs;
- user stories trace to requirements;
- acceptance criteria are testable;
- ambiguities are explicitly documented.
