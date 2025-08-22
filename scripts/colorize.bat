@echo off
echo ===========================================
echo      DeOldify Image Colorizer
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

REM Check if input file is provided
if "%~1"=="" (
    echo Usage: %0 input_image.jpg [output_image.jpg] [render_factor]
    echo.
    echo Examples:
    echo   %0 my_photo.jpg
    echo   %0 my_photo.jpg colored_photo.jpg
    echo   %0 my_photo.jpg colored_photo.jpg 25
    echo.
    echo Render factor: 7-45 (higher = better quality but slower)
    pause
    exit /b 1
)

REM Set default values
set INPUT_FILE=%~1
set OUTPUT_FILE=%~2
set RENDER_FACTOR=%~3

if "%RENDER_FACTOR%"=="" set RENDER_FACTOR=35

REM Check if input file exists
if not exist "%INPUT_FILE%" (
    echo Error: Input file '%INPUT_FILE%' not found!
    pause
    exit /b 1
)

echo.
echo Input file: %INPUT_FILE%
if not "%OUTPUT_FILE%"=="" echo Output file: %OUTPUT_FILE%
echo Render factor: %RENDER_FACTOR%
echo.

REM Run the colorizer
echo Starting colorization...
if "%OUTPUT_FILE%"=="" (
    python simple_colorizer.py "%INPUT_FILE%" --render_factor=%RENDER_FACTOR%
) else (
    python simple_colorizer.py "%INPUT_FILE%" "%OUTPUT_FILE%" --render_factor=%RENDER_FACTOR%
)

if %errorlevel% equ 0 (
    echo.
    echo ===========================================
    echo     Colorization completed successfully!
    echo ===========================================
) else (
    echo.
    echo ===========================================
    echo        Colorization failed!
    echo ===========================================
)

echo.
pause
