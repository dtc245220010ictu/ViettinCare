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

        # Seed FAQs (Cơ sở tri thức CSKH Ngân hàng số cho RAG)
        faqs = [
            (
                'Tài khoản & Đăng nhập',
                'Khách hàng không nhận được email/SMS mã xác nhận kích hoạt ứng dụng Ngân hàng số hoặc reset mật khẩu?',
                'Hướng dẫn khách kiểm tra hòm thư Rác (Spam/Junk) và kiểm tra tín hiệu mạng điện thoại. Nếu sau 3 phút vẫn chưa nhận được, nhân viên CSKH hướng dẫn xác thực khuôn mặt (eKYC) trên ứng dụng hoặc cấp mã kích hoạt lại qua kênh xác thực tổng đài bảo mật.',
                'đổi mật khẩu reset pass quên mật khẩu không nhận email kích hoạt otp ngân hàng số'
            ),
            (
                'Thanh toán & Hóa đơn',
                'Khách hàng chuyển khoản nhanh 24/7 hoặc thanh toán QR bị trừ tiền tài khoản nhưng bên nhận chưa nhận được?',
                'Đây là tình trạng trễ lệnh đối soát liên ngân hàng (Napas). Hệ thống ngân hàng tự động tra soát và hoàn tiền hoặc ghi có cho người thụ hưởng trong vòng 24h làm việc. Nhân viên CSKH cần xin Mã tham chiếu giao dịch (Transaction ID) và gửi yêu cầu tra soát liên ngân hàng. Tuyệt đối không tự ý cam kết hoàn tiền mặt ngay lập tức.',
                'chuyển tiền napas trừ tiền hai lần giao dịch hoàn tiền tra soát lỗi ngân hàng qr pay'
            ),
            (
                'Lỗi kỹ thuật & Phần mềm',
                'Ứng dụng Ngân hàng số báo lỗi không kết nối máy chủ hoặc lỗi xác thực sinh trắc học FaceID/Vân tay?',
                'Yêu cầu khách hàng kiểm tra kết nối mạng 4G/Wifi, cập nhật phiên bản mới nhất của ứng dụng trên App Store/Google Play hoặc khởi động lại thiết bị. Nếu lỗi liên quan đến sinh trắc học theo Quyết định 2345/QĐ-NHNN, hướng dẫn khách mang Căn cước công dân gắn chip tới quầy giao dịch gần nhất để cập nhật dữ liệu NFC.',
                'lỗi ứng dụng crash sinh trắc học faceid căn cước cccd nfc sập hệ thống'
            ),
            (
                'Tư vấn & Hướng dẫn sử dụng',
                'Điều kiện nâng cấp tài khoản thanh toán lên phân hạng Khách hàng Ưu tiên (Priority/VIP) và hạn mức giao dịch?',
                'Khách hàng duy trì số dư bình quân từ 200 triệu VNĐ trong 3 tháng gần nhất hoặc có gói tiền gửi tiết kiệm từ 1 tỷ VNĐ. Quyền lợi bao gồm: Miễn phí toàn bộ phí chuyển tiền và phí quản lý tài khoản, nâng hạn mức chuyển tiền trực tuyến lên tới 5 tỷ VNĐ/ngày, và có chuyên viên tư vấn tài chính riêng 24/7.',
                'nâng cấp vip priority hạn mức chuyển tiền biểu phí lãi suất tiết kiệm thẻ tín dụng'
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

