---
name: ticket-analysis
description: Analyze natural language customer support tickets to extract structured category, priority, customer sentiment, and sanitized problem keywords.
---
# Ticket Analysis Skill
## Objective
Parse incoming support ticket text and message exchanges to generate an intermediate structured JSON payload containing issue classification, urgency score, and filtered search terms.

## Inputs
- Ticket title & initial description
- Conversation exchanges (customer messages)

## Process
1. Sanitize text: strip credit card numbers, passwords, phone numbers, and sensitive tokens.
2. Identify Category candidates:
   - "Tài khoản & Đăng nhập" (Account & Login)
   - "Thanh toán & Hóa đơn" (Billing & Payment)
   - "Lỗi kỹ thuật & Phần mềm" (Technical Bug)
   - "Tư vấn & Hướng dẫn sử dụng" (Inquiry & User Guide)
   - "Khiếu nại dịch vụ" (Service Complaint)
3. Detect Urgency / Suggested Priority (Low, Medium, High, Urgent) based on keywords (e.g. "không thể truy cập", "tiền bị trừ hai lần", "hệ thống sập").
4. Extract search keywords for FAQ/Knowledge Base lookup.

## Rules
- Do not invent issues not present in the customer message.
- Output MUST be structured JSON.
- Never pass unmasked credentials into downstream AI contexts.

## Output Format
```json
{
  "category": "Tài khoản & Đăng nhập",
  "suggested_priority": "High",
  "sentiment": "Frustrated",
  "keywords": ["đổi mật khẩu", "reset", "chưa nhận email"],
  "sanitized_summary": "Khách hàng không thể đăng nhập sau khi đổi mật khẩu, không nhận được email đặt lại."
}
```
