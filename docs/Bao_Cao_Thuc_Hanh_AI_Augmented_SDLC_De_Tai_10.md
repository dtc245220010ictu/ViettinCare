# XÂY DỰNG HỆ THỐNG QUẢN LÝ HỖ TRỢ KHÁCH HÀNG BẰNG AI-AUGMENTED SDLC
*(Áp dụng cho Đề tài 10: Hệ thống Quản lý Hỗ trợ Khách hàng có tích hợp AI - ViettinCare)*

---

## A. TIÊU CHÍ ĐÁNH GIÁ BÀI THỰC HÀNH

Điểm cốt lõi của bài thực hành này là không dùng Codex như một công cụ sinh code, mà tổ chức Codex thành một AI Agent thực hiện các quy trình SDLC có kiểm soát bằng Skills, Tools và MCP, với các điểm kiểm soát của con người (Human Gate). Cách tiếp cận này cũng phù hợp với định hướng hiện tại của OpenAI về Codex: hiểu codebase, xây dựng tính năng, kiểm thử, review và tự động hóa các workflow lặp lại; OpenAI cũng đã có use case chính thức về việc lưu các workflow lặp lại thành Skills. 

Đánh giá năng lực sử dụng AI trong SDLC, thay vì chỉ đánh giá "AI đã viết được bao nhiêu code".

| Nội dung | Điểm |
|---|---|
| Phân tích yêu cầu | 1.0 |
| Xây dựng Requirements Skill | 1.0 |
| Thiết kế kiến trúc | 1.0 |
| Database Skill + CSDL | 1.0 |
| Coding Skill + implementation | 1.5 |
| Testing Skill + test evidence | 1.5 |
| Review + Security Skill | 1.0 |
| Documentation Skill | 0.5 |
| Sử dụng Tools/MCP | 0.5 |
| Human verification + báo cáo quá trình AI | 1.0 |
| **Tổng** | **10.0** |

Sinh viên phải nộp cả:
1. `SKILL.md` (Toàn bộ 12 Skill trong `.agents/skills/`)
2. Prompt/task đã giao cho Codex
3. Artifact Codex tạo ra (các file trong `docs/`)
4. Kết quả kiểm thử (Test Plan, Test Report, evidence 8/8 test passed)
5. Review report (`docs/code-review.md`)
6. Security report (`docs/security-review.md`)
7. Các lỗi AI phát hiện được & Hallucination đã ngăn chặn
8. Những chỉnh sửa do con người thực hiện (Human Gate)
9. Git history (54 files committed)

---

## B. MÔ HÌNH TỔNG QUÁT VÒNG ĐỜI PHÁT TRIỂN PHẦN MỀM ĐƯỢC TĂNG CƯỜNG BẰNG TRÍ TUỆ NHÂN TẠO AI

```
                        AI-Augmented SDLC
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
    [Con người]              [AI/LLM]               [Công cụ]
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                ▼
                       [Phát triển phần mềm]
                                │
    ┌──────────────┬────────────┼─────────────┬─────────────┐
    ▼              ▼            ▼             ▼             ▼
Requirements     Design       Coding       Testing     Deployment
    └──────────────┴────────────┼─────────────┴─────────────┘
                                ▼
                          [Maintenance]
```

Nếu sử dụng Codex làm công cụ AI hỗ trợ phát triển phần mềm, ta có mô hình:

```
                        AI-Augmented SDLC
                                │
                                ▼
                              Codex
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
      Skills                 Context                 Tools
         │                      │                      │
 ┌───────┴───────┐      ┌───────┴───────┐      ┌───────┴───────┐
 │Quy trình chuẩn│      │  Source code  │      │   Terminal    │
 │ Coding rules  │      │   Database    │      │      Git      │
 │ Testing rules │      │   Documents   │      │  Test runner  │
 └───────┬───────┘      └───────┬───────┘      └───────┬───────┘
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                ▼
                        Software Project
```

---

## C. HỆ THỐNG QUẢN LÝ HỖ TRỢ KHÁCH HÀNG BẰNG AI-AUGMENTED SDLC VỚI CODEX

