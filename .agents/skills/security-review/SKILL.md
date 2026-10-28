---
name: security-review
description: Kiểm toán kiến trúc phần mềm, mã nguồn và tích hợp AI nhằm phát hiện các lỗ hổng an ninh mạng và bảo đảm tuân thủ quy định quyền riêng tư dữ liệu khách hàng.
---
# Kỹ năng Kiểm toán Bảo mật (Security Review Skill)

## 1. Mục tiêu (Objective)
Đánh giá mức độ an toàn thông tin toàn diện của hệ thống dựa trên tiêu chuẩn OWASP Top 10 và các rủi ro an ninh đặc thù của ứng dụng AI/LLM (Prompt Injection, Rò rỉ dữ liệu cá nhân PII, AI Hallucination).

## 2. Đầu vào (Inputs)
Đọc và rà soát:
- Toàn bộ mã nguồn dự án trong repository
- Các file cấu hình (`.env.example`, `requirements.txt`)
- Tài liệu kiến trúc và luồng dữ liệu `docs/architecture.md`

## 3. Quy trình thực hiện (Process)
Kiểm tra theo bảng kiểm tra an ninh (Security Checklist):
1. **Lỗ hổng SQL Injection**:
   - Xác minh toàn bộ các câu lệnh SQL trong `services/` sử dụng cú pháp tham số hóa (`?` hoặc `%s`).
   - Tuyệt đối nghiêm cấm việc cộng chuỗi (string concatenation) hoặc f-string trong câu lệnh SQL.
2. **Lỗ hổng Cross-Site Scripting (XSS)**:
   - Kiểm tra việc auto-escaping của template engine Jinja2 đối với dữ liệu người dùng nhập.
   - Hạn chế tối đa việc sử dụng bộ lọc `|safe`.
3. **Lỗ hổng Cross-Site Request Forgery (CSRF)**:
   - Kiểm tra cơ chế bảo vệ phiên đăng nhập và các request POST thay đổi trạng thái.
4. **Xác thực và Lưu trữ Mật khẩu (Authentication)**:
   - Đảm bảo mật khẩu người dùng được băm bằng thuật toán an toàn (Werkzeug PBKDF2/SHA-256 hoặc bcrypt).
   - Tuyệt đối cấm lưu mật khẩu bản rõ trong CSDL hoặc trong tệp log.
5. **Kiểm soát Phân quyền (Authorization & RBAC)**:
   - Xác thực vai trò người dùng (Admin, Lead, Agent) tại từng route và API.
   - Ngăn chặn tình trạng leo thang đặc quyền ngang và dọc (IDOR).
6. **Quản lý Thông tin Bí mật (Secrets Management)**:
   - Xác nhận khóa bí mật (`SECRET_KEY`, `GEMINI_API_KEY`) không bị hard-code trong mã nguồn hoặc commit vào Git.
   - File `.env` phải được khai báo trong `.gitignore`.
7. **Bảo vệ Dữ liệu Cá nhân & Khử định danh (PII Sanitization)**:
   - Kiểm tra bộ lọc khử định danh trước khi gửi dữ liệu sang LLM bên thứ ba (loại bỏ mật khẩu, số thẻ ngân hàng, số điện thoại).
8. **Kiểm soát Hành vi AI & Phòng chống Bịa đặt (AI Guardrails)**:
   - Kiểm tra chính sách Human-in-the-Loop: AI chỉ sinh bản nháp, nhân viên hỗ trợ bắt buộc phải duyệt trước khi gửi cho khách.
   - Ràng buộc prompt hệ thống: Ngăn cấm AI tự ý đưa ra cam kết bồi thường hoàn tiền hoặc chính sách sai lệch.
9. **Kiểm tra Lỗ hổng Thư viện phụ thuộc**:
   - Rà soát các phiên bản thư viện trong `requirements.txt` nhằm tránh các gói lỗi thời đã bị cảnh báo CVE.
10. **Ngăn chặn Rò rỉ Thông tin (Information Leakage)**:
    - Máy chủ không được trả về chi tiết stack trace hoặc thông tin kỹ thuật nhạy cảm ra ngoài client khi gặp lỗi 500.

## 4. Đầu ra cần tạo (Outputs)
- `docs/security-review.md`
