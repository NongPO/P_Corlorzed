#!/usr/bin/env python3
"""
Simple DeOldify Image Colorizer
Usage: python simple_colorizer.py input_image.jpg [output_image.jpg] [--render_factor=35]
"""

import sys
import os
import argparse
from pathlib import Path

# Add DeOldify to path
sys.path.append('DeOldify')

def colorize_image(input_path, output_path=None, render_factor=35, model_type='artistic'):
    """
    Colorize a black and white image using DeOldify
    
    Args:
        input_path (str): Path to input image
        output_path (str): Path for output image (optional)
        render_factor (int): Quality factor (7-45, higher = better quality but slower)
        model_type (str): 'artistic' or 'stable'
    """
    try:
        # Change to DeOldify directory and add to path
        original_dir = os.getcwd()
        deoldify_path = os.path.join(original_dir, 'deoldify_core')
        os.chdir(deoldify_path)
        sys.path.insert(0, deoldify_path)
        
        # Import DeOldify modules (suppress IDE warnings with try/except)
        try:
            from deoldify.visualize import get_image_colorizer  # type: ignore
        except ImportError as ie:
            print(f"Failed to import DeOldify: {ie}")
            print("Make sure you're running from the correct directory with DeOldify folder present.")
            return None
        
        print(f"Loading {model_type} model...")
        
        # Get colorizer based on model type with error handling
        try:
            if model_type.lower() == 'artistic':
                colorizer = get_image_colorizer(artistic=True)
                print("✅ Artistic model loaded successfully")
            else:
                print("Loading Stable model...")
                colorizer = get_image_colorizer(artistic=False)
                print("✅ Stable model loaded successfully")
        except Exception as model_error:
            print(f"❌ Error loading {model_type} model: {model_error}")
            print("🔄 Falling back to Artistic model...")
            try:
                colorizer = get_image_colorizer(artistic=True)
                print("✅ Fallback to Artistic model successful")
                model_type = 'artistic_fallback'
            except Exception as fallback_error:
                print(f"❌ Failed to load any model: {fallback_error}")
                return None
        
        print(f"Colorizing image: {input_path}")
        print(f"Render factor: {render_factor}")
        
        # Convert input path to relative path from DeOldify directory
        input_rel_path = os.path.join('..', input_path)
        
        # Colorize the image
        result_path = colorizer.plot_transformed_image(
            path=input_rel_path, 
            render_factor=render_factor,
            display_render_factor=True,
            figsize=(20,20)
        )
        
        print(f"DeOldify result saved to: {result_path}")
        
        # Change back to original directory
        os.chdir(original_dir)
        
        # If output path is specified, copy the result there
        if output_path:
            import shutil
            # The result is usually in DeOldify/result_images/
            deoldify_result = os.path.join('DeOldify', 'result_images', os.path.basename(input_path))
            
            if os.path.exists(deoldify_result):
                # Create output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy2(deoldify_result, output_path)
                print(f"Result copied to: {output_path}")
            elif result_path and os.path.exists(result_path):
                os.makedirs(os.path.dirname(output_path), exist_ok=True)
                shutil.copy2(result_path, output_path)
                print(f"Result copied to: {output_path}")
            else:
                print(f"Warning: Could not find result file")
                print(f"Check DeOldify/result_images/ folder for the output")
        else:
            # If no output path specified, show where the result is
            deoldify_result = os.path.join('DeOldify', 'result_images', os.path.basename(input_path))
            if os.path.exists(deoldify_result):
                print(f"Result saved to: {deoldify_result}")
        
        print("Colorization completed!")
        return result_path
        
    except Exception as e:
        # Make sure to change back to original directory
        try:
            os.chdir(original_dir)
        except:
            pass
        print(f"Error during colorization: {str(e)}")
        print("Make sure you have all required dependencies installed.")
        return None

def main():
    parser = argparse.ArgumentParser(description='Colorize black and white images using DeOldify')
    parser.add_argument('input', help='Input image path')
    parser.add_argument('output', nargs='?', help='Output image path (optional)')
    parser.add_argument('--render_factor', type=int, default=35, 
                       help='Render factor (7-45, higher = better quality but slower)')
    parser.add_argument('--model', choices=['artistic', 'stable'], default='artistic',
                       help='Model type to use')
    
    args = parser.parse_args()
    
    # Validate input file
    if not os.path.exists(args.input):
        print(f"Error: Input file '{args.input}' not found!")
        return 1
    
    # Generate output filename if not provided
    output_path = args.output
    if not output_path:
        input_path = Path(args.input)
        output_path = str(input_path.parent / f"{input_path.stem}_colorized{input_path.suffix}")
    
    # Validate render factor
    if not (7 <= args.render_factor <= 45):
        print("Warning: Render factor should be between 7-45 for best results")
    
    # Colorize the image
    result = colorize_image(
        input_path=args.input,
        output_path=output_path, 
        render_factor=args.render_factor,
        model_type=args.model
    )
    
    return 0 if result else 1

if __name__ == "__main__":
    sys.exit(main())
