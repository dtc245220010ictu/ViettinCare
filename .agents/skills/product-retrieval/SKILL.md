---
name: product-retrieval
description: Truy xuất dữ liệu sản phẩm, dịch vụ hoặc hồ sơ tri thức từ cơ sở dữ liệu dựa trên tiêu chí intent có cấu trúc bằng câu lệnh SQL tham số hóa an toàn.
---
# Kỹ năng Truy xuất Dữ liệu (Product / Record Retrieval Skill)

## 1. Mục tiêu (Objective)
Thực hiện truy vấn dữ liệu từ cơ sở dữ liệu quan hệ (MySQL/SQLite) dựa trên các điều kiện lọc có cấu trúc (danh mục, từ khóa, mức giá, mức ưu tiên, chính sách dịch vụ) mà không gây ra rủi ro SQL Injection hoặc tràn bộ nhớ.

## 2. Đầu vào (Inputs)
- Đối tượng JSON chứa ý định người dùng (Structured Intent) từ bước phân tích câu hỏi/ticket
- Các tham số lọc: danh mục nghiệp vụ (`category`), từ khóa (`keywords`), giới hạn kết quả (`limit`)

## 3. Quy trình thực hiện (Process)
1. **Xây dựng câu lệnh SQL tham số hóa**: Sử dụng ký tự giữ chỗ (`?` đối với SQLite hoặc `%s` đối với MySQL), tuyệt đối không cộng chuỗi thô.
2. **Áp dụng bộ lọc danh mục**: Lọc chính xác hoặc theo tiền tố danh mục nghiệp vụ.
3. **Áp dụng tìm kiếm theo từ khóa**: Kết hợp các điều kiện tìm kiếm LIKE trên tiêu đề, nội dung và từ khóa gắn kèm bài viết.
4. **Sắp xếp và giới hạn kết quả**: Sắp xếp theo mức độ phù hợp hoặc ngày cập nhật mới nhất; giới hạn từ 3 đến 5 bản ghi phù hợp nhất.
5. **Xử lý trường hợp không tìm thấy dữ liệu**: Nếu không có bản ghi nào thỏa mãn, trả về danh sách rỗng `[]` thay vì ném ngoại lệ làm gián đoạn chương trình.

## 4. Quy tắc bắt buộc (Rules)
- Tuyệt đối nghiêm cấm việc nối chuỗi trực tiếp giá trị người dùng vào câu lệnh SQL.
- Không được truy xuất toàn bộ cơ sở dữ liệu rồi mới lọc trên bộ nhớ ứng dụng.
- Không gửi toàn bộ dữ liệu thô chưa lọc sang cho LLM.

## 5. Đầu ra cần tạo (Outputs)
- Mảng danh sách các bản ghi từ CSDL dưới dạng Dictionary/JSON.
