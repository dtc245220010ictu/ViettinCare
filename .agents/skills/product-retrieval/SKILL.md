---
name: product-retrieval
description: Truy xuất dữ liệu sản phẩm, dịch vụ ngân hàng số (thẻ, gói tài khoản, hạn mức, lãi suất, biểu phí) và quy trình xử lý tra soát từ cơ sở tri thức bằng SQL tham số hóa.
---
# Kỹ năng Truy xuất Dịch vụ Ngân hàng (Banking Product & FAQ Retrieval Skill)

## 1. Mục tiêu (Objective)
Thực hiện truy vấn cơ sở dữ liệu và kho tri thức FAQ để lấy thông tin các gói dịch vụ ngân hàng số, quy trình tra soát giao dịch, chính sách thẻ, quy định mở khóa Smart OTP và biểu phí dịch vụ dựa trên ý định có cấu trúc của khách hàng.

## 2. Đầu vào (Inputs)
- Ý định người dùng có cấu trúc (Structured Intent) từ module `question-analysis`
- Tiêu chí lọc: Nhóm dịch vụ (`Tài khoản & Đăng nhập`, `Thanh toán & Chuyển tiền`, `Lỗi ứng dụng Ngân hàng số`, `Chính sách & Biểu phí`), từ khóa chuyên ngành ngân hàng

## 3. Quy trình thực hiện (Process)
1. **Xây dựng câu lệnh SQL tham số hóa**:
   ```sql
   SELECT * FROM faqs WHERE category = ?;
   ```
2. **Tìm kiếm từ khóa mở rộng trong kho tri thức ngân hàng**:
   ```sql
   SELECT * FROM faqs WHERE category = ? OR (keywords LIKE ?) LIMIT 3;
   ```
3. **Trích xuất thông tin nghiệp vụ cốt lõi**:
   - Quy trình xử lý lỗi chuyển tiền bị trừ tài khoản
   - Hướng dẫn reset mật khẩu và mở khóa đăng nhập ứng dụng Ngân hàng số
   - Thủ tục khóa thẻ tín dụng khẩn cấp khi nghi ngờ gian lận
   - Quy định về thời gian tra soát liên ngân hàng (từ 1 đến 3 ngày làm việc)
4. **Giới hạn kết quả**: Chỉ lấy từ 1 đến 3 quy trình chuẩn nhất để tối ưu hóa context cho Trợ lý AI.

## 4. Quy tắc bắt buộc (Rules)
- 100% truy vấn dùng parameterized queries.
- Tuyệt đối không tự bịa đặt biểu phí hoặc quy định ngân hàng không tồn tại trong cơ sở dữ liệu.
