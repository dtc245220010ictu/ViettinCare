---
name: faq-retrieval
description: Truy xuất các bài viết câu hỏi thường gặp (FAQ) và quy trình xử lý chuẩn từ cơ sở tri thức bằng câu lệnh SQL tham số hóa dựa trên phân loại nghiệp vụ.
---
# Kỹ năng Truy xuất FAQ (FAQ Retrieval Skill)

## 1. Mục tiêu (Objective)
Truy xuất nhanh chóng các bài viết hướng dẫn xử lý sự cố và chính sách dịch vụ từ bảng `faqs` phù hợp với nội dung ticket của khách hàng, đảm bảo tốc độ truy vấn cao (< 50ms) và tuyệt đối an toàn với SQL Injection.

## 2. Đầu vào (Inputs)
- Đối tượng intent có cấu trúc từ bộ phân tích ticket (`category`, `keywords`)

## 3. Quy trình thực hiện (Process)
1. Xây dựng câu lệnh SQL tham số hóa tìm kiếm theo danh mục nghiệp vụ:
   ```sql
   SELECT * FROM faqs WHERE category = ?;
   ```
2. Nếu danh mục chưa có bài viết trực tiếp, tìm kiếm mở rộng theo các từ khóa có liên quan:
   ```sql
   SELECT * FROM faqs WHERE keywords LIKE ? LIMIT 3;
   ```
3. Giới hạn số lượng bản ghi trả về tối đa 3 bài viết liên quan nhất để tiết kiệm dung lượng token của LLM.
4. Trả về danh sách đối tượng FAQ dưới dạng cấu trúc JSON.

## 4. Đầu ra mẫu (Output Format)
```json
[
  {
    "id": 1,
    "category": "Tài khoản & Đăng nhập",
    "question": "Khách hàng không nhận được email kích hoạt hoặc email reset mật khẩu?",
    "answer": "Hướng dẫn khách kiểm tra hòm thư Rác (Spam/Junk). Nếu sau 5 phút vẫn chưa nhận được, nhân viên hỗ trợ xác minh thông tin chính chủ và gửi mã OTP thủ công."
  }
]
```
