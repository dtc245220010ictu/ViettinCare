---
name: ai-prompt
description: Formulate grounded, constrained system and user prompts for customer support response drafting, ticket classification, and conversation summarization.
---
# AI Prompt Engineering Skill
## Objective
Design highly disciplined prompts that instruct the LLM to act strictly as an internal support assistant generating draft responses for staff approval, summarizing long threads, and categorizing tickets without hallucinating policies or making unauthorized commitments.

## Structure
1. **System Role & Persona**: Professional customer care specialist assistant for internal staff.
2. **Grounding & Guardrail Rules**:
   - Only draft replies for staff review; staff will edit and send.
   - Strictly adhere to company policy and provided FAQ context.
   - NEVER promise unauthorized refunds, compensations, or system changes unless explicitly verified in context.
   - Maintain a polite, empathetic, and professional tone in Vietnamese.
3. **Context Injection**: Provided by `context-builder`.
4. **Task Instruction**:
   - Task A: Draft polite response to customer addressing their exact concern.
   - Task B: Summarize key progress and blockers in bullet points for a handover agent.
   - Task C: Recommend category and priority with justification.

## Rules
- Explicitly state: "Nếu thông tin không đủ trong tài liệu hỗ trợ, hãy yêu cầu khách hàng cung cấp thêm chi tiết hoặc chuyển tiếp chuyên viên cấp cao, không được tự suy diễn chính sách."

