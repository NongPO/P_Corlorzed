# 📁 Project Structure

## Core Files
- `app.py` - Main Flask web application
- `simple_colorizer.py` - DeOldify colorization core
- `ai_image_generator.py` - AI image generation with Stable Diffusion
- `requirements-ai-generation.txt` - Python dependencies

## Directories

### 📂 Input/Output
- `input_images/` - Test images for colorization
- `output_images/` - Colorized results
- `generated_images/` - AI generated images
- `uploads/` - Web uploaded files
- `results/` - Web processing results

### 📂 Web Interface
- `templates/` - HTML templates for web interface

### 📂 Scripts & Tools
- `scripts/` - Batch files for easy operation
  - `run_web.bat` - Start web server
  - `colorize.bat` - Command line colorization
  - `install_ai_generation.bat` - Install dependencies

### 📂 Documentation
- `docs/` - Project documentation
  - `CHANGELOG.md` - Version history
  - `CONTRIBUTING.md` - Contribution guidelines
  - `MODEL_COMPARISON.md` - AI model comparisons
  - `PROJECT_SUMMARY.md` - Project overview
  - `SETUP_COMPLETE.md` - Setup guide

### 📂 Archive
- `archive/` - Old test files and deprecated code

### 📂 Core Libraries
- `deoldify_core/` - DeOldify library and dependencies

### 📂 Development
- `.github/` - GitHub workflows and templates
- `.vscode/` - VS Code settings
- `Dockerfile` & `docker-compose.yml` - Container deployment

## Quick Start

1. Activate environment: `conda activate colorized`
2. Start server: `scripts\run_web.bat`
3. Open browser: `http://localhost:5000`

## Features

- 🎨 **Image Colorization**: AI-powered black & white to color conversion
- 🖼️ **AI Image Generation**: Text-to-image with Stable Diffusion
- 🌐 **Web Interface**: User-friendly web application
- 🚀 **GPU Acceleration**: CUDA support for fast processing
