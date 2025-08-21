# 🎨 DeOldify Image Colorizer - Thai Version

แปลงภาพขาวดำเป็นภาพสีด้วย AI อัตโนมัติ

## 🚀 การติดตั้งและใช้งาน

### วิธีที่ 1: ใช้งานผ่าน Batch File (ง่ายที่สุด)
1. ดับเบิลคลิกที่ไฟล์ `run_colorizer.bat`
2. ป้อน path ของไฟล์ภาพที่ต้องการแปลง
3. เลือกโมเดล (Artistic หรือ Stable)
4. รอผลลัพธ์ที่โฟลเดอร์ `results`

### วิธีที่ 2: ใช้งานผ่าน Command Line
```cmd
python main.py "path/to/your/image.jpg"
python main.py "path/to/your/image.jpg" --stable
```

### วิธีที่ 3: ลากไฟล์ใส่ Batch File
- ลากไฟล์ภาพมาวางที่ `run_colorizer.bat`

## 🎛️ ตัวเลือกต่าง ๆ

### โมเดล
- **Artistic**: ให้สีที่สวยงาม สดใส แต่อาจมีข้อผิดพลาดบ้าง
- **Stable**: สีเสถียรกว่า แต่อาจจืดกว่า

### Render Factor
- **10-20**: เร็ว แต่คุณภาพต่ำ
- **25-35**: สมดุลระหว่างเร็วและคุณภาพ (แนะนำ)
- **35-40**: คุณภาพสูง แต่ช้า

## 📁 โครงสร้างไฟล์

```
Corlorzed/
├── main.py                 # สคริปต์หลัก
├── run_colorizer.bat      # ไฟล์ batch สำหรับ Windows
├── download_models.py     # ดาวน์โหลดโมเดล
├── results/              # ผลลัพธ์ที่แปลงแล้ว
└── DeOldify/            # ไลบรารี DeOldify
    ├── models/          # โมเดล AI
    ├── test_images/     # ภาพทดสอบ
    └── ...
```

## 🔧 การแก้ไขปัญหา

### ปัญหาไม่พบ Python
1. ติดตั้ง Python 3.8+ จาก python.org
2. แก้ไข path ใน `run_colorizer.bat`

### ปัญหาไม่พบโมเดล
```cmd
python download_models.py
```

### ปัญหาไลบรารี
```cmd
pip install -r DeOldify/requirements-simple.txt
```

## 📸 ตัวอย่างการใช้งาน

### ผ่าน Python
```python
from main import colorize_simple

# แปลงภาพด้วยโมเดล Artistic
result = colorize_simple(
    image_path="test.jpg",
    output_dir="results",
    artistic=True,
    render_factor=35
)
```

### ผ่าน Command Line
```cmd
# โมเดล Artistic
python main.py "test_images/old_photo.jpg"

# โมเดล Stable
python main.py "test_images/old_photo.jpg" --stable

# กำหนด output directory
python main.py "test_images/old_photo.jpg" -o "my_results"
```

## 🎯 เทคนิคการใช้งาน

1. **ภาพคุณภาพดี**: ยิ่งภาพต้นฉบับชัดยิ่งดี
2. **ขนาดไฟล์**: ภาพใหญ่เกินไปอาจใช้เวลานาน
3. **ประเภทภาพ**: เหมาะกับภาพคน อาคาร ธรรมชาติ
4. **การทดลอง**: ลองทั้ง Artistic และ Stable เพื่อเปรียบเทียบ

## 📋 ความต้องการระบบ

- **Python**: 3.8+
- **RAM**: 4GB+ (แนะนำ 8GB+)
- **GPU**: ไม่จำเป็น แต่จะเร็วกว่าถ้ามี NVIDIA GPU
- **พื้นที่**: 2GB+ สำหรับโมเดลและไลบรารี

## 🆘 การขอความช่วยเหลือ

หากมีปัญหา:
1. ตรวจสอบ error message
2. ลองรันใน Command Prompt เพื่อดู error detail
3. ตรวจสอบว่าไฟล์ภาพเปิดได้
4. ลองใช้โมเดล Stable แทน Artistic

## 📝 หมายเหตุ

- โปรเจคนี้ใช้ DeOldify ของ jantic
- สำหรับใช้งานส่วนตัวเท่านั้น
- ผลลัพธ์อาจไม่ตรงกับสีจริง เป็นเพียงการคาดเดาของ AI
