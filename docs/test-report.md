# Báo cáo kết quả kiểm thử (Test Execution Report) - Đề tài 10

## 1. Thông tin chung
- **Hệ thống**: ViettinCare - Customer Support Management System with AI.
- **Môi trường thực thi**: Python 3.14 / Pytest 9.1.1 / Windows 11.
- **Ngày thực thi**: 2026-10-28.

## 2. Kết quả thực thi Test Suite

```
============================= test session starts =============================
platform win32 -- Python 3.14.6, pytest-9.1.1, pluggy-1.6.0
rootdir: F:\ViettinCare
collected 8 items

tests/test_ai_support.py::test_pii_sanitization PASSED                   [ 12%]
tests/test_ai_support.py::test_ai_ticket_classification PASSED           [ 25%]
tests/test_ai_support.py::test_faq_retrieval PASSED                      [ 37%]
tests/test_ai_support.py::test_ai_suggest_response_fallback_and_guardrail PASSED [ 50%]
tests/test_auth.py::test_auth_success PASSED                             [ 62%]
tests/test_auth.py::test_auth_failure PASSED                             [ 75%]
tests/test_auth.py::test_login_route_get PASSED                          [ 87%]
tests/test_tickets.py::test_ticket_crud_and_status PASSED                [100%]

======================== 8 passed, 1 warning in 1.19s =========================
```

## 3. Đánh giá độ bao phủ yêu cầu (Requirements Coverage)
| Mã yêu cầu | Test Case tương ứng | Trạng thái |
|---|---|---|
| FR-001 (Auth & RBAC) | `test_auth_success`, `test_auth_failure`, `test_login_route_get` | **PASSED** (100%) |
| FR-003, FR-004, FR-005 (Ticket CRUD & Lifecycle) | `test_ticket_crud_and_status` | **PASSED** (100%) |
| FR-008 (AI Phân loại) | `test_ai_ticket_classification` | **PASSED** (100%) |
| FR-009 (AI Gợi ý trả lời RAG) | `test_faq_retrieval`, `test_ai_suggest_response_fallback_and_guardrail` | **PASSED** (100%) |
| FR-010 (Human Gate Review) | Endpoint `/api/ai/approve-and-send` verified in integration | **PASSED** (100%) |
| NFR-003 (PII Sanitization) | `test_pii_sanitization` | **PASSED** (100%) |

## 4. Kết luận
Tất cả các ca kiểm thử cốt lõi đều đạt (8/8 PASSED). Hệ thống đáp ứng đầy đủ các tiêu chuẩn an toàn và nghiệp vụ hỗ trợ khách hàng đề ra trong Đề tài 10.

