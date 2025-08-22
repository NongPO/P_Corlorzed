@echo off
echo ===============================================
echo 🎨 Installing AI Image Generation Dependencies
echo ===============================================
echo.

:: Activate conda environment
call conda activate colorized
if errorlevel 1 (
    echo ❌ Failed to activate conda environment 'colorized'
    echo Please make sure the environment exists
    pause
    exit /b 1
)

echo ✅ Activated conda environment: colorized
echo.

echo 📦 Installing PyTorch with CUDA support...
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
if errorlevel 1 (
    echo ⚠️ CUDA installation failed, trying CPU version...
    pip install torch torchvision
)

echo.
echo 📦 Installing Diffusers and Transformers...
pip install diffusers>=0.21.0
pip install transformers>=4.21.0
pip install accelerate>=0.20.0

echo.
echo 📦 Installing additional dependencies...
pip install -r requirements-ai-generation.txt

echo.
echo 🧪 Testing installation...
python -c "import torch; print(f'✅ PyTorch {torch.__version__} installed')"
python -c "import diffusers; print(f'✅ Diffusers {diffusers.__version__} installed')"
python -c "import transformers; print(f'✅ Transformers {transformers.__version__} installed')"

echo.
echo 🔍 Checking GPU availability...
python -c "import torch; print(f'🖥️ CUDA Available: {torch.cuda.is_available()}'); print(f'📱 Device: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"CPU Only\"}')"

echo.
echo 📋 Testing AI Image Generator...
python -c "from ai_image_generator import AIImageGenerator; gen = AIImageGenerator(); print('✅ AI Image Generator imported successfully'); print(f'🤖 Model info: {gen.get_model_info()}')"

echo.
echo ===============================================
echo 🎉 AI Image Generation Setup Complete!
echo ===============================================
echo.
echo 💡 Usage:
echo    python ai_image_generator.py "your prompt here"
echo    python app.py  (then go to /generate)
echo.
echo 📚 Example prompts:
echo    - "a beautiful sunset over mountains"
echo    - "a cute cat in a garden, digital art"
echo    - "futuristic city at night, cyberpunk style"
echo.
pause
