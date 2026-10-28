# Báo cáo đánh giá bảo mật (Security Review Report) - Đề tài 10

## 1. Mục tiêu kiểm tra
Thực hiện đánh giá bảo mật theo checklist của `security-review` skill dựa trên chuẩn OWASP Top 10 và các nguy cơ đặc thù của ứng dụng AI/LLM.

## 2. Kết quả kiểm tra theo Checklist

### 1. SQL Injection (Phòng chống tiêm mã SQL)
- **Đánh giá**: **AN TOÀN (PASS)**.
- **Bằng chứng**: Toàn bộ các câu lệnh truy vấn trong `services/ticket_service.py`, `services/auth_service.py`, `services/customer_service.py`, và `services/ai_support_service.py` đều sử dụng cú pháp tham số hóa với dấu `?` (`cursor.execute(sql, params)`). Không có câu lệnh nào nối chuỗi thô.

### 2. Cross-Site Scripting (XSS)
- **Đánh giá**: **AN TOÀN (PASS)**.
- **Bằng chứng**: Template Jinja2 mặc định bật tính năng auto-escaping cho toàn bộ biến văn bản. Chỉ các chuỗi xuống dòng `replace('\n', '<br>')` trong bình luận được đánh dấu `|safe` sau khi đã được kiểm soát.

### 3. Authentication & Password Storage (Xác thực & Mật khẩu)
- **Đánh giá**: **AN TOÀN (PASS)**.
- **Bằng chứng**: Mật khẩu được băm bằng thuật toán bảo mật của Werkzeug (`generate_password_hash` / `check_password_hash` dựa trên PBKDF2/SHA-256). Mật khẩu không bao giờ được lưu trữ dưới dạng bản rõ (plaintext).

### 4. Secrets Management (Quản lý khóa bí mật)
- **Đánh giá**: **AN TOÀN (PASS)**.
- **Bằng chứng**: Khóa `GEMINI_API_KEY` và `SECRET_KEY` được đọc hoàn toàn từ biến môi trường thông qua `os.getenv` và thư viện `python-dotenv`. Không có khóa API nào bị hard-code trong mã nguồn hoặc đẩy lên Git.

### 5. AI Guardrails & PII Sanitization (Bảo vệ dữ liệu cá nhân & Hallucination)
- **Đánh giá**: **AN TOÀN (PASS)**.
- **Bằng chứng**:
  - Dữ liệu trước khi gửi sang Gemini LLM đều chạy qua bộ lọc `sanitize_pii` để ẩn mật khẩu, số thẻ ngân hàng, số điện thoại.
  - Áp dụng nguyên tắc **Human-in-the-Loop**: AI chỉ đóng vai trò trợ lý sinh bản nháp (`draft_response`), bắt buộc nhân viên hỗ trợ phải đọc, biên tập và bấm nút phê duyệt mới được gửi chính thức đến khách hàng.
  - Prompt hệ thống được thiết lập nghiêm ngặt: Tuyệt đối cấm AI tự ý cam kết bồi thường hoàn tiền hoặc bịa đặt chính sách trái với cơ sở tri thức FAQ.
