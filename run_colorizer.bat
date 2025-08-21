@echo off
chcp 65001 > nul
title DeOldify Image Colorizer

echo.
echo ========================================
echo   🎨 DeOldify Image Colorizer
echo ========================================
echo.

cd /d "%~dp0"

echo กำลังตรวจสอบ Python และไลบรารี...
echo.

REM ตรวจสอบ Python
"C:/Users/Nong PO/AppData/Local/Programs/Python/Python38/python.exe" --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ไม่พบ Python! โปรดติดตั้ง Python ก่อน
    pause
    exit /b 1
)

echo ✅ พบ Python แล้ว
echo.

REM รันโปรแกรม
if "%~1"=="" (
    echo โหมดเลือกไฟล์:
    "C:/Users/Nong PO/AppData/Local/Programs/Python/Python38/python.exe" main.py
) else (
    echo กำลังประมวลผล: %1
    "C:/Users/Nong PO/AppData/Local/Programs/Python/Python38/python.exe" main.py "%~1"
)

echo.
echo กดปุ่มใดก็ได้เพื่อปิด...
pause >nul
