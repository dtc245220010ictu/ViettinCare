# ViettinCare - Hệ thống Quản lý Hỗ trợ Khách hàng bằng AI-Augmented SDLC (Đề tài 10)

Hệ thống quản lý ticket hỗ trợ khách hàng được xây dựng theo mô hình **AI-Augmented SDLC**, biến AI thành AI Agent có kiểm soát chặt chẽ thông qua các Skill chuyên biệt, cơ chế kiểm duyệt của con người (**Human-in-the-Loop Gate**), bảo vệ thông tin riêng tư (**PII Masking**) và cơ sở tri thức tăng cường (**RAG Support**).

---

## 1. Cấu trúc thư mục chuẩn AI-Augmented SDLC

```
ViettinCare/
├── .agents/                  # Chứa các Skill của AI-Agent (AI-Augmented SDLC)
│   └── skills/               # Thư mục gốc của tất cả các skill
│       ├── requirements-analysis/   # Phân tích yêu cầu
│       │   └── SKILL.md
│       ├── architecture-design/     # Thiết kế kiến trúc
│       │   └── SKILL.md
│       ├── database-design/         # Thiết kế cơ sở dữ liệu
│       │   └── SKILL.md
│       ├── implementation/          # Triển khai mã nguồn
│       │   └── SKILL.md
│       ├── testing/                 # Kiểm thử phần mềm
│       │   └── SKILL.md
│       ├── code-review/             # Kiểm tra mã nguồn
│       │   └── SKILL.md
│       ├── security-review/         # Kiểm tra bảo mật
│       │   └── SKILL.md
│       ├── ticket-analysis/         # Phân tích ticket hỗ trợ
│       │   └── SKILL.md
│       ├── faq-retrieval/           # Truy xuất câu hỏi thường gặp
│       │   └── SKILL.md
│       ├── context-builder/         # Xây dựng ngữ cảnh cho AI
│       │   └── SKILL.md
│       ├── ai-prompt/               # Quản lý prompt AI
│       │   └── SKILL.md
│       └── documentation/           # Tài liệu hóa
│           └── SKILL.md
│
├── docs/                    # Tài liệu dự án (Đề tài 10)
│   ├── customer-requirement.md      # Yêu cầu của khách hàng
│   ├── requirements.md              # Yêu cầu chức năng & phi chức năng
│   ├── user-stories.md              # Câu chuyện người dùng
│   ├── acceptance-criteria.md       # Tiêu chí chấp nhận
│   ├── requirements-issues.md       # Danh sách issues yêu cầu
│   ├── architecture.md              # Kiến trúc hệ thống
│   ├── architecture-decisions.md    # Quyết định kiến trúc
│   ├── database-design.md           # Thiết kế cơ sở dữ liệu
│   ├── test-plan.md                 # Kế hoạch kiểm thử
│   ├── test-report.md               # Báo cáo kiểm thử
│   ├── code-review.md               # Kiểm tra mã nguồn
│   ├── security-review.md           # Kiểm tra bảo mật
│   ├── api.md                       # Tài liệu API
│   ├── deployment.md                # Hướng dẫn triển khai
│   ├── user-guide.md                # Hướng dẫn sử dụng
│   ├── ai-support-requirements.md   # Yêu cầu hỗ trợ AI
│   └── ticket-analysis.md           # Phân tích ticket hỗ trợ
│
├── database/                # Cơ sở dữ liệu
│   ├── schema.sql             # Định nghĩa cấu trúc bảng
│   └── db.py                  # Kết nối và khởi tạo CSDL
│
├── models/                  # Mô hình dữ liệu (data models)
├── routes/                  # Định tuyến (route) của ứng dụng Flask
│   ├── auth_routes.py         # Đường dẫn xác thực (đăng nhập/đăng xuất)
│   ├── ticket_routes.py       # Đường dẫn quản lý ticket hỗ trợ
│   ├── customer_routes.py     # Đường dẫn quản lý hồ sơ khách hàng
│   └── ai_routes.py           # Đường dẫn tính năng hỗ trợ AI
│
├── services/                # Lớp nghiệp vụ (business logic)
│   ├── auth_service.py        # Xác thực & phân quyền RBAC
│   ├── customer_service.py    # Quản lý hồ sơ khách hàng
│   ├── ticket_service.py      # Quản lý vòng đời ticket
│   └── ai_support_service.py  # Tính năng hỗ trợ AI
│
├── templates/               # Mẫu giao diện HTML (Jinja2)
│   ├── base.html              # Mẫu cơ sở
│   ├── login.html             # Trang đăng nhập
│   ├── dashboard.html         # Trang điều khiển
│   ├── tickets.html           # Quản lý ticket
│   ├── ticket_detail.html     # Chi tiết ticket
│   └── customers.html         # Quản lý khách hàng
│
├── static/                  # Tài nguyên tĩnh (CSS, JS)
│   ├── css/
│   │   └── style.css          # Định dạng giao diện
│   └── js/
│       └── ticket.js          # JavaScript xử lý ticket
│
├── tests/                   # Kiểm thử tự động
│   ├── test_auth.py           # Kiểm thử chức năng xác thực
│   ├── test_tickets.py        # Kiểm thử quản lý ticket
│   └── test_ai_support.py     # Kiểm thử tính năng hỗ trợ AI
│
├── app.py                     # Điểm vào chính của ứng dụng Flask
├── requirements.txt           # Danh sách thư viện phụ thuộc
└── README.md                  # Tài liệu chính của dự án
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

