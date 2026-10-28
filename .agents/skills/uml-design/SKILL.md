---
name: uml-design
description: Thiết kế các biểu đồ UML chuẩn hóa (Use Case, Sequence, Class, State, Activity, ERD) dựa trên yêu cầu hệ thống và kiến trúc phần mềm đã được phê duyệt.
---
# Kỹ năng Thiết kế Biểu đồ UML (UML Design Skill)

## 1. Mục tiêu (Objective)
Mô hình hóa trực quan và chuẩn xác cấu trúc, hành vi, luồng tương tác và vòng đời trạng thái của hệ thống quản lý hỗ trợ khách hàng ViettinCare bằng các biểu đồ UML tiêu chuẩn (sử dụng Mermaid và PlantUML).

## 2. Đầu vào (Inputs)
Đọc và phân tích:
- `docs/requirements.md` (Danh sách FR-001 đến FR-011)
- `docs/user-stories.md`
- `docs/architecture.md`
- `database/schema.sql`

## 3. Quy trình thực hiện (Process)
1. **Biểu đồ Ca sử dụng (Use Case Diagram)**:
   - Xác định các Actor: Admin, Team Lead, Support Agent, Customer, Gemini LLM.
   - Xác định các Use Case chính: Đăng nhập, Tạo ticket, Phân công ticket, Trao đổi, Xem báo cáo SLA, AI Phân loại, AI Gợi ý trả lời RAG, Phê duyệt Human Gate.
   - Thể hiện quan hệ `<<include>>` (ví dụ: AI Gợi ý trả lời include Tra cứu FAQ) và `<<extend>>`.
2. **Biểu đồ Tuần tự (Sequence Diagram)**:
   - Mô hình hóa luồng tiếp nhận sự cố, lọc PII, tra cứu FAQ, gọi LLM, trả về bản nháp.
   - Thể hiện rõ điểm ngắt **Human Gate**: Nhân viên hỗ trợ chỉnh sửa và bấm nút duyệt trước khi hệ thống lưu vào CSDL và gửi cho khách.
3. **Biểu đồ Lớp (Class Diagram)**:
   - Thể hiện các lớp thực thể: `User`, `Customer`, `Ticket`, `TicketComment`, `FAQ`, `AILog`.
   - Các lớp dịch vụ: `AuthService`, `TicketService`, `CustomerService`, `AISupportService`.
   - Quan hệ kết tập, phụ thuộc và số lượng phần tử (Multiplicity: 1..*, 0..1).
4. **Biểu đồ Máy trạng thái (State Machine Diagram)**:
   - Vòng đời trạng thái ticket: `[Mới]` -> `[Đang xử lý]` -> `[Chờ khách hàng]` -> `[Đã đóng]`.
5. **Biểu đồ Hoạt động (Activity Diagram)**:
   - Luồng rẽ nhánh: Có tìm thấy FAQ hay không, có mạng Internet hay không, nhân viên duyệt hay yêu cầu AI viết lại.

## 4. Đầu ra cần tạo (Outputs)
- Các biểu đồ được tích hợp trực tiếp vào `docs/architecture.md` và tài liệu báo cáo tổng thể.
