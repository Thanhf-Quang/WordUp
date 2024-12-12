import cloudinary
import cloudinary.uploader
from environ import Env

env = Env()
Env.read_env()

# Đọc CLOUDINARY_URL từ biến môi trường
CLOUDINARY_URL = env('CLOUDINARY_URL')

# Cấu hình cloudinary
cloudinary.config(
    cloud_name=CLOUDINARY_URL.split('@')[1],  # Lấy tên cloud từ URL
    api_key=CLOUDINARY_URL.split('//')[1].split(':')[0],  # Lấy API key từ URL
    api_secret=CLOUDINARY_URL.split(':')[2].split('@')[0],  # Lấy API secret từ URL
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': CLOUDINARY_URL,
}

# Kiểm tra kết nối bằng cách tải lên file test
try:
    response = cloudinary.uploader.upload("https://via.placeholder.com/150")
    print("Kết nối thành công!")
    print("URL của ảnh tải lên:", response['secure_url'])
except Exception as e:
    print("Không thể kết nối với Cloudinary:", e)