### 1. Mục tiêu
Sau bài thực hành, sinh viên có khả năng:
1. Phân tích yêu cầu phần mềm với sự hỗ trợ của AI.
2. Xây dựng và sử dụng Skill cho từng hoạt động SDLC.
3. Sử dụng Codex như một AI Agent thay vì chỉ sử dụng AI để sinh mã nguồn.
4. Phân biệt Skill, Tool và MCP.
5. Sử dụng Codex xuyên suốt các giai đoạn:
   - Requirements Engineering
   - Architecture Design
   - Database Design
   - Implementation
   - Testing
   - Code Review
   - Security Review
   - Documentation
6. Tích hợp các tính năng AI hỗ trợ khách hàng: AI phân loại ticket & mức ưu tiên, gợi ý câu trả lời nháp từ FAQ (RAG), tóm tắt lịch sử trao đổi.
7. Kiểm chứng độc lập kết quả do AI tạo ra.
8. Thiết lập cơ chế kiểm soát của con người (Human Gate) bắt buộc phê duyệt phản hồi AI trước khi gửi cho khách.
9. Quản lý Skill cùng với mã nguồn bằng Git.
10. Bảo vệ quyền riêng tư người dùng thông qua cơ chế khử định danh dữ liệu cá nhân (PII Masking).

---

### PHẦN I. XÁC ĐỊNH BÀI TOÁN

#### Bước 1. Xác định bài toán
Ta xây dựng: **Hệ thống quản lý hỗ trợ khách hàng có tích hợp AI (ViettinCare)**.

Hệ thống có bốn nhóm người dùng:
1. **Quản trị viên (Admin)**: Đăng nhập; quản lý người dùng; cấu hình phân quyền; quản lý cơ sở tri thức FAQ; theo dõi toàn bộ hệ thống.
2. **Quản lý nhóm (Team Lead)**: Phân công ticket cho nhân viên; theo dõi tiến độ xử lý; xem báo cáo SLA, thời gian xử lý và nhóm vấn đề phổ biến.
3. **Nhân viên hỗ trợ (Support Agent)**: Đăng nhập; xem danh sách ticket được phân công; cập nhật trạng thái (Mới, Đang xử lý, Chờ khách hàng, Đã đóng); trao đổi ý kiến và đính kèm mô tả; sử dụng Trợ lý AI để nhận gợi ý câu trả lời; phê duyệt hoặc chỉnh sửa câu trả lời AI trước khi gửi khách.
4. **Khách hàng (Customer)**: Gửi yêu cầu hỗ trợ (ticket); theo dõi trạng thái xử lý; trao đổi phản hồi với nhân viên hỗ trợ.

---

### PHẦN II. CHUẨN BỊ MÔI TRƯỜNG

#### Bước 2. Tạo project: Mở VS Code -> Terminal
```bash
# Tạo thư mục
mkdir ViettinCare
cd ViettinCare

# Khởi tạo Git
git init

# Tạo môi trường Python
python -m venv venv

# Kích hoạt môi trường (Windows PowerShell)
venv\Scripts\activate

# Cài các thư viện cơ bản
pip install flask werkzeug python-dotenv pytest google-generativeai

# Lưu dependencies
pip freeze > requirements.txt
```

---

### PHẦN III. TẠO CẤU TRÚC AI-AUGMENTED SDLC

#### Bước 3. Tạo cấu trúc thư mục (Dùng Codex để tạo)
```
ViettinCare/
├── .git/
├── .agents/
│    └── skills/
├── docs/
├── database/
├── models/
├── routes/
├── services/
├── templates/
├── static/
├── tests/
├── app.py
├── requirements.txt
└── .gitignore
```
Đây là lúc bắt đầu đưa AI-Augmented SDLC vào project.

---

### PHẦN IV. XÂY DỰNG REQUIREMENTS SKILL

#### Bước 4. Tạo Skill phân tích yêu cầu
Tạo thư mục: `.agents/skills/requirements-analysis/`  
Tạo file: `.agents/skills/requirements-analysis/SKILL.md`  

Quy định cấu trúc:
- Inputs: `customer requirements`, `business requirements`, `SLA constraints`
- Process: 10 bước chuẩn hóa từ Identify stakeholders đến Traceability
- Rules: Không viết code, không thiết kế CSDL, không bịa đặt quy tắc kinh doanh chưa ghi nhận
- Outputs: `docs/requirements.md`, `docs/user-stories.md`, `docs/acceptance-criteria.md`, `docs/requirements-issues.md`
- Verification: Kiểm tra mã định danh FR/NFR, tính kiểm thử được của tiêu chí chấp nhận.

