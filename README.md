# ViettinCare - Hệ thống Quản lý Hỗ trợ Khách hàng bằng AI-Augmented SDLC (Đề tài 10)

Hệ thống quản lý ticket hỗ trợ khách hàng được xây dựng theo mô hình **AI-Augmented SDLC**, biến AI thành AI Agent có kiểm soát chặt chẽ thông qua các Skill chuyên biệt, cơ chế kiểm duyệt của con người (**Human-in-the-Loop Gate**), bảo vệ thông tin riêng tư (**PII Masking**) và cơ sở tri thức tăng cường (**RAG Support**).

---

## 1. Cấu trúc thư mục chuẩn AI-Augmented SDLC

```
ViettinCare/
├── .agents/
│   └── skills/
│       ├── requirements-analysis/
│       │   └── SKILL.md
│       ├── architecture-design/
│       │   └── SKILL.md
│       ├── database-design/
│       │   └── SKILL.md
│       ├── implementation/
│       │   └── SKILL.md
│       ├── testing/
│       │   └── SKILL.md
│       ├── code-review/
│       │   └── SKILL.md
│       ├── security-review/
│       │   └── SKILL.md
│       ├── ticket-analysis/
│       │   └── SKILL.md
│       ├── faq-retrieval/
│       │   └── SKILL.md
│       ├── context-builder/
│       │   └── SKILL.md
│       ├── ai-prompt/
│       │   └── SKILL.md
│       └── documentation/
│           └── SKILL.md
│
├── docs/
│   ├── customer-requirement.md
│   ├── requirements.md
│   ├── user-stories.md
│   ├── acceptance-criteria.md
│   ├── requirements-issues.md
│   ├── architecture.md
│   ├── architecture-decisions.md
│   ├── database-design.md
│   ├── test-plan.md
│   ├── test-report.md
│   ├── code-review.md
│   ├── security-review.md
│   ├── api.md
│   ├── deployment.md
│   ├── user-guide.md
│   ├── ai-support-requirements.md
│   └── ticket-analysis.md
│
├── database/
│   ├── schema.sql
│   └── db.py
│
├── models/
├── routes/
│   ├── auth_routes.py
│   ├── ticket_routes.py
│   ├── customer_routes.py
│   └── ai_routes.py
│
├── services/
│   ├── auth_service.py
│   ├── customer_service.py
│   ├── ticket_service.py
│   └── ai_support_service.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── tickets.html
│   ├── ticket_detail.html
│   └── customers.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── ticket.js
│
├── tests/
│   ├── test_auth.py
│   ├── test_tickets.py
│   └── test_ai_support.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 2. Các tính năng chính (Đề tài 10)
1. **Quản lý Vòng đời Ticket**: Tạo mới, gán nhân viên phụ trách, cập nhật trạng thái (`New`, `In Progress`, `Waiting Customer`, `Closed`), phân loại danh mục và mức độ ưu tiên.
2. **Quản lý Hồ sơ Khách hàng & Phân quyền RBAC**: Quản trị viên (Admin), Quản lý nhóm (Team Lead), Nhân viên hỗ trợ (Support Agent).
3. **AI Phân loại & Gợi ý Mức ưu tiên**: Phân tích tự động nội dung ticket đề xuất danh mục và độ khẩn cấp.
4. **AI Gợi ý Trả lời (RAG) & Human Gate**: AI đối chiếu cơ sở tri thức FAQ/chính sách và soạn thảo câu trả lời nháp. Nhân viên hỗ trợ xem trước, chỉnh sửa và bấm duyệt trước khi gửi cho khách.
5. **AI Tóm tắt Lịch sử**: Tóm tắt chuỗi trao đổi dài thành 3 gạch đầu dòng then chốt cho nhân viên nhận ca trực mới.
6. **Bảo mật & Quyền riêng tư (PII Sanitization)**: Khử định danh mật khẩu, số thẻ ngân hàng, số điện thoại trước khi truyền dữ liệu ra LLM bên ngoài.

---

## 3. Khởi chạy nhanh
```bash
# 1. Cài đặt phụ thuộc
pip install -r requirements.txt

# 2. Khởi tạo CSDL SQLite mẫu
python database/db.py

# 3. Chạy kiểm thử tự động
python -m pytest -v

# 4. Khởi động Web App
python app.py
```
Truy cập: `http://127.0.0.1:5000` (Đăng nhập với `admin` / `Admin@123` hoặc `agent_lan` / `Agent@123`).

