---
name: implementation
description: Triển khai mã nguồn phần mềm bằng Python Flask tuân thủ kiến trúc phân tầng, lược đồ CSDL và nguyên tắc viết mã sạch.
---
# Kỹ năng Triển khai Mã nguồn (Implementation Skill)

## 1. Mục tiêu (Objective)
Hiện thực hóa các thành phần phần mềm bằng ngôn ngữ Python (Flask Framework), bảo đảm tuân thủ nghiêm ngặt tài liệu đặc tả yêu cầu, thiết kế kiến trúc và lược đồ cơ sở dữ liệu đã được phê duyệt.

## 2. Đầu vào (Inputs)
Đọc và nắm vững:
- `docs/requirements.md`
- `docs/architecture.md`
- `docs/database-design.md`

## 3. Quy trình thực hiện (Process)
1. **Đọc hiểu đặc tả**: Nắm rõ các ca sử dụng, luồng dữ liệu và quy tắc nghiệp vụ.
2. **Hiểu rõ ranh giới kiến trúc**: Duy trì sự phân tách rõ rệt giữa Routes (tầng giao diện/điều khiển), Services (tầng xử lý nghiệp vụ) và Database DAO (tầng dữ liệu).
3. **Triển khai lần lượt theo từng phân hệ**:
   - Khởi tạo kết nối CSDL và nạp dữ liệu khởi tạo mẫu (`database/db.py`)
   - Phân hệ xác thực & kiểm tra phân quyền RBAC (`services/auth_service.py`, `routes/auth_routes.py`)
   - Phân hệ quản lý khách hàng (`services/customer_service.py`, `routes/customer_routes.py`)
   - Phân hệ quản lý vòng đời ticket (`services/ticket_service.py`, `routes/ticket_routes.py`)
   - Phân hệ Trợ lý AI tăng cường (`services/ai_support_service.py`, `routes/ai_routes.py`) với cơ chế lọc PII và Human Gate
   - Xây dựng giao diện tương tác người dùng (`templates/`, `static/`)
4. **Chạy công cụ kiểm tra tĩnh (Linter & Type Checker)**: Rà soát lỗi cú pháp và chuẩn định dạng PEP 8.
5. **Chạy kiểm thử tự động**: Đảm bảo toàn bộ test case kiểm thử pass 100%.
6. **Kiểm tra Git Diff**: Rà soát các thay đổi, ngăn chặn việc phát sinh code rác hoặc vi phạm phạm vi dự án (scope creep).

## 4. Quy tắc bắt buộc (Rules)
- Không tự ý thay đổi yêu cầu nghiệp vụ hoặc thiết kế kiến trúc đã được duyệt.
- Không hard-code các thông tin bí mật hoặc khóa API trong mã nguồn (bắt buộc dùng `.env`).
- Nếu phát hiện đặc tả kỹ thuật chưa rõ hoặc thiếu dữ liệu, phải dừng lại và yêu cầu con người quyết định thay vì tự suy đoán.
- Luôn xử lý ngoại lệ an toàn, không trả về thông tin lỗi nhạy cảm ra ngoài client.

## 5. Đầu ra cần tạo (Outputs)
- Toàn bộ mã nguồn ứng dụng trong: `models/`, `routes/`, `services/`, `templates/`, `static/`, `app.py`