---

### PHẦN V. CUNG CẤP YÊU CẦU CHO CODEX

#### Bước 5. Tạo yêu cầu của khách hàng
Tạo file: `docs/customer-requirement.md`  
Nội dung:
- Doanh nghiệp cần hệ thống quản lý hỗ trợ khách hàng, giải quyết tình trạng bỏ sót ticket và tốn thời gian đọc lại lịch sử.
- Nhân viên cần đăng nhập, phân quyền, quản lý khách hàng, tạo ticket, cập nhật trạng thái, phân công và trao đổi.
- Tích hợp AI phân loại ticket, gợi ý câu trả lời từ FAQ và tóm tắt lịch sử trao đổi.
- Bắt buộc có cơ chế nhân viên kiểm duyệt câu trả lời của AI trước khi gửi cho khách.

---

### PHẦN VI. YÊU CẦU CODEX SỬ DỤNG SKILL

#### Bước 6. Chạy Codex
Đưa yêu cầu:
> Hãy thực hiện Requirements Engineering cho project này.  
> Sử dụng `requirements-analysis` skill.  
> Đọc: `docs/customer-requirement.md`  
> Thực hiện đúng quy trình được quy định trong skill.  
> Không viết source code.  
> Tạo:  
> - `docs/requirements.md`  
> - `docs/user-stories.md`  
> - `docs/acceptance-criteria.md`  
> - `docs/requirements-issues.md`  
> Sau khi hoàn thành, giải thích: Skill đã sử dụng, Artifacts đã tạo, Requirements còn chưa rõ, Giả định đã dùng.

---

### PHẦN VII. KIỂM CHỨNG KẾT QUẢ

#### Bước 7. Không chấp nhận ngay kết quả của AI
Sinh viên mở `docs/requirements.md` và kiểm tra:
- FR-001: Đăng nhập và phân quyền (Admin, Team Lead, Agent).
- FR-002: Quản lý khách hàng và thông tin liên hệ.
- FR-003: Tạo ticket, cập nhật tiêu đề, mô tả, mức ưu tiên, trạng thái.
- FR-004: Phân công ticket cho nhân viên xử lý.
- FR-005: Quản lý lịch sử trao đổi và file đính kèm ở mức mô tả.
- FR-006: Tìm kiếm/lọc ticket theo khách hàng, trạng thái, mức ưu tiên, thời gian.
- FR-007: Thống kê số ticket, thời gian xử lý, nhóm vấn đề thường gặp.
- FR-008: AI phân loại ticket theo nhóm vấn đề và mức ưu tiên gợi ý.
- FR-009: AI gợi ý câu trả lời dựa trên mô tả ticket và lịch sử trao đổi (RAG).
- FR-010: Cơ chế nhân viên duyệt câu trả lời AI trước khi gửi (Human Gate).
- FR-011: AI tóm tắt lịch sử hỗ trợ dài thành các ý chính.

**Kiểm tra AI Hallucination / Requirement Invention:**
Kiểm tra xem Codex có tự ý thêm:
> "Khách hàng có thể tự động nhận hoàn tiền vào tài khoản ngân hàng khi AI phát hiện lỗi thanh toán."
hay không. Nếu có thì đây là AI hallucination, phải loại bỏ ngay vì mọi quyết định tài chính phải có sự xét duyệt ngoại tuyến của con người.

---

### PHẦN VIII. HUMAN GATE 1

Không được: `Requirements -> Codex -> Architecture`  
Mà phải: `Requirements -> Codex -> Human Verification -> APPROVED -> Architecture`

```
Requirements Review
Reviewer: Student / Lead QA
Status: APPROVED
Checked:
[X] Functional requirements (FR-001 -> FR-011)
[X] Non-functional requirements (NFR-001 -> NFR-006)
[X] User stories (US-001 -> US-011)
[X] Acceptance criteria (AC-001 -> AC-009)
[X] Ambiguities & Hallucination eliminated
Approved for Architecture Design.
```

---

### PHẦN IX. XÂY DỰNG ARCHITECTURE SKILL

