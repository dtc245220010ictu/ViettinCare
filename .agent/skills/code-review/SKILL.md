---
name: code-review
description: Thực hiện đánh giá mã nguồn có cấu trúc, khách quan, tập trung vào tính đúng đắn, tuân thủ yêu cầu, ranh giới kiến trúc, khả năng bảo trì và xử lý ngoại lệ.
---
# Kỹ năng Đánh giá Mã nguồn (Code Review Skill)

## 1. Mục tiêu (Objective)
Thẩm định chất lượng mã nguồn dự án, phát hiện sớm các lỗi tiềm ẩn (bugs), các đoạn mã gây mùi (code smells), các vi phạm kiến trúc phân tầng và bảo đảm tiêu chuẩn viết mã trước khi phát hành phiên bản.

## 2. Đầu vào (Inputs)
Đọc và rà soát:
- `docs/requirements.md`
- `docs/architecture.md`
- Toàn bộ mã nguồn triển khai trong `app.py`, `models/`, `routes/`, `services/`, `database/`

## 3. Quy trình thực hiện (Process)
1. **Kiểm tra tính đúng đắn (Correctness)**: Mã nguồn có thực thi đúng và đủ các chức năng nghiệp vụ quy định không?
2. **Kiểm tra tuân thủ yêu cầu (Requirements Compliance)**: Có tính năng thừa tự chế hoặc thiếu hụt tính năng đã cam kết không?
3. **Kiểm tra tuân thủ kiến trúc (Architecture Compliance)**: Có tình trạng gọi ngược tầng, truy vấn SQL trực tiếp từ view/template hoặc để AI tự ý gọi DB không?
4. **Kiểm tra chất lượng và khả năng bảo trì (Maintainability)**: Đảm bảo tuân thủ PEP 8, nguyên tắc DRY (Don't Repeat Yourself), đặt tên hàm và biến tường minh, phân tách hàm ngắn gọn.
5. **Kiểm tra xử lý ngoại lệ & Logging (Error Handling)**: Có khối `try-except` an toàn không? Có bắt lỗi chung chung làm ẩn dấu vết sự cố không?
6. **Kiểm tra truy cập cơ sở dữ liệu (Database Patterns)**: Rà soát tránh lỗi N+1 truy vấn; đảm bảo 100% truy vấn đều dùng câu lệnh tham số hóa.
7. **Kiểm tra chất lượng bộ test (Test Quality)**: Test case có thực sự kiểm tra logic cốt lõi không?
8. **Phân loại mức độ phát hiện**:
   - `CRITICAL`: Lỗi nghiêm trọng, có nguy cơ sập hệ thống hoặc lộ bí mật, phải sửa ngay.
   - `HIGH`: Lỗi logic hoặc nguy cơ mất ổn định cao.
   - `MEDIUM`: Đoạn mã cần tối ưu, trường hợp biên chưa bắt.
   - `LOW`: Vấn đề về thẩm mỹ mã nguồn, đặt tên hoặc chú thích.

## 4. Quy tắc bắt buộc (Rules)
- Không chỉnh sửa trực tiếp mã nguồn trong lúc thực hiện review.
- Mọi đánh giá phải có dẫn chứng cụ thể kèm tên tệp và dòng mã tương ứng.

## 5. Đầu ra cần tạo (Outputs)
- `docs/code-review.md`
