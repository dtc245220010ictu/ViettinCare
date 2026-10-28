---
name: context-builder
description: Construct compact, sanitized context combining ticket details, filtered conversation history, and official FAQ guidelines for the LLM.
---
# Context Builder Skill
## Objective
Build a concise, well-structured context block containing sanitized ticket details, filtered past message exchanges, and verified FAQ references, while removing noise and ensuring token efficiency.

## Inputs
- Ticket data (ID, Title, Category, Priority, Status)
- Filtered ticket conversation history (Customer & Agent comments)
- Retrieved FAQ/KB solutions

## Process
1. Sanitize customer inputs (mask email, phone, personal identity info).
2. Filter out conversational fluff (e.g., redundant greeting duplicates).
3. Assemble formatted context sections:
   - `[TICKET_INFO]`
   - `[RECENT_EXCHANGES]`
   - `[OFFICIAL_FAQ_GUIDELINES]`
4. Enforce strict character/token budget (max 2000 characters).

## Rules
- Do not introduce facts or customer claims not in the original ticket.
- Do not modify customer's original complaint intent.
- Ensure all retrieved FAQ content is cleanly attributed.

