---
name: requirements-analysis
description: Phân tích yêu cầu phần mềm và chuyển đổi yêu cầu ngôn ngữ tự nhiên thành tài liệu đặc tả chức năng, phi chức năng, user stories, tiêu chí chấp nhận và ma trận truy vết cho hệ thống hỗ trợ khách hàng.
---
# Kỹ năng Phân tích Yêu cầu (Requirements Analysis Skill)

## 1. Mục tiêu (Objective)
Phân tích có hệ thống các yêu cầu nghiệp vụ quản lý hỗ trợ khách hàng, chuyển đổi yêu cầu ngôn ngữ tự nhiên thành bộ đặc tả kỹ thuật có cấu trúc, đóng vai trò đầu vào chuẩn xác cho các công đoạn thiết kế kiến trúc, thiết kế cơ sở dữ liệu, lập trình và kiểm thử.

## 2. Đầu vào (Inputs)
Đọc và đối chiếu các tài liệu dự án sau khi sẵn sàng:
- Yêu cầu của khách hàng (`docs/customer-requirement.md`)
- Quy định nghiệp vụ và tiêu chuẩn dịch vụ (SLA)
- Các tài liệu đặc tả hiện có
- Ràng buộc dự án (Bảo mật dữ liệu cá nhân PII, cơ chế con người kiểm duyệt Human-in-the-Loop)

## 3. Quy trình thực hiện (Process)
### Bước 1: Xác định các bên liên quan (Stakeholders)
Nhận diện tất cả các bên liên quan: Khách hàng sử dụng dịch vụ, Nhân viên hỗ trợ (Support Agent), Quản lý nhóm (Team Lead), Quản trị viên hệ thống (Admin).

### Bước 2: Xác định các tác nhân (Actors)
Xác định tác nhân tương tác trực tiếp với phần mềm.

### Bước 3: Xác định yêu cầu chức năng (Functional Requirements)
Chuyển đổi nhu cầu kinh doanh thành danh sách yêu cầu chức năng với mã định danh chuẩn:
- `FR-001`: Đăng nhập và phân quyền RBAC
- `FR-002`: Quản lý hồ sơ và thông tin khách hàng
- `FR-003`: Tạo và quản lý vòng đời Ticket (Mới, Đang xử lý, Chờ khách, Đã đóng)
- `FR-004`: Phân công ticket cho nhân viên xử lý
- `FR-005`: Lịch sử trao đổi và quản lý phản hồi
- `FR-006`: Tìm kiếm, lọc nâng cao theo trạng thái, mức ưu tiên, khách hàng
- `FR-007`: Báo cáo thống kê hiệu suất hỗ trợ và vi phạm SLA
- `FR-008`: AI tự động phân loại sự cố và gợi ý mức ưu tiên
- `FR-009`: AI gợi ý câu trả lời nháp đối chiếu cơ sở tri thức FAQ (RAG)
- `FR-010`: Cơ chế con người phê duyệt (Human Gate) trước khi gửi phản hồi AI
- `FR-011`: AI tóm tắt chuỗi trao đổi dài khi bàn giao ca trực

### Bước 4: Xác định yêu cầu phi chức năng (Non-Functional Requirements)
Định nghĩa tiêu chí kỹ thuật với mã định danh:
- `NFR-001` (Hiệu năng): CRUD < 1s, AI generation < 4s
- `NFR-002` (Bảo mật): Băm mật khẩu bcrypt/SHA-256, kiểm tra quyền truy cập route
- `NFR-003` (Quyền riêng tư): Tự động che dữ liệu nhạy cảm (PII Masking) trước khi gọi LLM
- `NFR-004` (Độ tin cậy): Cơ chế dự phòng ngoại tuyến (Fallback Engine) khi AI mất mạng
- `NFR-005` (Khả năng bảo trì): Kiến trúc phân tầng tách bạch rõ ràng

### Bước 5: Liệt kê quy tắc nghiệp vụ (Business Rules)
- Phản hồi do AI sinh ra bắt buộc phải có sự kiểm duyệt của nhân viên trước khi gửi khách.
- AI tuyệt đối không cam kết bồi hoàn tài chính sai thẩm quyền.

### Bước 6: Tách bạch các giả định (Assumptions)
Tách riêng những điểm suy đoán ra khỏi yêu cầu cốt lõi.

### Bước 7: Nhận diện điểm mơ hồ và lỗi AI Hallucination (Ambiguities)
Chỉ ra các điểm chưa rõ, mâu thuẫn hoặc không thể kiểm thử. Loại bỏ các yêu cầu bịa đặt do AI tự thêm vào.

### Bước 8: Xây dựng User Stories
Định dạng chuẩn:
*Là một `<vai trò>`, Tôi muốn `<chức năng>`, Để `<lợi ích>`.*

### Bước 9: Xây dựng Tiêu chí chấp nhận (Acceptance Criteria)
Mỗi User Story quan trọng phải có tiêu chí kiểm thử rõ ràng theo chuẩn:
*Given (Bối cảnh ban đầu) - When (Hành động) - Then (Kết quả kỳ vọng).*

### Bước 10: Ma trận truy vết (Traceability)
Đảm bảo mọi User Story và Acceptance Criteria đều truy vết trực tiếp về mã yêu cầu FR/NFR.

## 4. Quy tắc bắt buộc (Rules)
- Không viết mã nguồn (source code) trong bước này.
- Không thiết kế cơ sở dữ liệu hoặc kiến trúc phần mềm.
- Không tự ý bịa đặt quy tắc kinh doanh chưa được ghi nhận trong tài liệu.
- Phân biệt rành mạch giữa yêu cầu đã duyệt và giả định.

## 5. Đầu ra cần tạo (Outputs)
- `docs/requirements.md`
- `docs/user-stories.md`
- `docs/acceptance-criteria.md`
- `docs/requirements-issues.md`

## 6. Tiêu chuẩn kiểm chứng (Verification)
Trước khi bàn giao kết quả, xác minh:
- 100% yêu cầu chức năng và phi chức năng có mã định danh.
- Tất cả User Stories có liên kết truy vết.
- Toàn bộ tiêu chí chấp nhận đều kiểm thử được (testable).
- Các điểm mơ hồ và lỗi bịa đặt được ghi chú rõ ràng.
