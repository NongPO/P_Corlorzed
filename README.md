# 🎨 DeOldify Image Colorizer

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![FastAI](https://img.shields.io/badge/FastAI-1.0.61-orange.svg)](https://fastai.org)
[![Flask](https://img.shields.io/badge/Flask-Web_App-green.svg)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **AI-powered tool to colorize black and white images using DeOldify framework**

Transform your old black and white photos into vibrant colorized images using state-of-the-art deep learning models.

## ✨ Features

- 🖼️ **CLI Tool**: Command-line interface for batch processing
- 🌐 **Web Application**: User-friendly web interface with Flask
- 🤖 **Dual AI Models**: 
  - **Artistic Model** (255MB): Creative, vibrant colorization
  - **Stable Model** (874MB): Realistic, accurate colorization
- 🚀 **Easy Setup**: Windows batch files for quick execution
- 📱 **Responsive Design**: Mobile-friendly web interface

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

**Option C: Docker (Includes models)**
```bash
docker-compose up -d
```

### 4. Run Application

#### Option A: Web Interface
```bash
python app.py
# Open http://localhost:5000
```

#### Option B: Command Line
```bash
python simple_colorizer.py input_images/photo.jpg output_images/colorized.jpg
```

#### Option C: Windows Shortcuts
- Double-click `run_web.bat` for web interface
- Double-click `colorize.bat` for CLI tool

## 📁 Project Structure

```
P_Corlorzed/
├── 🎨 Main Tools
│   ├── simple_colorizer.py    # CLI colorization tool
│   ├── app.py                 # Flask web application
│   ├── colorize.bat          # Windows CLI shortcut
│   └── run_web.bat           # Windows web shortcut
│
├── 🧠 AI Core
│   └── deoldify_core/
│       ├── models/           # AI models (download required)
│       ├── deoldify/         # Core DeOldify framework
│       ├── fastai/           # FastAI integration
│       └── requirements.txt  # Python dependencies
│
├── 📁 Directories
│   ├── input_images/         # Source images
│   ├── output_images/        # CLI results
│   ├── uploads/              # Web uploads
│   ├── results/              # Web results
│   └── templates/            # HTML templates
│
└── 📚 Documentation
    ├── README.md             # This file
    ├── README_THAI.md        # Thai documentation
    ├── SETUP_COMPLETE.md     # Setup guide
    └── MODEL_COMPARISON.md   # Model comparison
```

## 🤖 AI Models Comparison

| Model | Size | Best For | Quality | Speed |
|-------|------|----------|---------|-------|
| **Artistic** | 255MB | Portraits, Art | Creative & Vibrant | ⚡ Fast |
| **Stable** | 874MB | Landscapes, Architecture | Realistic & Accurate | 🐌 Slower |

## 🌐 Web Interface

![Web Interface Preview](https://via.placeholder.com/800x400?text=Upload+%E2%86%92+Select+Model+%E2%86%92+Colorize+%E2%86%92+Download)

**Features:**
- Drag & drop image upload
- Model selection (Artistic/Stable)
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
