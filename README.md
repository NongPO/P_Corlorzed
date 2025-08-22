# 🎨 DeOldify AI Studio

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAI](https://img.shields.io/badge/FastAI-1.0.61-orange.svg)](https://fastai.org)
[![Flask](https://img.shields.io/badge/Flask-Web_App-green.svg)](https://flask.palletsprojects.com)
[![Diffusers](https://img.shields.io/badge/Diffusers-AI_Generation-purple.svg)](https://huggingface.co/docs/diffusers)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Complete AI-powered image processing suite: Colorize old photos AND generate new images from text**

Transform your old black and white photos into vibrant colorized images AND create stunning artwork from text descriptions using cutting-edge AI technology.

## ✨ Features

### 🖼️ Image Colorization (DeOldify)
- **CLI Tool**: Command-line interface for batch processing
- **Web Interface**: User-friendly colorization with drag & drop
- **Dual AI Models**: 
  - **Artistic Model** (255MB): Creative, vibrant colorization
  - **Stable Model** (874MB): Realistic, accurate colorization

### 🎨 AI Image Generation (Stable Diffusion)
- **Text-to-Image**: Generate images from text descriptions
- **Multiple Variations**: Create multiple styles of the same concept
- **Advanced Controls**: Size, steps, guidance scale, and seed options
- **Example Prompts**: Built-in prompt suggestions and templates

### 🌐 Web Application
- **Unified Interface**: Both colorization and generation in one app
- **Responsive Design**: Mobile-friendly design
- **Real-time Preview**: Instant results with download options
- **Parameter Control**: Fine-tune generation settings

## 🚀 Quick Start

### 1. Clone Repository
```bash
git clone https://github.com/NongPO/P_Corlorzed.git
cd P_Corlorzed
```

### 2. Setup Environment
```bash
# Create conda environment
conda create -n colorized python=3.8
conda activate colorized

# Install dependencies
pip install -r deoldify_core/requirements.txt
```

### 3. Download AI Models
Due to GitHub file size limitations, download models separately:

**Option A: Automatic Download (Recommended)**
```bash
python download_models.py
```

**Option B: Manual Download**
```bash
# Artistic Model (255MB)
wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth -O deoldify_core/models/ColorizeArtistic_gen.pth

# Stable Model (874MB) 
wget https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth -O deoldify_core/models/ColorizeStable_gen.pth
```

### 4. Install AI Image Generation (Optional)
```bash
# Install additional dependencies for text-to-image generation
install_ai_generation.bat
# OR manually:
pip install -r requirements-ai-generation.txt
```

### 5. Run Application

#### Option A: Web Interface (Full Features)
```bash
python app.py
# Open http://localhost:5000
# - Go to "/" for image colorization
# - Go to "/generate" for AI image generation
```

#### Option B: Command Line Tools
```bash
# Colorize images
python simple_colorizer.py input_images/photo.jpg output_images/colorized.jpg

# Generate images from text
python ai_image_generator.py "a beautiful sunset over mountains"
```

#### Option C: Windows Shortcuts
- Double-click `run_web.bat` for web interface
- Double-click `colorize.bat` for CLI colorization tool

#### Option D: Docker (Includes everything)
```bash
docker-compose up -d
# Open http://localhost:5000
```

## 📁 Project Structure

```
P_Corlorzed/
├── 🎨 Main Applications
│   ├── app.py                      # Flask web application (colorize + generate)
│   ├── simple_colorizer.py         # CLI colorization tool
│   ├── ai_image_generator.py       # CLI image generation tool
│   ├── download_models.py          # Model downloader with progress
│   ├── run_web.bat                 # Windows web shortcut
│   ├── colorize.bat                # Windows CLI shortcut
│   └── install_ai_generation.bat   # AI generation setup
│
├── 🧠 AI Core
│   └── deoldify_core/
│       ├── models/                 # AI models (download required)
│       ├── deoldify/               # Core DeOldify framework
│       ├── fastai/                 # FastAI integration
│       └── requirements.txt       # Colorization dependencies
│
├── 📁 Directories
│   ├── input_images/               # Source images for CLI
│   ├── output_images/              # CLI colorization results
│   ├── generated_images/           # AI-generated images
│   ├── uploads/                    # Web uploads
│   ├── results/                    # Web colorization results
│   └── templates/                  # HTML templates
│       ├── index.html              # Colorization interface
│       ├── generate.html           # Image generation interface
│       ├── generate_result.html    # Single generation result
│       └── variations_result.html  # Multiple variations result
│
├── 🐳 Docker & Dependencies
│   ├── Dockerfile                  # Container definition
│   ├── docker-compose.yml          # Multi-service setup
│   ├── requirements-ai-generation.txt # Image generation dependencies
│   └── .github/workflows/          # CI/CD pipeline
│
└── 📚 Documentation
    ├── README.md                   # This file
    ├── README_THAI.md              # Thai documentation
    ├── SETUP_COMPLETE.md           # Setup guide
    ├── MODEL_COMPARISON.md         # Model comparison
    └── CONTRIBUTING.md             # Contribution guidelines
```

## 🤖 AI Capabilities

### 🎨 Image Colorization Models

| Model | Size | Best For | Quality | Speed |
|-------|------|----------|---------|-------|
| **Artistic** | 255MB | Portraits, Art | Creative & Vibrant | ⚡ Fast |
| **Stable** | 874MB | Landscapes, Architecture | Realistic & Accurate | 🐌 Slower |

### ✨ Image Generation Features

- **Text-to-Image**: Generate images from descriptive text
- **Style Control**: Adjust guidance scale for creativity vs accuracy
- **Size Options**: 512px, 768px, 1024px generation
- **Seed Control**: Reproducible results with seed values
- **Variations**: Generate multiple styles of the same concept
- **Advanced Parameters**: Steps, guidance, negative prompts

## 🌐 Web Interface

### 🖼️ Colorization Interface
![Colorization Preview](https://via.placeholder.com/800x400?text=Upload+%E2%86%92+Select+Model+%E2%86%92+Colorize+%E2%86%92+Download)

**Features:**
- Drag & drop image upload
- Model selection (Artistic/Stable)
- Real-time progress tracking
- Side-by-side comparison
- Download colorized images

### 🎨 Generation Interface
![Generation Preview](https://via.placeholder.com/800x400?text=Text+Prompt+%E2%86%92+AI+Generation+%E2%86%92+Download)

**Features:**
- Text prompt input with examples
- Advanced parameter controls
- Multiple variations generation
- Real-time generation progress
- Gallery view with download options

## 💡 Usage Examples

### 🖼️ Image Colorization

**CLI Usage:**
```bash
# Basic colorization
python simple_colorizer.py input_images/old_photo.jpg output_images/colorized.jpg

# Specify model
python simple_colorizer.py input_images/portrait.jpg output_images/artistic.jpg --model artistic
python simple_colorizer.py input_images/landscape.jpg output_images/stable.jpg --model stable
```

**Web Usage:**
1. Go to `http://localhost:5000/`
2. Upload your black & white image
3. Choose Artistic or Stable model
4. Click "Colorize Image"
5. Download the result

### 🎨 AI Image Generation

**CLI Usage:**
```bash
# Basic generation
python ai_image_generator.py "a beautiful sunset over mountains"

# Advanced parameters
python ai_image_generator.py "a cyberpunk city at night" --width 1024 --height 1024 --steps 30 --guidance 10.0
```

**Web Usage:**
1. Go to `http://localhost:5000/generate`
2. Enter your text prompt
3. Adjust advanced settings (optional)
4. Click "Generate Image"
5. Download the result

**Example Prompts:**
- `"a majestic lion in the African savanna, golden hour lighting, photorealistic"`
- `"a cyberpunk city at night, neon lights, futuristic buildings, digital art"`
- `"a cute anime girl with blue hair in a magical forest, studio ghibli style"`
- `"abstract art with geometric shapes, vibrant colors, modern style"`
- Real-time processing status
- Instant download of results
- Mobile responsive design

## 💻 System Requirements

- **Python**: 3.8 or higher
- **OS**: Windows, Linux, macOS
- **RAM**: 8GB minimum (16GB recommended)
- **Storage**: 2GB free space
- **GPU**: Optional (CUDA support for faster processing)

## 📦 Dependencies

```txt
torch>=1.7.0
torchvision>=0.8.0
fastai==1.0.61
Flask>=2.0.0
opencv-python>=4.5.0
Pillow>=8.0.0
matplotlib>=3.3.0
numpy>=1.19.0
```

## � Docker Deployment

### Quick Start with Docker
```bash
# Clone repository
git clone https://github.com/NongPO/P_Corlorzed.git
cd P_Corlorzed

# Build and run with Docker Compose
docker-compose up -d

# Access application
open http://localhost:5000
```

### Docker Commands
```bash
# Build image
docker build -t deoldify-colorizer .

# Run container
docker run -p 5000:5000 -v $(pwd)/deoldify_core/models:/app/deoldify_core/models deoldify-colorizer

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### CLI Examples
```bash
# Basic colorization
python simple_colorizer.py input.jpg output.jpg

# Use specific model
python simple_colorizer.py input.jpg output.jpg --model stable

# Batch processing
for img in input_images/*.jpg; do
    python simple_colorizer.py "$img" "output_images/$(basename "$img")"
done
```

### Python API
```python
from simple_colorizer import colorize_image

# Colorize with artistic model
result = colorize_image('input.jpg', model='artistic')

# Colorize with stable model
result = colorize_image('input.jpg', model='stable')
```

## 🔧 Troubleshooting

### Common Issues

1. **ModuleNotFoundError**: Install missing dependencies
   ```bash
   pip install -r deoldify_core/requirements.txt
   ```

2. **Model not found**: Download AI models to `deoldify_core/models/`

3. **Out of memory**: Reduce image size or use CPU mode

4. **Web app not accessible**: Check if port 5000 is available

### Performance Tips

- **GPU Acceleration**: Install CUDA for faster processing
- **Image Size**: Resize large images for better performance
- **Model Selection**: Use Artistic for faster results, Stable for accuracy

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [DeOldify](https://github.com/jantic/DeOldify) - Original framework
- [FastAI](https://fastai.org) - Deep learning library
- [PyTorch](https://pytorch.org) - Neural network framework
- [Flask](https://flask.palletsprojects.com) - Web framework

## 📞 Support

- 📚 **Documentation**: [Thai README](README_THAI.md)
- 🐛 **Issues**: [GitHub Issues](https://github.com/NongPO/P_Corlorzed/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/NongPO/P_Corlorzed/discussions)

---

<div align="center">

**⭐ Star this repository if you find it helpful! ⭐**

Made with ❤️ by [NongPO](https://github.com/NongPO)

</div>
