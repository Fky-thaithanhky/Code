import os
import re,time
import random
import requests
from datetime import datetime

# ✅ Tạo ID ngẫu nhiên (giống UUID)
def random_hex_id():
    parts = [8, 4, 4, 4, 12]
    return '-'.join(''.join(random.choices('0123456789abcdef', k=p)) for p in parts)

# 🌐 URL upload
url = "https://dulieu.dethitailieu.com/member/uploads/create"

# ⚠️ Thay cookie bằng cookie của bạn
COOKIE_STRING = "october_session=october_session=eyJpdiI6IkNGRk5YWXU0dU9VMGVaY3N2Y2drVEE9PSIsInZhbHVlIjoiWnFLcDh2bFFVUjJzSlExNEpKOW04clRiWk04c01nSlk1bk1uczAxMXk5TlQwNTBjQkVvck5kZlJieldndzE2YklUdDB2NVhuSUcxNERONXR1NDl5V1YrbTB4aVBWbVR1TGlOUGxBSFZtNEJZeFQ0SDBIWFVHUXo4aHIxbkVvTEEiLCJtYWMiOiJkZTVlNjY4Y2U1ODNiMDUwZDE3OGVmNDJmOTAxOWQzZjA1MWFkZmExMDE1ODU4MDYxZDYyN2M1ZDY5M2NhY2ViIiwidGFnIjoiIn0%3D; user_auth=eyJpdiI6IktJUFhNRkc1R2Z4bWdQV2hPVThXT0E9PSIsInZhbHVlIjoiVnlLczFvNWliRjdhMFFlOVA2N0l6a0QwY0pVRWNhaEd5TnNqRXZPUU5vU3VFVG5UMGtVb3creWdnWWVUR1FjSUtSNGU3Y1ZrZmwza0FLL3N5bjNZS2ZKbUxUdy9yamxVYnVUa0lnWmNZVmlpd0p0WG9Jd01MTHdvZTF3SzZ6T0JhaTFkYm1hNG5WUzRoTTR3dWs1OEQ1dkQ4MDBabml2ZGZWSHlseDgzeVJUZ25UcTU1K3dOczkvRlJrOWw4VTlNVGRPcXErYm9hQUpqUmFFVEd4d1ZUYXh5L0s5eWwxRURXeWc2SkJQU1UvQT0iLCJtYWMiOiIyNWY4ZDNkNjYwN2JkNDM5OGMzYmY5NzMwYWM3MGVhMzA4N2IwMGE2MTViODY2YTFhMjNkZDU5MTQyNjc5OGNiIiwidGFnIjoiIn0%3D"

headers = {
  'User-Agent': "Mozilla/5.0 (iPhone; CPU iPhone OS 18_7 like Mac OS X)",
  'x-requested-with': "XMLHttpRequest",
  'origin': "https://dulieu.dethitailieu.com",
  'referer': "https://dulieu.dethitailieu.com/member/uploads/create",
  'x-october-request-handler': "onUpload",
  'Cookie': COOKIE_STRING
}

while True:
    try:
        payload = {
            'classify': 'class-12',
            'subject': 'math',
            'type': "short_answer"
        }
        files_upload = [
            ('question_image_upload', (random_hex_id(), open("1c.JPG", 'rb'), 'image/jpeg')),
            ('solution_image_upload', (random_hex_id(), open("2.JPG", 'rb'), 'image/jpeg'))]
        response = requests.post(url, data=payload, files=files_upload, headers=headers)
        status = response.status_code
        print(status)
        time.sleep(200)
    except:
        time.sleep(500)
        continue
print("\n📄 Toàn bộ kết quả đã ghi vào '/root/upload_log.txt'")