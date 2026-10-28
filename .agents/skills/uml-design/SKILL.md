---
name: uml-design
description: Design standard UML diagrams (Use Case, Sequence, Class, Activity, ERD) from approved system requirements and architectural specifications.
---
# UML Design Skill

## Objective
Produce accurate, standard UML diagrams modeling system behavior, interactions, component lifecycles, and data structures using Mermaid and PlantUML standards.

## Inputs
Read:
- `docs/requirements.md`
- `docs/user-stories.md`
- `docs/architecture.md`
- `database/schema.sql`

## Process
1. **Use Case Diagram**:
   - Identify Actors (Admin, Team Lead, Support Agent, Customer, External LLM API).
   - Define Use Cases and boundaries.
   - Specify `<<include>>` and `<<extend>>` relationships.
2. **Sequence Diagram**:
   - Model the interaction flow between User, Controller, Services, Database, and LLM API.
   - Detail the Human-in-the-Loop review and approval sequence.
3. **Class Diagram**:
   - Model entities, attributes, methods, and associations (1..*, 0..1).
4. **State Machine Diagram**:
   - Model ticket status transitions (`New` -> `In Progress` -> `Waiting Customer` -> `Closed`).
5. **Activity Diagram**:
   - Model the AI classification and draft response workflow with error fallback.

## Outputs
- `docs/uml-diagrams.md` (or embedded in `docs/architecture.md`)
