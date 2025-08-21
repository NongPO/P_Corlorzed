#!/usr/bin/env python3
"""
🎨 DeOldify Model Downloader
Download required AI models for image colorization
"""

import os
import sys
import requests
from pathlib import Path
import hashlib
from tqdm import tqdm

# Model information
MODELS = {
    'artistic': {
        'url': 'https://data.deepai.org/deoldify/ColorizeArtistic_gen.pth',
        'filename': 'ColorizeArtistic_gen.pth',
        'size': 255 * 1024 * 1024,  # 255MB
        'description': 'Artistic model - Creative and vibrant colorization'
    },
    'stable': {
        'url': 'https://www.dropbox.com/s/usf7uifrctqw9rl/ColorizeStable_gen.pth?dl=1',
        'filename': 'ColorizeStable_gen.pth', 
        'size': 874 * 1024 * 1024,  # 874MB
        'description': 'Stable model - Realistic and accurate colorization'
    }
}

def format_size(size_bytes):
    """Convert bytes to human readable format"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"

def download_file(url, filepath, expected_size=None):
    """Download file with progress bar"""
    print(f"📥 Downloading: {filepath.name}")
    print(f"🔗 URL: {url}")
    
    response = requests.get(url, stream=True)
    response.raise_for_status()
    
    total_size = int(response.headers.get('content-length', 0))
    if expected_size and total_size == 0:
        total_size = expected_size
    
    with open(filepath, 'wb') as file, tqdm(
        desc=filepath.name,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as pbar:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)
                pbar.update(len(chunk))
    
    print(f"✅ Downloaded: {filepath} ({format_size(filepath.stat().st_size)})")

def verify_model(filepath, expected_size=None):
    """Verify downloaded model"""
    if not filepath.exists():
        return False, "File not found"
    
    file_size = filepath.stat().st_size
    if expected_size and abs(file_size - expected_size) > (expected_size * 0.1):  # 10% tolerance
        return False, f"Size mismatch: {format_size(file_size)} (expected ~{format_size(expected_size)})"
    
    # Check if file is not empty and not obviously corrupted
    if file_size < 1024:  # Less than 1KB is suspicious
        return False, "File too small, possibly corrupted"
    
    return True, "OK"

def main():
    """Main download function"""
    print("🎨 DeOldify Model Downloader")
    print("=" * 50)
    
    # Create models directory
    models_dir = Path(__file__).parent / 'deoldify_core' / 'models'
    models_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"📁 Models directory: {models_dir}")
    print()
    
    # Check which models to download
    download_all = len(sys.argv) == 1 or 'all' in sys.argv
    download_artistic = download_all or 'artistic' in sys.argv
    download_stable = download_all or 'stable' in sys.argv
    
    if len(sys.argv) > 1 and not download_all:
        print(f"📋 Requested models: {', '.join(sys.argv[1:])}")
    else:
        print("📋 Downloading all models")
    print()
    
    # Download models
    for model_name, model_info in MODELS.items():
        if (model_name == 'artistic' and not download_artistic) or \
           (model_name == 'stable' and not download_stable):
            continue
            
        filepath = models_dir / model_info['filename']
        
        print(f"🤖 Model: {model_name.title()}")
        print(f"📝 Description: {model_info['description']}")
        print(f"📊 Expected size: {format_size(model_info['size'])}")
        
        # Check if already exists
        if filepath.exists():
            is_valid, message = verify_model(filepath, model_info['size'])
            if is_valid:
                print(f"✅ Model already exists and verified: {filepath}")
                print()
                continue
            else:
                print(f"⚠️ Existing model invalid ({message}), re-downloading...")
        
        try:
            download_file(model_info['url'], filepath, model_info['size'])
            
            # Verify download
            is_valid, message = verify_model(filepath, model_info['size'])
            if is_valid:
                print(f"✅ Download verified: {message}")
            else:
                print(f"❌ Download verification failed: {message}")
                filepath.unlink()  # Delete corrupted file
                
        except Exception as e:
            print(f"❌ Download failed: {e}")
            if filepath.exists():
                filepath.unlink()
        
        print()
    
    # Summary
    print("📋 Download Summary:")
    print("-" * 30)
    
    total_size = 0
    for model_name, model_info in MODELS.items():
        filepath = models_dir / model_info['filename']
        if filepath.exists():
            size = filepath.stat().st_size
            total_size += size
            print(f"✅ {model_name.title()}: {format_size(size)}")
        else:
            print(f"❌ {model_name.title()}: Not downloaded")
    
    print(f"\n📊 Total size: {format_size(total_size)}")
    
    if total_size > 0:
        print("\n🎉 Ready to colorize images!")
        print("📚 Usage:")
        print("   CLI: python simple_colorizer.py input.jpg output.jpg")
        print("   Web: python app.py")
    else:
        print("\n⚠️ No models downloaded. Please check your internet connection.")

if __name__ == "__main__":
    main()
