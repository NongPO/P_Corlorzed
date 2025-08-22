#!/usr/bin/env python3
"""
🎨 AI Image Generator
Generate images from text prompts using Stable Diffusion
"""

import os
import sys
import torch
import requests
from pathlib import Path
from PIL import Image
import numpy as np
from typing import Optional, List, Tuple
import uuid
from datetime import datetime

# Try to import diffusers for local generation
try:
    from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
    DIFFUSERS_AVAILABLE = True
    print("✅ Diffusers library found - Local AI generation available")
except ImportError:
    DIFFUSERS_AVAILABLE = False
    print("⚠️ Diffusers not installed. Install with: pip install diffusers")
    print("💡 Only API-based generation will be available.")

class AIImageGenerator:
    """AI Image Generator class supporting multiple backends"""
    
    def __init__(self, use_local: bool = True, model_name: str = "runwayml/stable-diffusion-v1-5"):
        self.use_local = use_local and DIFFUSERS_AVAILABLE
        self.model_name = model_name
        self.pipeline = None
        self.device = self._get_device()
        
        if self.use_local:
            self._load_local_model()
    
    def _get_device(self) -> str:
        """Detect available device"""
        if torch.cuda.is_available():
            return "cuda"
        elif hasattr(torch.backends, 'mps') and torch.backends.mps.is_available():
            return "mps"  # Apple Silicon
        else:
            return "cpu"
    
    def _load_local_model(self):
        """Load Stable Diffusion model locally"""
        try:
            print(f"🤖 Loading Stable Diffusion model: {self.model_name}")
            print(f"📱 Device: {self.device}")
            
            self.pipeline = StableDiffusionPipeline.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32,
                safety_checker=None,
                requires_safety_checker=False
            )
            
            # Optimize scheduler
            self.pipeline.scheduler = DPMSolverMultistepScheduler.from_config(
                self.pipeline.scheduler.config
            )
            
            # Move to device
            self.pipeline = self.pipeline.to(self.device)
            
            # Enable memory efficient attention if available
            if hasattr(self.pipeline, "enable_attention_slicing"):
                self.pipeline.enable_attention_slicing()
            
            if hasattr(self.pipeline, "enable_xformers_memory_efficient_attention"):
                try:
                    self.pipeline.enable_xformers_memory_efficient_attention()
                except:
                    pass  # xformers not available
            
            print("✅ Model loaded successfully!")
            
        except Exception as e:
            print(f"❌ Failed to load local model: {e}")
            print("💡 Falling back to API-based generation")
            self.use_local = False
            self.pipeline = None
    
    def generate_image(
        self,
        prompt: str,
        negative_prompt: str = "blurry, low quality, distorted, ugly, bad anatomy",
        width: int = 512,
        height: int = 512,
        num_inference_steps: int = 20,
        guidance_scale: float = 7.5,
        seed: Optional[int] = None,
        output_dir: str = "generated_images"
    ) -> str:
        """
        Generate image from text prompt
        
        Args:
            prompt: Text description of desired image
            negative_prompt: What to avoid in the image
            width: Image width
            height: Image height
            num_inference_steps: Number of denoising steps
            guidance_scale: How closely to follow the prompt
            seed: Random seed for reproducibility
            output_dir: Directory to save generated images
            
        Returns:
            Path to generated image
        """
        
        # Create output directory
        Path(output_dir).mkdir(exist_ok=True)
        
        # Generate unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        image_id = str(uuid.uuid4())[:8]
        filename = f"generated_{timestamp}_{image_id}.png"
        output_path = Path(output_dir) / filename
        
        if self.use_local and self.pipeline:
            return self._generate_local(
                prompt, negative_prompt, width, height,
                num_inference_steps, guidance_scale, seed, output_path
            )
        else:
            return self._generate_api(
                prompt, negative_prompt, width, height, output_path
            )
    
    def _generate_local(
        self,
        prompt: str,
        negative_prompt: str,
        width: int,
        height: int,
        num_inference_steps: int,
        guidance_scale: float,
        seed: Optional[int],
        output_path: Path
    ) -> str:
        """Generate image using local Stable Diffusion model"""
        
        print(f"🎨 Generating image locally...")
        print(f"📝 Prompt: {prompt}")
        print(f"🚫 Negative: {negative_prompt}")
        print(f"📐 Size: {width}x{height}")
        
        # Set seed for reproducibility
        if seed is not None:
            torch.manual_seed(seed)
            if torch.cuda.is_available():
                torch.cuda.manual_seed(seed)
        
        try:
            # Generate image with progress tracking (updated for newer diffusers)
            def progress_callback(pipe, step, timestep, callback_kwargs):
                progress = (step / num_inference_steps) * 100
                print(f"Progress: {progress:.1f}% ({step}/{num_inference_steps})")
                return callback_kwargs
            
            with torch.autocast(self.device):
                result = self.pipeline(
                    prompt=prompt,
                    negative_prompt=negative_prompt,
                    width=width,
                    height=height,
                    num_inference_steps=num_inference_steps,
                    guidance_scale=guidance_scale,
                    callback_on_step_end=progress_callback
                )
            
            image = result.images[0]
            
            # Save image
            image.save(output_path)
            print(f"✅ Image generated: {output_path}")
            
            return str(output_path)
            
        except Exception as e:
            print(f"❌ Local generation failed: {e}")
            raise
    
    def _generate_api(
        self,
        prompt: str,
        negative_prompt: str,
        width: int,
        height: int,
        output_path: Path
    ) -> str:
        """Generate image using external API (Hugging Face, etc.)"""
        
        print(f"🌐 Generating image via API...")
        print(f"📝 Prompt: {prompt}")
        
        # This is a placeholder for API-based generation
        # You can integrate with services like:
        # - Hugging Face Inference API
        # - OpenAI DALL-E
        # - Stability AI API
        # - Replicate API
        
        try:
            # Example: Create a placeholder image
            placeholder_image = Image.new('RGB', (width, height), color='lightblue')
            
            # Add text to indicate API generation
            from PIL import ImageDraw, ImageFont
            draw = ImageDraw.Draw(placeholder_image)
            
            try:
                # Try to use a default font
                font = ImageFont.load_default()
            except:
                font = None
            
            text = f"API Generated\n{prompt[:50]}..."
            draw.text((10, 10), text, fill='black', font=font)
            
            placeholder_image.save(output_path)
            print(f"✅ Placeholder image created: {output_path}")
            print("💡 Integrate with your preferred AI API for real generation")
            
            return str(output_path)
            
        except Exception as e:
            print(f"❌ API generation failed: {e}")
            raise
    
    def generate_variations(
        self,
        base_prompt: str,
        variations: List[str],
        output_dir: str = "generated_images"
    ) -> List[str]:
        """Generate multiple variations of a base prompt"""
        
        results = []
        for i, variation in enumerate(variations):
            full_prompt = f"{base_prompt}, {variation}"
            try:
                result_path = self.generate_image(
                    prompt=full_prompt,
                    output_dir=output_dir
                )
                results.append(result_path)
                print(f"✅ Variation {i+1}/{len(variations)} completed")
            except Exception as e:
                print(f"❌ Variation {i+1} failed: {e}")
                results.append(None)
        
        return results
    
    def get_model_info(self) -> dict:
        """Get information about the current model"""
        return {
            "use_local": self.use_local,
            "model_name": self.model_name if self.use_local else "API-based",
            "device": self.device,
            "diffusers_available": DIFFUSERS_AVAILABLE
        }

