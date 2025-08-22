#!/usr/bin/env python3
"""
Test AI Image Generator
"""

print("🧪 Testing AI Image Generator...")

try:
    print("📦 Importing libraries...")
    import torch
    print(f"✅ PyTorch {torch.__version__}")
    
    import diffusers
    print(f"✅ Diffusers {diffusers.__version__}")
    
    from ai_image_generator import AIImageGenerator
    print("✅ AI Image Generator imported")
    
    print("🤖 Creating generator (API mode)...")
    generator = AIImageGenerator(use_local=False)
    
    print("📊 Model info:")
    info = generator.get_model_info()
    for key, value in info.items():
        print(f"  - {key}: {value}")
    
    print("🎨 Testing placeholder generation...")
    result = generator.generate_image(
        prompt="a beautiful sunset",
        output_dir="generated_images"
    )
    print(f"✅ Generated: {result}")
    
    print("🎉 All tests passed!")
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
