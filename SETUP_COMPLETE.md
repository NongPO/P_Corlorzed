# 🎨 DeOldify Setup สำเร็จแล้ว! 

## ✅ สิ่งที่ติดตั้งเรียบร้อยแล้ว:

### Environment & Dependencies
- ✅ Conda environment: `colorized` 
- ✅ Python 3.8 พร้อม PyTorch และ CUDA support
- ✅ FastAI 1.0.61
- ✅ OpenCV, Matplotlib, Pillow
- ✅ IPython, FFmpeg, yt-dlp
- ✅ โมเดล DeOldify (Artistic & Stable) - **ทำงานได้ทั้งคู่!**

### ไฟล์และโฟลเดอร์
- ✅ `simple_colorizer.py` - สคริปต์หลักสำหรับแปลงภาพ
- ✅ `app.py` - เว็บแอพพลิเคชัน
- ✅ `colorize.bat` - ไฟล์ batch สำหรับ Windows 
- ✅ `run_web.bat` - รันเว็บแอพ
- ✅ `input_images/` - โฟลเดอร์สำหรับใส่รูปต้นฉบับ
- ✅ `output_images/` - โฟลเดอร์สำหรับผลลัพธ์
- ✅ `deoldify_core/` - โค้ดหลักที่เรียบร้อยแล้ว
- ✅ `README_THAI.md` - คู่มือการใช้งาน

### โมเดล AI (อัปเดต!)
- ✅ **Artistic Model**: 255 MB - สำหรับภาพคน, ศิลปะ
- ✅ **Stable Model**: 874 MB - สำหรับภาพธรรมชาติ, อาคาร

## 🚀 วิธีการใช้งาน:

### วิธีที่ 1: ใช้ไฟล์ .bat (ง่ายที่สุด)
```cmd
colorize.bat input_images/your_image.jpg
colorize.bat input_images/your_image.jpg output_images/result.jpg
colorize.bat input_images/your_image.jpg output_images/result.jpg 25
```

### วิธีที่ 2: Command Line
```cmd
conda activate colorized
python simple_colorizer.py input_images/your_image.jpg
python simple_colorizer.py input_images/your_image.jpg output_images/result.jpg --render_factor=25
```

## 📋 พารามิเตอร์:
- **render_factor**: 7-45 (7=เร็วแต่คุณภาพต่ำ, 45=ช้าแต่คุณภาพสูง)
- **model**: artistic (default) หรือ stable

## 🔧 การแก้ไขปัญหา:

### หากพบ Error:
1. ตรวจสอบว่า activate environment แล้ว: `conda activate colorized`
2. ตรวจสอบ path ของรูปภาพ
3. ลด render_factor หากมีปัญหา memory

### ประสิทธิภาพ:
- ใช้ render_factor 15-25 สำหรับการทดสอบ
- ใช้ render_factor 35-45 สำหรับผลลัพธ์คุณภาพสูง
- รูปขนาดใหญ่จะใช้เวลานานกว่า

## 📁 ตัวอย่างโครงสร้าง:
```
Corlorzed/
├── input_images/
│   └── old_photo.jpg      <- วางรูปต้นฉบับที่นี่
├── output_images/         <- ผลลัพธ์จะอยู่ที่นี่
├── colorize.bat          <- Double-click เพื่อใช้งาน
└── simple_colorizer.py   <- สคริปต์หลัก
```

## 🎯 ตอนนี้พร้อมใช้งานแล้ว!
ลองวางรูปขาวดำใน `input_images/` แล้ว double-click `colorize.bat` ได้เลย!
