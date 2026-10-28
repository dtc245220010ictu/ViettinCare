---
name: question-analysis
description: Phân tích câu hỏi ngôn ngữ tự nhiên của người dùng để trích xuất ý định (intent), thực thể (entities), từ khóa (keywords) và các ràng buộc có cấu trúc.
---
# Kỹ năng Phân tích Câu hỏi (Question Analysis Skill)

## 1. Mục tiêu (Objective)
Tiếp nhận và bóc tách câu hỏi hoặc yêu cầu khiếu nại bằng ngôn ngữ tự nhiên từ người dùng, chuyển đổi thành biểu diễn trung gian có cấu trúc dạng JSON (Structured Intent), đóng vai trò đầu vào trực tiếp cho module truy xuất dữ liệu (Retrieval Engine).

## 2. Đầu vào (Inputs)
- Một câu hỏi hoặc đoạn văn bản tiếng Việt do khách hàng/người dùng gửi đến
- Lịch sử hội thoại ngữ cảnh (nếu có)

## 3. Quy trình thực hiện (Process)
1. **Lọc sạch dữ liệu đầu vào (Text Sanitization)**: Khử bỏ các chuỗi nhạy cảm (mật khẩu, số thẻ ngân hàng, số điện thoại).
2. **Nhận diện ý định cốt lõi (Core Intent)**:
   - Tra cứu giải pháp tài khoản / quên mật khẩu
   - Sự cố thanh toán / hóa đơn bị trừ tiền sai
   - Báo cáo lỗi kỹ thuật / màn hình trắng / lỗi 500
   - Tư vấn gói cước, nâng cấp dịch vụ
3. **Trích xuất thực thể và từ khóa (Entity & Keyword Extraction)**:
   - Trích xuất danh mục nghiệp vụ (`category`)
   - Trích xuất từ khóa tìm kiếm (`keywords`)
   - Đánh giá mức độ khẩn cấp (`priority`: Low, Medium, High, Urgent)
4. **Chuẩn hóa dữ liệu đầu ra**: Đóng gói thành đối tượng JSON chuẩn:
   ```json
   {
     "category": "Tài khoản & Đăng nhập",
     "keywords": ["đổi mật khẩu", "reset", "email"],
     "suggested_priority": "High",
     "sanitized_summary": "Khách hàng không nhận được email đổi mật khẩu..."
   }
   ```

## 4. Quy tắc bắt buộc (Rules)
- Không tự ý bịa đặt từ khóa hoặc thông tin không xuất hiện trong câu hỏi gốc.
- Không gửi trực tiếp câu hỏi người dùng chưa qua phân tích sang LLM mà bắt buộc phải qua bước trích xuất có cấu trúc này.

## 5. Đầu ra cần tạo (Outputs)
- Đối tượng JSON đại diện cho ý định người dùng (Intermediate Representation).
- Tài liệu mô tả module phân tích: `docs/question-analysis.md` (hoặc `docs/ticket-analysis.md`).