#### Bước 8. Tạo Skill
Tạo: `.agents/skills/architecture-design/SKILL.md`  
Quy định: Inputs -> 10 bước phân tích kiến trúc -> Rules -> Outputs (`docs/architecture.md`, `docs/architecture-decisions.md`) -> Verification.

---

### PHẦN X. SỬ DỤNG ARCHITECTURE SKILL

#### Bước 9. Yêu cầu Codex
Codex tạo kiến trúc hệ thống ViettinCare:

```
                            Web Browser
           (Support Workspace, Ticket Detail, AI Panel)
                                │
                                ▼
                        Flask Application
                  (Auth & RBAC, REST API Router)
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
    Auth Service         Customer Service        Ticket Service
         │                      │                      │
         │                      │                      ▼
         │                      │              AI Support Service
         │                      │                      │
         │                      │            ┌─────────┴─────────┐
         │                      │            ▼                   ▼
         │                      │       FAQ Retriever      Context Builder
         │                      │            │                   │
         │                      │            └─────────┬─────────┘
         │                      │                      ▼
         ▼                      ▼                 Gemini Service
+─────────────────────────────────────────+            │
|       Relational Database (SQLite)      |            ▼
| (users, customers, tickets, faqs, logs) |       Gemini LLM API
+─────────────────────────────────────────+
```

---

### PHẦN XI. HUMAN GATE 2

Sinh viên kiểm tra đối chiếu:
```
Requirement
    ↓
Architecture component
```
Ví dụ:
- `FR-003 Tạo/sửa Ticket` -> `Ticket Service` -> `SQLite`
- `FR-008 AI Phân loại` -> `Ticket Analyzer` -> `AI Support Service`
- `FR-009 AI Gợi ý trả lời` -> `FAQ Retriever` -> `Context Builder` -> `Gemini API`
- `FR-010 Nhân viên duyệt` -> `AI Routes (/api/ai/approve-and-send)` -> `Ticket Service`

Nếu không tìm được component đáp ứng requirement -> kiến trúc chưa đạt. Kết quả: **APPROVED**.

---

### PHẦN XII. DATABASE SKILL

#### Bước 10. Tạo Skill
Tạo: `.agents/skills/database-design/SKILL.md`  
Quy định: Requirements -> Entities -> Relationships -> Normalization -> PK/FK -> Constraints -> Indexes -> SQL Schema -> Verification.

Các thực thể: `users`, `customers`, `tickets`, `ticket_comments`, `faqs`, `ai_logs`.  
Quan hệ:
- `customers` 1 ───────── N `tickets`
- `users` 1 ───────── N `tickets` (assigned_to)
- `tickets` 1 ───────── N `ticket_comments`
- `tickets` 1 ───────── N `ai_logs`

---

### PHẦN XIII. YÊU CẦU CODEX THIẾT KẾ DATABASE

#### Bước 11
Codex tạo:
- `docs/database-design.md`
- `database/schema.sql`

---

### PHẦN XIV. KIỂM TRA DATABASE

