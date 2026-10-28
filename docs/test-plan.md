# Kế hoạch kiểm thử (Test Plan) - Đề tài 10

## 1. Mục tiêu kiểm thử
Xác minh tính đúng đắn của toàn bộ các chức năng nghiệp vụ quản lý ticket và các tính năng AI tăng cường (phân loại, gợi ý trả lời RAG, tóm tắt chuỗi trao đổi, cơ chế duyệt của con người).

## 2. Phạm vi kiểm thử
- **Xác thực & Phân quyền**: Đăng nhập, session, vai trò Admin/Lead/Agent (FR-001).
- **Quản lý Ticket & Vòng đời**: Tạo mới, chuyển đổi trạng thái (New -> In Progress -> Waiting Customer -> Closed), gán việc, thêm trao đổi (FR-003, FR-004, FR-005).
- **Trợ lý AI & RAG**:
  - Khử định danh dữ liệu cá nhân PII (NFR-003).
  - Phân loại danh mục và mức ưu tiên tự động (FR-008).
  - Gợi ý câu trả lời nháp từ cơ sở tri thức FAQ (FR-009).
  - Cơ chế con người phê duyệt trước khi gửi (FR-010).
  - Tóm tắt chuỗi trao đổi dài (FR-011).

## 3. Chiến lược kiểm thử
- Sử dụng Framework **pytest**.
- Tách biệt kiểm thử Unit, Integration và API Simulation.
- Mocking và Fallback an toàn cho tầng dịch vụ AI bên ngoài khi không có kết nối internet hoặc API key.
