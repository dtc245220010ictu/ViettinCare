---
name: tour-retrieval
description: Thực hiện truy vấn cơ sở dữ liệu để lấy các bản ghi nghiệp vụ (tour du lịch, vé dịch vụ, ticket hỗ trợ) thỏa mãn điều kiện tìm kiếm bằng câu lệnh tham số hóa.
---
# Kỹ năng Truy xuất Nghiệp vụ Dịch vụ (Tour / Service Retrieval Skill)

## 1. Mục tiêu (Objective)
Thực thi truy vấn cơ sở dữ liệu quan hệ một cách bảo mật, chính xác nhằm lấy các thông tin dịch vụ, danh sách ticket hỗ trợ hoặc câu hỏi thường gặp (FAQ) phù hợp với tiêu chí tìm kiếm của người dùng.

## 2. Đầu vào (Inputs)
- Các tham số tìm kiếm: mã dịch vụ/ticket, danh mục, từ khóa tìm kiếm, trạng thái, mức độ ưu tiên
- Giới hạn số lượng bản ghi trả về

## 3. Quy trình thực hiện (Process)
1. Xác thực các tham số đầu vào, đảm bảo tên cột lọc nằm trong danh sách trắng (whitelist).
2. Xây dựng câu truy vấn `SELECT` với các tham số giữ chỗ `?`.
3. Áp dụng các mệnh đề lọc:
   - `WHERE category = ?`
   - `AND status = ?`
   - `AND (title LIKE ? OR description LIKE ?)`
4. Áp dụng sắp xếp theo mức độ ưu tiên khẩn cấp (`Urgent` -> `High` -> `Medium` -> `Low`) và thời gian tiếp nhận mới nhất.
5. Giới hạn số lượng bản ghi tối đa để bảo vệ tài nguyên hệ thống.
6. Chuyển đổi kết quả truy vấn thành danh sách các đối tượng dữ liệu sạch.

## 4. Quy tắc bắt buộc (Rules)
- 100% câu truy vấn đều phải dùng tham số hóa, ngăn chặn triệt để SQL Injection.
- Luôn xử lý trường hợp không tìm thấy dữ liệu bằng việc trả về danh sách rỗng, không làm phát sinh lỗi hệ thống.