Sinh viên kiểm tra cấu trúc bảng `tickets`:
```
tickets
   ├── ticket_number (UNIQUE, VARCHAR)
   ├── customer_id (FK -> customers)
   ├── title (VARCHAR, NOT NULL)
   ├── description (TEXT, NOT NULL)
   ├── category (VARCHAR)
   ├── priority (CHECK IN 'Low', 'Medium', 'High', 'Urgent')
   ├── status (CHECK IN 'New', 'In Progress', 'Waiting Customer', 'Closed')
   └── assigned_to (FK -> users)
```
Đồng thời kiểm tra `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, `CHECK`, và `INDEX` tối ưu truy vấn.

---

### PHẦN XV. IMPLEMENTATION SKILL

#### Bước 12. Tạo Skill
`.agents/skills/implementation/SKILL.md`  
Quy định: Read Specification -> Understand Architecture -> Understand Database -> Implement -> Run Linter -> Run Tests -> Review Diff.

---

### PHẦN XVI. BẮT ĐẦU LẬP TRÌNH

#### Bước 13. Yêu cầu Codex
Triển khai hệ thống quản lý cốt lõi:
1. Kết nối CSDL và dữ liệu mẫu (`database/db.py`)
2. Xác thực và phân quyền (`services/auth_service.py`, `routes/auth_routes.py`)
3. Quản lý khách hàng (`services/customer_service.py`, `routes/customer_routes.py`)
4. Quản lý Ticket CRUD và chuyển đổi trạng thái (`services/ticket_service.py`, `routes/ticket_routes.py`)
5. Bảng điều khiển phân tích SLA (`templates/dashboard.html`)

Chưa triển khai các chức năng AI ở bước này.

---

### PHẦN XVII. TESTING SKILL

#### Bước 14. Tạo Testing Skill
`.agents/skills/testing/SKILL.md`  
Quy định: Requirements -> Test Scenario -> Test Case -> Automated Test -> Execution -> Result -> Defect.

---

### PHẦN XVIII. KIỂM THỬ

#### Bước 15. Yêu cầu Codex
Tạo:
- `tests/test_auth.py`
- `tests/test_tickets.py`
- `tests/test_ai_support.py`
- `docs/test-plan.md`
- `docs/test-report.md`

Chạy kiểm thử: `python -m pytest -v`  
Kết quả: **8/8 test cases PASSED (100%)**.

---

### PHẦN XIX. CODE REVIEW SKILL

#### Bước 16. Tạo Skill
`.agents/skills/code-review/SKILL.md`  
Quy định tiêu chuẩn đánh giá: Correctness, Requirements Compliance, Architecture Compliance, Maintainability, Security, Performance, Testing.

---

### PHẦN XX. REVIEW CODE

#### Bước 17
Codex tạo: `docs/code-review.md`.  
Phát hiện lỗi regex PII và xử lý validate rỗng tại API duyệt phản hồi; đã sửa chữa và kiểm tra lại.

---

### PHẦN XXI. SECURITY SKILL

#### Bước 18. Tạo Skill
`.agents/skills/security-review/SKILL.md`  
Checklist: SQL Injection, XSS, CSRF, Authentication, Authorization, Secrets, Input Validation, PII Masking, Hallucination Prevention.

---

### PHẦN XXII. SECURITY REVIEW

#### Bước 19
Codex tạo: `docs/security-review.md`.  
Xác nhận an toàn toàn diện: 100% truy vấn dùng parameterized queries; không hard-code API key; dữ liệu cá nhân nhạy cảm được che trước khi gọi AI.

---

### PHẦN XXIII. TRỢ LÝ AI HỖ TRỢ KHÁCH HÀNG (AI SUPPORT ASSISTANT)

Sau khi core system ổn định, ta mới triển khai trợ lý AI hỗ trợ khách hàng.

#### 1. Xác định yêu cầu AI hỗ trợ
Tạo file: `docs/ai-support-requirements.md`  
Yêu cầu AI phân tích ticket, trích xuất cấu trúc vấn đề, tra cứu FAQ, soạn câu trả lời nháp cho nhân viên duyệt, tóm tắt lịch sử trao đổi và ẩn dữ liệu nhạy cảm PII.

#### 2. Sử dụng Requirements Skill
Phân tích yêu cầu chức năng:
- `FR-AI-001`: Phân loại ticket và đề xuất mức ưu tiên.
- `FR-AI-002`: Tra cứu cơ sở tri thức FAQ/chính sách hỗ trợ (RAG).
- `FR-AI-003`: Soạn thảo câu trả lời nháp chuẩn mực, thân thiện.
- `FR-AI-004`: Cơ chế Human Gate bắt buộc nhân viên hỗ trợ duyệt trước khi gửi.
- `FR-AI-005`: Tóm tắt lịch sử trao đổi dài thành 3 gạch đầu dòng.

#### 3. Xác định User Story & Acceptance Criteria
Ví dụ:
```
US-AI-001:
As a support agent,
I want AI to suggest a draft response based on verified FAQs,
so that I can respond accurately and quickly while keeping full review control.

