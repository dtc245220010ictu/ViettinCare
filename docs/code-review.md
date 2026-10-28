# Báo cáo đánh giá mã nguồn (Code Review Report) - Đề tài 10

## 1. Phương pháp & Mục tiêu
Sử dụng bộ tiêu chuẩn `code-review` skill để đánh giá mã nguồn về: tính đúng đắn, tuân thủ kiến trúc phân tầng, phân tách trách nhiệm (Separation of Concerns), xử lý ngoại lệ và chất lượng mã nguồn.

## 2. Kết quả đánh giá theo phân loại rủi ro

| Mức độ | Vị trí | Vấn đề phát hiện | Giải pháp đã khắc phục | Trạng thái |
|---|---|---|---|---|
| **CRITICAL** | `services/ai_support_service.py` | Regex lọc PII ban đầu không bắt được chuỗi "mật khẩu của tôi là Pass@...", có nguy cơ rò rỉ secret lên máy chủ LLM công cộng. | Bổ sung regex nhận diện pattern `(?:của tôi là\|là)?\s*` và nhận diện riêng `Pass@\w+`. Đã viết test case kiểm chứng lại. | **ĐÃ XỬ LÝ** |
| **HIGH** | `routes/ai_routes.py` | Nguy cơ nhân viên bấm gửi duyệt nhưng nội dung bị rỗng hoặc ticket không tồn tại gây crash máy chủ. | Thêm validate dữ liệu `not ticket_id or not approved_content` và trả về HTTP 400 Bad Request kèm thông báo lỗi rõ ràng. | **ĐÃ XỬ LÝ** |
| **MEDIUM** | `services/ticket_service.py` | Chưa sắp xếp ưu tiên hiển thị theo mức độ khẩn cấp (Urgent lên đầu). | Bổ sung mệnh đề `ORDER BY CASE t.priority WHEN 'Urgent' THEN 1 WHEN 'High' THEN 2 ...` | **ĐÃ XỬ LÝ** |
| **LOW** | `templates/base.html` | Thẻ badge trạng thái hiển thị chưa đồng bộ màu sắc chuẩn thiết kế. | Chuẩn hóa bảng màu CSS cho các trạng thái New, In Progress, Waiting Customer, Closed. | **ĐÃ XỬ LÝ** |

## 3. Đánh giá tuân thủ kiến trúc (Architecture Compliance)
- Mã nguồn tuân thủ triệt để nguyên tắc phân tầng: Controller (`routes/`) -> Service (`services/`) -> Data Access (`database/`).
- Tầng AI không bao giờ được phép thực thi SQL tự do mà luôn giao tiếp qua intermediate representation và context injection.

