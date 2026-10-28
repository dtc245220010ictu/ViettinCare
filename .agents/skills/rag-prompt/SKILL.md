---
name: rag-prompt
description: Construct constrained, grounded prompts for LLM response generation based on retrieved context and enterprise policy.
---
# RAG Prompt Engineering Skill

## Objective
Design highly disciplined prompts that instruct the LLM to generate responses strictly grounded in provided context, prohibiting hallucination and enforcing support guidelines.

## Structure
1. **System Persona**: Professional support assistant for internal staff and customers.
2. **Grounding Rules**:
   - Only use facts present in the `[CONTEXT]` section.
   - Do NOT invent policies, features, or compensation rules.
   - If context is insufficient, state clearly that information is not available and ask for clarification.
3. **Context Section**: Injected from the retrieval & context-builder steps.
4. **User Query**: Customer question or issue description.
5. **Output Constraints**: Polite, professional Vietnamese; concise bullet points where applicable.

## Rules
- Explicitly enforce: "Không tự tạo dữ liệu nếu context không cung cấp."
- Prohibit unauthorized refund or legal commitments.
