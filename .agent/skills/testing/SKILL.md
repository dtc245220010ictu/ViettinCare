---
name: testing
description: Lập kế hoạch, thiết kế và thực thi kiểm thử tự động toàn diện (unit test, integration test, xác thực phản hồi AI) cho hệ thống quản lý ticket hỗ trợ.
---
# Kỹ năng Kiểm thử Phần mềm (Testing Skill)

## 1. Mục tiêu (Objective)
Xác minh tính đúng đắn về mặt chức năng, kiểm tra các trường hợp biên, tính an toàn trong phân quyền người dùng và độ tin cậy của các tính năng AI hỗ trợ khách hàng bằng bộ kiểm thử tự động hóa.

## 2. Đầu vào (Inputs)
Đọc và phân tích:
- `docs/requirements.md`
- `docs/user-stories.md`
- `docs/acceptance-criteria.md`

## 3. Quy trình thực hiện (Process)
1. **Phân tích yêu cầu & tiêu chí chấp nhận**: Chuyển đổi các tiêu chí AC thành các ca kiểm thử cụ thể.
2. **Xây dựng kịch bản kiểm thử (Test Scenarios)**:
   - Kịch bản xác thực và phân quyền (Đúng mật khẩu, sai mật khẩu, kiểm tra quyền truy cập route)
   - Kịch bản vòng đời ticket (Tạo mới, chuyển trạng thái `New` -> `In Progress` -> `Waiting Customer` -> `Closed`)
   - Kịch bản Trợ lý AI (Lọc khử định danh PII, phân loại sự cố, gợi ý câu trả lời từ FAQ, cơ chế duyệt của con người)
3. **Thiết kế Ca kiểm thử (Test Cases)**: Bao gồm cả trường hợp kỳ vọng (Positive), trường hợp lỗi (Negative) và trường hợp biên (Edge Cases).
4. **Viết mã kiểm thử tự động**: Viết mã kiểm thử bằng framework `pytest`:
   - `tests/test_auth.py`
   - `tests/test_tickets.py`
   - `tests/test_ai_support.py`
5. **Thực thi bộ kiểm thử (Execution)**: Chạy lệnh `python -m pytest -v`.
6. **Phân tích kết quả & Ghi nhận lỗi (Defects Reporting)**: Báo cáo tỷ lệ pass/fail và phân tích nguyên nhân lỗi nếu có.
7. **Đo lường độ bao phủ yêu cầu (Requirements Coverage)**: Đảm bảo 100% yêu cầu cốt lõi đều có test case kiểm chứng.

## 4. Quy tắc bắt buộc (Rules)
- Tuyệt đối không sửa mã kiểm thử chỉ để làm bài test vượt qua (không cheat test).
- Phải kiểm thử cả hành vi được phép và hành vi bị cấm (ví dụ: nhân viên không được truy cập chức năng admin, phản hồi AI chưa duyệt thì không được gửi cho khách).
- Sử dụng cơ chế giả lập (Mocking / Fallback) cho các dịch vụ AI bên ngoài để bảo đảm kiểm thử chạy ổn định, lặp lại được mà không phụ thuộc vào kết nối mạng.

## 5. Đầu ra cần tạo (Outputs)
- `docs/test-plan.md`
- `docs/test-report.md`
- Các tệp kiểm thử tự động trong thư mục `tests/`