Acceptance Criteria (AC-AI-001):
Given: Database contains FAQ for "Reset password email delay".
When: Agent clicks "AI Soạn thảo Câu trả lời Nháp" on Ticket #1001.
Then: System retrieves the relevant FAQ, feeds sanitized context to Gemini,
And: Displays editable draft in the UI editor.
And: The response is NOT sent until human clicks "Phê duyệt & Gửi".
```

#### 4. Thiết kế kiến trúc Trợ lý AI
Luồng dữ liệu:
```
Ticket Details -> Sanitizer -> Ticket Analyzer -> FAQ Retriever -> Context Builder -> Prompt Builder -> Gemini Service -> Draft -> Human Gate -> Sent
```

#### 5. Thiết kế Ticket Context Analyzer
Intermediate representation JSON:
```json
{
  "category": "Tài khoản & Đăng nhập",
  "suggested_priority": "High",
  "keywords": ["đổi mật khẩu", "reset", "email"],
  "sanitized_summary": "Khách hàng không đăng nhập được sau khi đổi mật khẩu..."
}
```
Tạo Skill: `.agents/skills/ticket-analysis/SKILL.md` và `docs/ticket-analysis.md`.

#### 6. FAQ Knowledge Retrieval
Chuyển đổi intent thành SQL tham số hóa:
```sql
SELECT * FROM faqs WHERE category = ? AND keywords LIKE ?;
```
Tạo Skill: `.agents/skills/faq-retrieval/SKILL.md`.

#### 7. Implement Retrieval
Triển khai `retrieve_faqs(intent)` trong `services/ai_support_service.py`.

#### 8. Context Builder
Tạo Skill: `.agents/skills/context-builder/SKILL.md`.  
Đóng gói thông tin ticket, 4 bình luận gần nhất và FAQ liên quan, giới hạn dưới 2000 ký tự.

#### 9. Prompt Builder
Tạo Skill: `.agents/skills/ai-prompt/SKILL.md`.  
System prompt:
> "Bạn là Trợ lý AI hỗ trợ nhân viên chăm sóc khách hàng ViettinCare. Chỉ soạn thảo câu trả lời nháp để nhân viên duyệt. Không cam kết hoàn tiền hoặc chính sách nếu chưa có dữ liệu cung cấp."

#### 10. Gemini Service
Triển khai `generate_with_gemini()` an toàn, đọc key từ `.env`, có Fallback Engine dự phòng khi ngoại tuyến.

#### 11. Kết hợp thành AI Support Service
Tích hợp toàn bộ pipeline vào `services/ai_support_service.py`.

#### 12. Tạo Flask API
Các endpoints trong `routes/ai_routes.py`:
- `POST /api/ai/classify`
- `POST /api/ai/suggest`
- `POST /api/ai/summarize`
- `POST /api/ai/approve-and-send` *(Human Gate)*
- `POST /api/ai/apply-classification`

#### 13. Xây dựng giao diện Hỗ trợ & Trợ lý AI
Tạo:
- `templates/ticket_detail.html`: Giao diện 2 cột với bảng điều khiển Trợ lý AI, tab Gợi ý nháp, Tóm tắt, Phân loại và banner Human Gate cảnh báo.
- `static/css/style.css`: Bảng màu hiện đại, responsive, thẻ trạng thái trực quan.
- `static/js/ticket.js`: Logic gọi API fetch asynchronous, xử lý duyệt gửi và cập nhật UI tức thì.

#### 14. Chạy thử toàn bộ hệ thống
Khởi động hệ thống và kiểm chứng trải nghiệm thực tế:
- Nhân viên mở Ticket #1001.
- Bấm "AI Soạn thảo Câu trả lời Nháp" -> AI sinh phản hồi chuẩn mực dựa trên FAQ.
- Nhân viên chỉnh sửa số hotline, bấm "Phê duyệt & Gửi cho Khách hàng".
- Bình luận được đưa vào dòng thời gian của ticket, trạng thái ticket tự động đổi sang `Waiting Customer`.

---

### PHẦN XXIV. MCP

Tích hợp Model Context Protocol (MCP) khi liên kết với GitHub Issues hoặc Webhook tiếp nhận ticket từ bên ngoài:
```
External Helpdesk Ticket -> MCP Server -> Codex Agent -> Phân tích -> Đề xuất giải pháp -> Testing -> Human Approval
```

---

### PHẦN XXV. DOCUMENTATION SKILL

#### Bước 20
Tạo: `.agents/skills/documentation/SKILL.md`  
Đồng bộ hóa toàn bộ tài liệu dự án:
- `README.md`
- `docs/api.md`
- `docs/architecture.md`
- `docs/database-design.md`
- `docs/deployment.md`
- `docs/user-guide.md`

---

### PHẦN XXVI. KẾT QUẢ CUỐI CÙNG

Sau toàn bộ quá trình, chúng ta có cấu trúc dự án hoàn chỉnh:

```
ViettinCare/
│
├── .agents/
│   └── skills/
│       ├── requirements-analysis/ (SKILL.md)
│       ├── architecture-design/ (SKILL.md)
│       ├── database-design/ (SKILL.md)
│       ├── implementation/ (SKILL.md)
│       ├── testing/ (SKILL.md)
│       ├── code-review/ (SKILL.md)
│       ├── security-review/ (SKILL.md)
│       ├── ticket-analysis/ (SKILL.md)
│       ├── faq-retrieval/ (SKILL.md)
│       ├── context-builder/ (SKILL.md)
│       ├── ai-prompt/ (SKILL.md)
│       └── documentation/ (SKILL.md)
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
│   ├── ticket-analysis.md
│   └── Bao_Cao_Thuc_Hanh_AI_Augmented_SDLC_De_Tai_10.md
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
│   ├── css/style.css
│   └── js/ticket.js
│
├── tests/
│   ├── test_auth.py
│   ├── test_tickets.py
│   └── test_ai_support.py
│
├── app.py
├── requirements.txt
├── README.md
└── Bao_Cao_Thuc_Hanh_AI_Augmented_SDLC_De_Tai_10.docx
```

---

### PHẦN XXVII. TOÀN BỘ QUY TRÌNH DƯỚI DẠNG AI-AUGMENTED SDLC

```
[CUSTOMER]
    │
    ▼ Customer Requirement
