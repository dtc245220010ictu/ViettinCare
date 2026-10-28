import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'viettincare.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    conn = get_db()
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    seed_initial_data(conn)
    conn.close()

def seed_initial_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    if cursor.fetchone()[0] == 0:
        # Seed users
        users = [
            ('admin', 'admin@viettincare.vn', generate_password_hash('Admin@123'), 'Quản Trị Viên', 'admin'),
            ('lead_tuan', 'tuan.lead@viettincare.vn', generate_password_hash('Lead@123'), 'Trần Anh Tuấn (Team Lead)', 'lead'),
            ('agent_lan', 'lan.agent@viettincare.vn', generate_password_hash('Agent@123'), 'Nguyễn Mai Lan (Support Agent)', 'agent'),
            ('agent_huy', 'huy.agent@viettincare.vn', generate_password_hash('Agent@123'), 'Lê Quang Huy (Support Agent)', 'agent'),
        ]
        cursor.executemany(
            "INSERT INTO users (username, email, password_hash, full_name, role) VALUES (?, ?, ?, ?, ?)",
            users
        )

        # Seed customers
        customers = [
            ('Phạm Minh Hoàng', 'hoang.pm@gmail.com', '0912345678', 'Tập đoàn An Phát', 'VIP'),
            ('Đỗ Bích Phương', 'phuong.db@techcorp.vn', '0987654321', 'TechCorp JSC', 'Standard'),
            ('Lê Văn Nam', 'nam.le@startup.io', '0903112233', 'V-Solutions', 'Standard'),
        ]
        cursor.executemany(
            "INSERT INTO customers (full_name, email, phone, company, tier) VALUES (?, ?, ?, ?, ?)",
            customers
        )

        # Seed FAQs (Cơ sở tri thức cho RAG)
        faqs = [
            (
                'Tài khoản & Đăng nhập',
                'Khách hàng không nhận được email kích hoạt hoặc email reset mật khẩu thì xử lý thế nào?',
                'Hướng dẫn khách kiểm tra hòm thư Rác (Spam/Junk). Nếu sau 5 phút vẫn chưa nhận được, nhân viên hỗ trợ xác minh thông tin chính chủ qua số điện thoại đăng ký và gửi mã OTP kích hoạt thủ công qua SMS.',
                'đổi mật khẩu reset pass quên mật khẩu không nhận email kích hoạt otp'
            ),
            (
                'Thanh toán & Hóa đơn',
                'Khách hàng bị trừ tiền hai lần khi gia hạn dịch vụ hoặc giao dịch thất bại nhưng bị trừ tiền?',
                'Hệ thống tự động đối soát ngân hàng trong vòng 24h. Nhân viên hỗ trợ cần xin mã giao dịch (Transaction ID) và ảnh sao kê. Nếu đối soát lỗi từ cổng thanh toán, tiền sẽ được hoàn tự động về tài khoản khách sau 3-5 ngày làm việc. Nhân viên không được cam kết hoàn tiền mặt ngay lập tức.',
                'thanh toán trừ tiền hai lần giao dịch hoàn tiền banking lỗi ngân hàng'
            ),
            (
                'Lỗi kỹ thuật & Phần mềm',
                'Hệ thống báo lỗi 500 hoặc màn hình trắng khi tải danh sách báo cáo?',
                'Yêu cầu khách hàng xóa cache trình duyệt (Ctrl+F5) hoặc thử trình duyệt ẩn danh. Nếu vẫn gặp lỗi, thu thập URL cụ thể, thời điểm xảy ra lỗi và chuyển tiếp cho đội ngũ Kỹ thuật hạ tầng (DevOps).',
                'lỗi 500 màn hình trắng tải báo cáo crash lag hệ thống sập'
            ),
            (
                'Tư vấn & Hướng dẫn sử dụng',
                'Quy trình nâng cấp gói tài khoản từ Standard lên VIP được thực hiện ra sao?',
                'Khách hàng có thể vào Cài đặt -> Gói dịch vụ -> Chọn Nâng cấp VIP. Quyền lợi VIP bao gồm SLA phản hồi ưu tiên dưới 15 phút, có nhân viên kỹ thuật hỗ trợ 24/7 và hạn mức lưu trữ gấp 5 lần.',
                'nâng cấp vip bảng giá ưu đãi sla quyền lợi gói dịch vụ'
            )
        ]
        cursor.executemany(
            "INSERT INTO faqs (category, question, answer, keywords) VALUES (?, ?, ?, ?)",
            faqs
        )

        # Seed sample tickets
        tickets = [
            (
                'TCK-1001', 1,
                'Không đăng nhập được sau khi đổi mật khẩu, đã thử reset nhưng chưa nhận email',
                'Tôi vừa thực hiện đổi mật khẩu lúc 9h sáng nay. Sau đó đăng xuất thì không vào lại được. Đã bấm quên mật khẩu nhiều lần nhưng hòm thư hoang.pm@gmail.com vẫn không thấy email gửi về. Công việc đang gấp, nhờ xử lý sớm giúp!',
                'Tài khoản & Đăng nhập', 'High', 'New', 3
            ),
            (
                'TCK-1002', 2,
                'Giao dịch thanh toán gia hạn gói dịch vụ báo lỗi nhưng tài khoản ngân hàng đã bị trừ 500k',
                'Sáng nay tôi thanh toán gói dịch vụ qua quét mã QR VNPay. Ứng dụng báo lỗi kết nối cổng thanh toán, tuy nhiên tiền trong tài khoản VCB của tôi đã bị trừ 500.000đ. Hệ thống vẫn báo tài khoản hết hạn.',
                'Thanh toán & Hóa đơn', 'Urgent', 'In Progress', 3
            ),
            (
                'TCK-1003', 3,
                'Cần tư vấn thủ tục nâng cấp tài khoản công ty lên gói Doanh nghiệp VIP',
                'Công ty chúng tôi sắp mở rộng thêm 20 nhân viên nên muốn tìm hiểu chính sách ưu đãi khi nâng cấp gói dịch vụ Standard lên VIP.',
                'Tư vấn & Hướng dẫn sử dụng', 'Medium', 'Closed', 4
            )
        ]
        cursor.executemany(
            "INSERT INTO tickets (ticket_number, customer_id, title, description, category, priority, status, assigned_to) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            tickets
        )

        # Seed comments
        comments = [
            (1, 1, 'customer', 'Phạm Minh Hoàng', 'Tôi đã kiểm tra kỹ cả hòm thư Spam nhưng vẫn hoàn toàn không có email.', 0),
            (2, 3, 'agent', 'Nguyễn Mai Lan', 'Chào chị Phương, em đã tiếp nhận thông tin. Chị vui lòng gửi giúp em mã tham chiếu giao dịch trừ tiền trên app VCB để em gửi sang kế toán đối soát nhé ạ.', 0),
            (3, 4, 'agent', 'Lê Quang Huy', 'Chào anh Nam, tư vấn viên đã gửi tài liệu báo giá qua email cho anh. Hợp đồng nâng cấp đã hoàn tất.', 0)
        ]
        cursor.executemany(
            "INSERT INTO ticket_comments (ticket_id, user_id, author_role, author_name, content, is_internal) VALUES (?, ?, ?, ?, ?, ?)",
            comments
        )

        conn.commit()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully at:", DB_PATH)
