@echo off
echo ===========================================
echo      🎨 DeOldify Web Application
echo ===========================================
echo.

REM Check if conda is available
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: Conda not found! Please install Anaconda/Miniconda first.
    pause
    exit /b 1
)

REM Activate the colorized environment
echo Activating conda environment: colorized
call conda activate colorized
if %errorlevel% neq 0 (
    echo Error: Could not activate environment 'colorized'
    echo Please make sure the environment exists: conda create -n colorized python=3.8
    pause
    exit /b 1
)

REM Check if Flask is installed
python -c "import flask" 2>nul
if %errorlevel% neq 0 (
    echo Installing Flask...
    pip install flask werkzeug
)

echo.
echo 🌐 Starting DeOldify Web Server...
echo 📁 Upload folder: uploads/
echo 📁 Result folder: results/
echo 🎯 Server will start at: http://localhost:5000
echo.
echo ✨ Open your web browser and go to: http://localhost:5000
echo 🔄 Press Ctrl+C to stop the server
echo.

REM Start the Flask app
python app.py

echo.
echo Web server stopped.
pause
