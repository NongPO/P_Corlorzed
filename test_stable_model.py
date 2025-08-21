#!/usr/bin/env python3
"""
ทดสอบโมเดล Stable แบบรวดเร็ว
"""

import os
import sys

def test_stable_model():
    """ทดสอบโมเดล Stable"""
    
    print("🧪 ทดสอบโมเดล Stable อย่างรวดเร็ว")
    print("=" * 40)
    
    # ตรวจสอบไฟล์โมเดล
    models_dir = "deoldify_core/models"
    stable_model = os.path.join(models_dir, "ColorizeStable_gen.pth")
    
    if not os.path.exists(stable_model):
        print("❌ ไม่พบไฟล์โมเดล Stable")
        return False
    
    size = os.path.getsize(stable_model)
    print(f"📊 ขนาดโมเดล Stable: {size:,} bytes ({size/1024/1024:.1f} MB)")
    
    if size < 100000000:  # น้อยกว่า 100MB
        print("❌ ขนาดไฟล์ไม่ถูกต้อง")
        return False
    
    print("✅ ไฟล์โมเดล Stable มีขนาดถูกต้อง")
    
    # ทดสอบการโหลดโมเดล
    try:
        print("\n🔄 กำลังทดสอบการโหลดโมเดล...")
        
        # เปลี่ยนไปยัง deoldify_core directory
        original_dir = os.getcwd()
        os.chdir("deoldify_core")
        sys.path.insert(0, os.getcwd())
        
        from deoldify.visualize import get_image_colorizer
        
        print("📚 โหลดไลบรารี DeOldify สำเร็จ")
        
        # ทดสอบโหลดโมเดล Stable
        print("🏞️ กำลังโหลดโมเดล Stable...")
        colorizer = get_image_colorizer(artistic=False)
        
        print("✅ โหลดโมเดล Stable สำเร็จ!")
        
        # กลับไปยัง directory เดิม
        os.chdir(original_dir)
        
        return True
        
    except Exception as e:
        print(f"❌ เกิดข้อผิดพลาด: {e}")
        
        # กลับไปยัง directory เดิม
        try:
            os.chdir(original_dir)
        except:
            pass
        
        return False

def main():
    success = test_stable_model()
    
    print("\n" + "=" * 40)
    
    if success:
        print("🎉 โมเดล Stable พร้อมใช้งาน!")
        print("\n💡 ทดสอบการใช้งาน:")
        print("python simple_colorizer.py input.jpg output.jpg --model=stable")
        print("python simple_colorizer.py input.jpg output.jpg --model=artistic")
    else:
        print("❌ โมเดล Stable ยังไม่พร้อมใช้งาน")
        print("\n💡 ใช้โมเดล Artistic แทน:")
        print("python simple_colorizer.py input.jpg output.jpg --model=artistic")

if __name__ == "__main__":
    main()