+─────────+      SKILLS (12 Skills)
|         |──────► [Requirements Skill] ──► Requirements ──► [HUMAN GATE 1: APPROVED]
|         |──────► [Architecture Skill]  ──► Architecture ──► [HUMAN GATE 2: APPROVED]
|         |──────► [Database Skill]      ──► Database     ──► [HUMAN GATE 3: APPROVED]
|  CODEX  |──────► [Coding Skill]        ──► Source Code
|  AGENT  |──────► [Testing Skill]       ──► Pytest (8/8 Passed)
|         |──────► [Review Skill]        ──► Review Report
|         |──────► [Security Skill]      ──► Security Report (PII Masking)
|         |──────► [Documentation Skill] ──► Technical Docs ──► [HUMAN QA] ──► [RELEASE]
+─────────+
    │
    ├─────────► TOOLS: [Terminal] [File System] [Python] [Pytest] [Git]
    │
    └─────────► MCP:   [GitHub Issues / Helpdesk Webhook]
```

---

### PHẦN XXVIII. VAI TRÒ CỦA 4 THÀNH PHẦN

| Thành phần | Vai trò |
|---|---|
| **Codex** | AI Agent điều phối và thực hiện các tác vụ phát triển phần mềm |
| **Skill** | Tri thức thủ tục, quy trình và tiêu chuẩn chuyên môn quy định cách thực hiện một loại tác vụ |
| **Tool** | Cơ chế cho phép Codex thực hiện thao tác cụ thể trên môi trường làm việc |
| **MCP** | Cơ chế kết nối Codex với các hệ thống, dịch vụ và nguồn dữ liệu bên ngoài |

---

### PHẦN XXIX. QUẢN LÝ VERSION CỦA SKILL

Một ưu điểm quan trọng là Skill không nên được xem là tài liệu tĩnh. Quản lý version cho Skills giúp duy trì và nâng cấp quy trình làm việc theo thời gian:
```
requirements-analysis/
├── v1/
│   └── SKILL.md
├── v2/
│   └── SKILL.md
└── v3/
    └── SKILL.md
```

---

### PHẦN XXX. MỘT LƯU Ý QUAN TRỌNG VỀ LƯU TRỮ SKILL

Có hai khái niệm lưu trữ cần phân biệt:
1. **Cấp project**: Skill được quản lý cùng repository tại `.agents/skills/`. Mục tiêu: phục vụ workflow cụ thể của project và đồng bộ qua Git.
2. **Cấp nền tảng**: Quản lý thông qua Skills API của nền tảng AI để tái sử dụng Skill ở cấp hệ thống cho nhiều dự án khác nhau.

Do đó, trong bài thực hành này, dự án được tổ chức chuẩn mực bắt đầu với:
```
Project
   └── .agents/skills/
```
