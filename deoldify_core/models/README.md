# AI Models Directory

This directory should contain the DeOldify pre-trained models:

## Required Files:
- `ColorizeArtistic_gen.pth` (255 MB) - For artistic colorization
- `ColorizeStable_gen.pth` (874 MB) - For stable/realistic colorization

## Download Instructions:
Due to GitHub file size limitations, these models are not included in the repository.

### Option 1: Download from Original DeOldify Repository
```bash
# Download Artistic model
wget https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth

# Download Stable model  
wget https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth
```

### Option 2: Use the provided download script
```bash
python download_models.py
```

## File Structure:
```
models/
├── .gitkeep
├── README.md (this file)
├── ColorizeArtistic_gen.pth    # 255 MB
└── ColorizeStable_gen.pth      # 874 MB
```

## Note:
- Models are excluded from Git due to size limitations (GitHub max: 100MB)
- Models must be downloaded separately after cloning the repository
- Both models are required for full functionality
