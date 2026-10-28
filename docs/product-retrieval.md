# Tài liệu Truy xuất Dữ liệu & Tri thức Hỗ trợ (Retrieval Specification) - Đề tài 10

## 1. Mục tiêu
Đặc tả chi tiết module truy xuất dữ liệu theo quy định của kỹ năng `product-retrieval` và `tour-retrieval`. Chuyển đổi ý định có cấu trúc từ bước phân tích câu hỏi thành các câu truy vấn cơ sở dữ liệu tham số hóa an toàn.

## 2. Quy trình truy xuất (Retrieval Pipeline)
```
User Question -> Question Analyzer -> Structured Intent -> Parameterized SQL Query -> Database -> Matching Records
```

## 3. Câu lệnh SQL tham số hóa mẫu
```python
def retrieve_records(intent):
    category = intent.get("category")
    keywords = intent.get("keywords", [])
    
    # Truy vấn theo danh mục
    query = "SELECT * FROM faqs WHERE category = ?"
    params = [category]
    
    # Mở rộng theo từ khóa nếu cần
    if keywords:
        kw_conditions = " OR ".join(["keywords LIKE ?" for _ in keywords])
        query = f"SELECT * FROM faqs WHERE category = ? OR ({kw_conditions}) LIMIT 3"
        params = [category] + [f"%{k}%" for k in keywords]
        
    return execute_query(query, params)
```

## 4. Kiểm soát an ninh
- Tuyệt đối không nối chuỗi (No string concatenation).
- Giới hạn tối đa 3-5 bản ghi liên quan nhất để tối ưu hóa context cho mô hình ngôn ngữ lớn.
