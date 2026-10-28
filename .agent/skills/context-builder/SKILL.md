---
name: context-builder
description: Xây dựng khối ngữ cảnh ngắn gọn, bảo mật, kết hợp thông tin ticket, lịch sử trao đổi đã khử định danh PII và bài viết hướng dẫn FAQ chính thức cho LLM.
---
# Kỹ năng Xây dựng Ngữ cảnh AI (Context Builder Skill)

## 1. Mục tiêu (Objective)
Đóng gói một khối ngữ cảnh (Context Block) chuẩn xác, cô đọng và an toàn, kết hợp giữa thông tin chi tiết của ticket, lịch sử các lượt trao đổi gần nhất (đã được khử định danh thông tin cá nhân) và giải pháp tra cứu được từ cơ sở tri thức FAQ để làm đầu vào cho LLM.

## 2. Đầu vào (Inputs)
- Dữ liệu chi tiết của Ticket (Mã ticket, Tiêu đề, Mô tả ban đầu, Danh mục, Mức ưu tiên)
- Danh sách các bình luận trao đổi gần nhất giữa khách hàng và nhân viên
- Danh sách các bài viết FAQ tra cứu được từ tầng `FAQ Retriever`

## 3. Quy trình thực hiện (Process)
1. **Khử định danh dữ liệu cá nhân (PII Sanitization)**: Loại bỏ hoặc thay thế mật khẩu, số thẻ ngân hàng, số điện thoại thành các nhãn mask an toàn (`[MASKED_INFO]`).
2. **Lọc nhiễu hội thoại**: Lọc bỏ các câu chào hỏi lặp lại không mang giá trị ngữ nghĩa kỹ thuật; chỉ giữ lại tối đa 4 lượt trao đổi gần nhất để tối ưu dung lượng token.
3. **Định dạng cấu trúc ngữ cảnh chuẩn**:
   ```text
   [THÔNG TIN TICKET]
   Mã: ... | Tiêu đề: ... | Mô tả: ...

   [LỊCH SỬ TRAO ĐỔI GẦN ĐÂY]
   - customer: ...
   - agent: ...

   [CƠ SỞ TRI THỨC VÀ CHÍNH SÁCH DOANH NGHIỆP]
   Vấn đề: ...
   Giải pháp chuẩn: ...
   ```
4. **Kiểm soát dung lượng Token**: Giới hạn toàn bộ khối ngữ cảnh dưới 2000 ký tự (khoảng 500 tokens) để vừa tiết kiệm chi phí, vừa giảm độ trễ phản hồi của AI.

## 4. Quy tắc bắt buộc (Rules)
- Không thêm thắt bất kỳ dữ liệu nào không có trong cơ sở dữ liệu.
- Không làm thay đổi nội dung khiếu nại gốc của khách hàng.
- Nguồn trích xuất từ FAQ phải được phân tách rõ ràng với nội dung trao đổi của khách.

## 5. Đầu ra cần tạo (Outputs)
- Chuỗi văn bản ngữ cảnh sạch được truyền vào hàm tạo prompt của mô hình ngôn ngữ lớn.