def main():
    """Command line interface for AI image generation"""
    import argparse
    
    parser = argparse.ArgumentParser(description="🎨 AI Image Generator")
    parser.add_argument("prompt", help="Text prompt for image generation")
    parser.add_argument("--negative", default="blurry, low quality", 
                       help="Negative prompt")
    parser.add_argument("--width", type=int, default=512, help="Image width")
    parser.add_argument("--height", type=int, default=512, help="Image height")
    parser.add_argument("--steps", type=int, default=20, 
                       help="Number of inference steps")
    parser.add_argument("--guidance", type=float, default=7.5, 
                       help="Guidance scale")
    parser.add_argument("--seed", type=int, help="Random seed")
    parser.add_argument("--output", default="generated_images", 
                       help="Output directory")
    parser.add_argument("--api-only", action="store_true", 
                       help="Use API-only mode")
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = AIImageGenerator(use_local=not args.api_only)
    
    # Print model info
    info = generator.get_model_info()
    print(f"🤖 Model: {info['model_name']}")
    print(f"📱 Device: {info['device']}")
    print(f"🏠 Local: {info['use_local']}")
    print()
    
    try:
        # Generate image
        result_path = generator.generate_image(
            prompt=args.prompt,
            negative_prompt=args.negative,
            width=args.width,
            height=args.height,
            num_inference_steps=args.steps,
            guidance_scale=args.guidance,
            seed=args.seed,
            output_dir=args.output
        )
        
        print(f"\n🎉 Image generated successfully!")
        print(f"📁 Saved to: {result_path}")
        
    except Exception as e:
        print(f"\n❌ Generation failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
