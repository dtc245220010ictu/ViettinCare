---
name: architecture-design
description: Thiết kế kiến trúc phần mềm từ các yêu cầu đã phê duyệt, bảo đảm tính truy vết và lập biên bản quyết định kiến trúc (ADR) cho hệ thống hỗ trợ khách hàng tích hợp AI.
---
# Kỹ năng Thiết kế Kiến trúc (Architecture Design Skill)

## 1. Mục tiêu (Objective)
Chuyển hóa các yêu cầu phần mềm đã được con người phê duyệt thành cấu trúc kiến trúc phần mềm mạch lạc, mô-đun hóa, đáp ứng cả các luồng xử lý giao dịch truyền thống và luồng AI tăng cường (RAG, phân loại, tóm tắt, duyệt phản hồi).

## 2. Đầu vào (Inputs)
Đọc các tài liệu yêu cầu đã được phê duyệt:
- `docs/requirements.md`
- `docs/user-stories.md`
- `docs/acceptance-criteria.md`

## 3. Quy trình thực hiện (Process)
1. **Xác định phong cách kiến trúc**: Phân tầng (Layered Architecture) kết hợp Service-Oriented AI Pipeline.
2. **Xác định các thành phần chính**:
   - Tầng Trình diễn (Web UI, AI Workspace Panel)
   - Tầng Điều khiển (Flask Blueprints, Auth & RBAC Middleware)
   - Tầng Dịch vụ nghiệp vụ (`AuthService`, `CustomerService`, `TicketService`)
   - Tầng AI Tăng cường (`AISupportService`, `TicketAnalyzer`, `FAQRetriever`, `ContextBuilder`, `PromptBuilder`)
   - Tầng Dữ liệu (Relational Repository, SQLite/MySQL)
3. **Định nghĩa trách nhiệm từng thành phần**: Phân định rõ ranh giới xử lý dữ liệu và trách nhiệm đơn lẻ (Single Responsibility Principle).
4. **Xác định sự phụ thuộc (Dependencies)**: Kiểm soát hướng phụ thuộc đơn chiều (Routes -> Services -> Models/Database).
5. **Định nghĩa giao tiếp giữa các thành phần**: REST API đồng bộ, cấu trúc JSON có định dạng chuẩn.
6. **Xác định luồng dữ liệu (Data Flow)**: Luồng dữ liệu nghiệp vụ và luồng dữ liệu AI có sự can thiệp của con người (Human Gate).
7. **Xác định các hệ thống bên ngoài**: Google Gemini LLM API, Cổng Webhook, Dịch vụ Email.
8. **Thiết lập ranh giới bảo mật (Security Boundaries)**:
   - Cô lập quyền truy cập cơ sở dữ liệu đối với dịch vụ AI bên ngoài (LLM không được chạy lệnh SQL trực tiếp).
   - Bộ lọc khử định danh PII đứng trước mọi yêu cầu gửi ra bên ngoài mạng nội bộ.
9. **Lập biên bản quyết định kiến trúc (ADR)**: Ghi chép lý do lựa chọn công nghệ và kiến trúc.
10. **Kiểm tra tính truy vết (Traceability Check)**: Đảm bảo mọi FR đều được ánh xạ vào ít nhất một thành phần kiến trúc cụ thể.

## 4. Quy tắc bắt buộc (Rules)
- Không viết mã nguồn chi tiết trong bước thiết kế.
- Không tự ý sửa đổi yêu cầu nghiệp vụ đã được phê duyệt.
- Tuyệt đối không cho phép mô hình ngôn ngữ lớn (LLM) truy cập hoặc thao tác trực tiếp lên cơ sở dữ liệu.
- Mọi quyết định kiến trúc lớn phải có lý do kỹ thuật thuyết phục (Rationale).

## 5. Đầu ra cần tạo (Outputs)
- `docs/architecture.md`
- `docs/architecture-decisions.md`

## 6. Tiêu chuẩn kiểm chứng (Verification)
Xác nhận mọi yêu cầu chức năng từ `FR-001` đến `FR-011` đều được hỗ trợ bởi ít nhất một thành phần kiến trúc tương ứng trước khi chuyển sang bước thiết kế CSDL.
