---
name: documentation
description: Tạo lập và đồng bộ hóa tài liệu kỹ thuật toàn diện, phản ánh chính xác hiện trạng triển khai, kiến trúc, API và hướng dẫn vận hành của hệ thống.
---
# Kỹ năng Tài liệu hóa Hệ thống (Documentation Skill)

## 1. Mục tiêu (Objective)
Xây dựng và duy trì bộ tài liệu kỹ thuật chuẩn mực, rõ ràng, cập nhật và đồng bộ 100% với mã nguồn, lược đồ cơ sở dữ liệu và các luồng nghiệp vụ thực tế của dự án ViettinCare.

## 2. Đầu vào (Inputs)
Đọc và đối chiếu:
- `requirements.txt`, `app.py`
- Các gói mã nguồn trong `models/`, `routes/`, `services/`, `database/schema.sql`
- Các tệp tài liệu đặc tả hiện có trong thư mục `docs/`

## 3. Quy trình thực hiện (Process)
1. **Kiểm tra hiện trạng mã nguồn**: Rà soát các tính năng, route, bảng CSDL và dịch vụ thực tế đã được lập trình.
2. **Cập nhật `README.md`**:
   - Giới thiệu tổng quan dự án và công nghệ áp dụng.
   - Sơ đồ cấu trúc thư mục chuẩn AI-Augmented SDLC.
   - Hướng dẫn cài đặt, cấu hình biến môi trường và chạy dự án từng bước.
3. **Cập nhật Đặc tả API (`docs/api.md`)**:
   - Liệt kê đầy đủ các endpoint REST API (Auth, Ticket, AI Assistant, Customer).
   - Mô tả chi tiết phương thức HTTP, cấu trúc Request Body JSON, Response Body JSON, mã trạng thái HTTP (200, 400, 401, 404, 500).
4. **Cập nhật Thiết kế Kiến trúc (`docs/architecture.md`)**:
   - Phản ánh chính xác cấu trúc phân tầng và tương tác giữa các service.
   - Bổ sung sơ đồ luồng dữ liệu của Trợ lý AI và điểm kiểm soát Human Gate.
5. **Cập nhật Thiết kế Cơ sở Dữ liệu (`docs/database-design.md`)**:
   - Đồng bộ hóa sơ đồ thực thể liên kết (ERD) và từ điển dữ liệu (Data Dictionary) với tệp `database/schema.sql`.
6. **Cập nhật Hướng dẫn Triển khai (`docs/deployment.md`)**:
   - Hướng dẫn triển khai môi trường cục bộ (Local Development) và môi trường máy chủ sản xuất (Production).
   - Danh mục biến môi trường bắt buộc và cấu hình máy chủ.
7. **Cập nhật Hướng dẫn Sử dụng (`docs/user-guide.md`)**:
   - Hướng dẫn từng bước cho các nhóm người dùng: Quản trị viên (Admin), Quản lý nhóm (Team Lead) và Nhân viên hỗ trợ (Support Agent).
   - Quy trình sử dụng Trợ lý AI và phê duyệt câu trả lời nháp.

## 4. Quy tắc bắt buộc (Rules)
- Tuyệt đối không mô tả các tính năng ảo tưởng hoặc chưa từng được triển khai trong mã nguồn thực tế.
- Mọi câu lệnh hướng dẫn cài đặt phải được kiểm chứng khả năng chạy thành công trên môi trường thực tế.

## 5. Đầu ra cần tạo (Outputs)
- `README.md`
- `docs/api.md`
- `docs/architecture.md`
- `docs/database-design.md`
- `docs/deployment.md`
- `docs/user-guide.md`
- `docs/Bao_Cao_Thuc_Hanh_AI_Augmented_SDLC_De_Tai_10.md`
