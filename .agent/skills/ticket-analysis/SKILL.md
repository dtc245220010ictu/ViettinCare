---
name: ticket-analysis
description: Phân tích nội dung ticket hỗ trợ khách hàng bằng ngôn ngữ tự nhiên để trích xuất danh mục vấn đề, mức độ ưu tiên đề xuất, cảm xúc khách hàng và từ khóa sự cố đã khử định danh PII.
---
# Kỹ năng Phân tích Ticket (Ticket Analysis Skill)

## 1. Mục tiêu (Objective)
Bóc tách tiêu đề và mô tả sự cố của ticket thành biểu diễn trung gian dạng JSON có cấu trúc. Đây là cầu nối giúp tự động hóa khâu gán nhãn, phát hiện sự cố khẩn cấp và cung cấp đầu vào chuẩn cho bộ máy RAG.

## 2. Đầu vào (Inputs)
- Tiêu đề ticket (`title`)
- Mô tả chi tiết vấn đề (`description`)
- Chuỗi bình luận trao đổi của khách hàng (nếu có)

## 3. Quy trình thực hiện (Process)
1. **Khử định danh dữ liệu cá nhân (PII Sanitization)**:
   - Che mật khẩu: `[MASKED_PASSWORD]`
   - Che số thẻ ngân hàng, số tài khoản: `[MASKED_CREDIT_CARD]`, `[MASKED_ACCOUNT_NO]`
   - Che số điện thoại liên hệ: `[MASKED_PHONE]`
2. **Xác định Danh mục nghiệp vụ (Category)**:
   - `Tài khoản & Đăng nhập`: Từ khóa liên quan đến mật khẩu, login, quên pass, OTP.
   - `Thanh toán & Hóa đơn`: Từ khóa liên quan đến trừ tiền, chuyển khoản, ngân hàng, QR code.
   - `Lỗi kỹ thuật & Phần mềm`: Từ khóa lỗi 500, crash, trắng màn hình, hệ thống sập.
   - `Tư vấn & Hướng dẫn sử dụng`: Từ khóa nâng cấp VIP, hỏi bảng giá, hướng dẫn sử dụng.
3. **Đề xuất Mức độ ưu tiên (Suggested Priority)**:
   - `Urgent`: Sự cố liên quan đến tiền bạc, trừ tiền 2 lần hoặc lỗi sập hệ thống.
   - `High`: Không đăng nhập được, tài khoản bị khóa trong giờ làm việc.
   - `Medium`: Các lỗi hiển thị nhỏ hoặc thắc mắc dịch vụ thông thường.
   - `Low`: Góp ý cải tiến hoặc phản ánh chung.
4. **Trích xuất từ khóa phục vụ tra cứu**: Đưa ra danh sách từ khóa đại diện ngắn gọn.

## 4. Đầu ra chuẩn (Output Format)
```json
{
  "category": "Tài khoản & Đăng nhập",
  "suggested_priority": "High",
  "keywords": ["đổi mật khẩu", "reset", "email"],
  "sanitized_summary": "Khách hàng không thể đăng nhập sau khi đổi mật khẩu..."
}
```
