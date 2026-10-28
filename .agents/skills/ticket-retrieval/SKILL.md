---
name: ticket-retrieval
description: Truy xuất dữ liệu ticket hỗ trợ khách hàng ngân hàng, lịch sử khiếu nại giao dịch và hồ sơ tài khoản bằng câu lệnh SQL tham số hóa an toàn.
---
# Kỹ năng Truy xuất Ticket CSKH Ngân hàng (Banking Ticket Retrieval Skill)

## 1. Mục tiêu (Objective)
Thực thi truy vấn cơ sở dữ liệu quan hệ một cách bảo mật, chính xác nhằm lấy danh sách ticket khiếu nại, sự cố giao dịch ngân hàng số hoặc lịch sử phản hồi theo tiêu chí tìm kiếm của nhân viên tổng đài và khách hàng.

## 2. Đầu vào (Inputs)
- Tham số tìm kiếm: mã ticket (`TCK-...`), số điện thoại/email khách hàng, số tài khoản, danh mục nghiệp vụ (Tài khoản, Chuyển tiền, Smart OTP, Thẻ tín dụng, Biểu phí), trạng thái xử lý (`New`, `In Progress`, `Waiting Customer`, `Closed`), mức độ ưu tiên.
- Phân trang và giới hạn số lượng bản ghi trả về.

## 3. Quy trình thực hiện (Process)
1. Xác thực các tham số đầu vào (phòng chống Parameter Tampering).
2. Xây dựng câu truy vấn `SELECT` với các tham số giữ chỗ `?` (Parameterized SQL).
3. Áp dụng các mệnh đề lọc nghiệp vụ ngân hàng:
   - `WHERE category = ?` (Lọc theo mảng nghiệp vụ: Tài khoản & Đăng nhập, Thanh toán & Chuyển tiền, Thẻ & Hạn mức, Smart OTP)
   - `AND status = ?` (Mới tiếp nhận, Đang tra soát, Chờ khách hàng, Đã giải quyết)
   - `AND (title LIKE ? OR description LIKE ?)`
4. Sắp xếp ưu tiên theo mức độ rủi ro tài chính (`Urgent` ưu tiên hàng đầu) và thời gian phát sinh sự cố.
5. Giới hạn số lượng bản ghi trả về (tránh tràn bộ nhớ).
6. Khử định danh các dữ liệu nhạy cảm trước khi trả về view.

## 4. Quy tắc bắt buộc (Rules)
- 100% câu truy vấn phải dùng cú pháp tham số hóa, ngăn chặn triệt để SQL Injection.
- Luôn kiểm tra quyền truy cập (Authorization): Nhân viên chỉ được xem ticket trong phạm vi phân công hoặc nhóm trực.
- Trả về danh sách rỗng an toàn nếu không tìm thấy bản ghi, không ném ngoại lệ làm gián đoạn hệ thống.

## 5. Đầu ra cần tạo (Outputs)
- Mảng dữ liệu các bản ghi ticket ngân hàng sạch, có cấu trúc.

