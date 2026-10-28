---
name: rag-prompt
description: Xây dựng các mẫu prompt có ràng buộc chặt chẽ để hướng dẫn LLM sinh câu trả lời bám sát ngữ cảnh tra cứu được, chống hiện tượng ảo giác (hallucination) và tuân thủ chính sách doanh nghiệp.
---
# Kỹ năng Thiết kế Prompt RAG (RAG Prompt Engineering Skill)

## 1. Mục tiêu (Objective)
Thiết kế các mẫu prompt (System Prompt & User Prompt) chặt chẽ, kỷ luật cao, hướng dẫn mô hình ngôn ngữ lớn (Gemini LLM) đóng vai trò trợ lý chuyên môn, chỉ tạo bản nháp câu trả lời dựa trên sự thật có trong ngữ cảnh tra cứu (Grounding Context), tuyệt đối không suy diễn chính sách bừa bãi.

## 2. Cấu trúc Prompt chuẩn mực (Prompt Structure)
1. **Vai trò hệ thống (System Persona)**:
   > "Bạn là Trợ lý AI hỗ trợ nhân viên chăm sóc khách hàng ViettinCare. Nhiệm vụ của bạn là SOẠN THẢO CÂU TRẢ LỜI NHÁP để nhân viên hỗ trợ duyệt trước khi gửi cho khách hàng."
2. **Quy tắc rào chắn bắt buộc (Grounding Rules)**:
   - Chỉ sử dụng các sự thật và giải pháp có trong phần `[CƠ SỞ TRI THỨC VÀ CHÍNH SÁCH DOANH NGHIỆP]`.
   - TUYỆT ĐỐI KHÔNG tự ý cam kết bồi thường, hoàn tiền mặt ngay lập tức hoặc ghi nhận lỗi hệ thống nếu chưa có xác nhận từ kế toán/kỹ thuật.
   - Nếu ngữ cảnh không có thông tin giải quyết, lịch sự hướng dẫn khách hàng cung cấp thêm mã giao dịch/ảnh chụp màn hình hoặc thông báo chuyển tiếp chuyên viên cấp cao.
   - Trả lời bằng tiếng Việt lịch sự, thân thiện, đồng cảm và rõ ràng.
3. **Tiêm ngữ cảnh (Context Injection)**: Được cung cấp bởi `Context Builder`.
4. **Câu hỏi / Yêu cầu của người dùng**: Nội dung sự cố của khách hàng.
5. **Ràng buộc đầu ra (Output Constraints)**: Câu trả lời nháp có cấu trúc mở đầu lịch sự, nội dung hướng dẫn từng bước và lời chào kết chuyên nghiệp.

## 3. Quy tắc bắt buộc (Rules)
- Không trả lời dựa trên kiến thức chung ngoài đời thực khi câu hỏi liên quan đến chính sách cụ thể của doanh nghiệp.
- Mọi câu trả lời của AI đều ở trạng thái nháp (Draft) phục vụ quy trình Human Gate.
