# Bản ghi quyết định kiến trúc (Architectural Decision Records - ADR) - Đề tài 10

## ADR-001: Lựa chọn Framework Backend (Python Flask)
- **Bối cảnh**: Hệ thống cần một framework web nhẹ, dễ tích hợp với các thư viện AI hiện đại của Python (Google GenAI, LangChain, Pytest), đồng thời dễ triển khai và kiểm thử.
- **Quyết định**: Sử dụng Python Flask với mô hình Blueprints để phân tách rõ ràng các nhóm router (`auth_routes`, `ticket_routes`, `ai_routes`, `customer_routes`).
- **Hệ quả**: Cấu trúc rõ ràng, thời gian khởi động nhanh, dễ dàng viết test case tự động hóa bằng pytest.

## ADR-002: Áp dụng mô hình Human-in-the-Loop cho phản hồi AI
- **Bối cảnh**: Mô hình ngôn ngữ lớn (LLM) có nguy cơ bịa đặt (hallucination), có thể đưa ra lời khuyên sai quy trình hoặc cam kết bồi thường ngoài thẩm quyền làm thiệt hại cho doanh nghiệp.
- **Quyết định**: Tuyệt đối không cho phép AI tự động gửi tin nhắn trực tiếp tới khách hàng. AI chỉ sinh ra bản nháp (Draft Response). Nhân viên hỗ trợ phải xem trước, chỉnh sửa (nếu cần) và bấm nút xác nhận duyệt mới được lưu vào hệ thống và gửi cho khách.
- **Hệ quả**: Đảm bảo an toàn 100% về mặt pháp lý và chính sách chăm sóc khách hàng.

## ADR-003: Kiến trúc RAG tối giản cho cơ sở tri thức FAQ
- **Bối cảnh**: Cần cung cấp cho AI các chính sách chính thức của doanh nghiệp để câu trả lời luôn bám sát nghiệp vụ.
- **Quyết định**: Triển khai tầng `FAQ Retriever` dựa trên trích xuất từ khóa phân loại và truy vấn tham số hóa (Parameterized SQL) lọc theo chuyên mục và từ khóa liên quan, đưa vào Context Builder trước khi gửi prompt cho Gemini API.
- **Hệ quả**: Chi phí vận hành thấp, không phụ thuộc vào hạ tầng vector database cồng kềnh, tốc độ truy xuất dưới 50ms.

## ADR-004: Bảo mật thông tin cá nhân khách hàng (PII Masking)
- **Bối cảnh**: Khách hàng thường gửi thông tin nhạy cảm (số thẻ, mật khẩu tạm thời, số điện thoại) trong mô tả ticket. Gửi trực tiếp dữ liệu này ra API công cộng vi phạm nguyên tắc bảo mật.
- **Quyết định**: Thiết kế module `sanitizer` chạy cục bộ trên máy chủ trước khi xây dựng ngữ cảnh AI, tự động thay thế các mẫu nhạy cảm bằng nhãn mask `[MASKED_INFO]`.
- **Hệ quả**: Đảm bảo tuân thủ tiêu chuẩn an toàn thông tin và quyền riêng tư của khách hàng.
