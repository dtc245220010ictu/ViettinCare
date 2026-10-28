---
name: database-design
description: Thiết kế lược đồ cơ sở dữ liệu quan hệ chuẩn hóa cho hệ thống quản lý ticket, thông tin khách hàng, tài khoản nhân viên, chuỗi trao đổi và nhật ký kiểm toán AI.
---
# Kỹ năng Thiết kế Cơ sở Dữ liệu (Database Design Skill)

## 1. Mục tiêu (Objective)
Thiết kế lược đồ cơ sở dữ liệu quan hệ (Relational Database Schema) đạt chuẩn hóa tối thiểu dạng chuẩn 3 (3NF), đảm bảo tính toàn vẹn dữ liệu, tối ưu hóa hiệu năng truy vấn cho quy trình quản lý ticket và lưu vết kiểm toán đầy đủ cho các hành động của Trợ lý AI.

## 2. Đầu vào (Inputs)
Đọc và phân tích:
- `docs/requirements.md`
- `docs/architecture.md`

## 3. Quy trình thực hiện (Process)
1. **Phân tích thực thể dữ liệu**: Trích xuất các thực thể từ yêu cầu nghiệp vụ:
   - `users`: Nhân viên hỗ trợ, Quản lý nhóm, Quản trị viên
   - `customers`: Hồ sơ khách hàng, phân hạng VIP/Standard
   - `tickets`: Yêu cầu hỗ trợ, danh mục, mức ưu tiên, trạng thái
   - `ticket_comments`: Lịch sử các lượt trao đổi phản hồi
   - `faqs`: Cơ sở tri thức, câu hỏi thường gặp phục vụ RAG
   - `ai_logs`: Nhật ký gọi AI, thời gian xử lý, độ trễ và trạng thái phê duyệt của con người
2. **Xác định các mối quan hệ (Relationships)**: Thiết lập quan hệ 1-N giữa Customer - Ticket, User - Ticket, Ticket - Comments, Ticket - AI Logs.
3. **Chuẩn hóa dữ liệu (Normalization)**: Đưa các bảng về dạng chuẩn 1NF, 2NF và 3NF nhằm loại bỏ dư thừa dữ liệu.
4. **Xác định Khóa chính và Khóa ngoại (PK & FK)**: Khóa chính tự tăng (AUTOINCREMENT), khóa ngoại liên kết ràng buộc toàn vẹn tham chiếu kèm quy tắc `ON DELETE CASCADE` hoặc `ON DELETE SET NULL`.
5. **Thiết lập ràng buộc dữ liệu (Constraints)**:
   - `NOT NULL` cho các trường bắt buộc
   - `UNIQUE` cho email, username, ticket_number
   - `CHECK` cho danh sách giá trị trạng thái hợp lệ (`status` IN ('New', 'In Progress', 'Waiting Customer', 'Closed'))
6. **Thiết kế Chỉ mục (Indexes)**: Đánh chỉ mục trên các cột thường xuyên lọc và tìm kiếm (`status`, `priority`, `customer_id`, `assigned_to`, `category`).
7. **Sinh mã lược đồ SQL**: Viết file `database/schema.sql` hoàn chỉnh, tương thích SQLite và MySQL.
8. **Kiểm tra đối chiếu**: Đối chiếu lược đồ với toàn bộ các ca nghiệp vụ yêu cầu.

## 4. Quy tắc bắt buộc (Rules)
- Không viết mã nguồn ứng dụng trong bước này.
- Mọi bảng bắt buộc phải có khóa chính.
- Mọi bảng quan trọng đều phải có các trường dấu vết thời gian (`created_at`, `updated_at`).
- Mật khẩu người dùng bắt buộc lưu ở dạng băm mã hóa an toàn, không lưu bản rõ.

## 5. Đầu ra cần tạo (Outputs)
- `docs/database-design.md`
- `database/schema.sql`

## 6. Tiêu chuẩn kiểm chứng (Verification)
Kiểm tra tính toàn vẹn: Không vi phạm chuẩn 3NF, đầy đủ khóa ngoại, chỉ mục được tạo đúng chỗ, sẵn sàng cho công đoạn lập trình.
