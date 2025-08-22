#!/usr/bin/env python3
"""
DeOldify Web Application
Upload and colorize black and white images through web interface
"""

import os
import sys
from flask import Flask, request, render_template, redirect, url_for, flash, send_file, jsonify
from werkzeug.utils import secure_filename
import uuid
from datetime import datetime

# Add DeOldify to path
sys.path.insert(0, 'deoldify_core')

# Import AI modules
try:
    from simple_colorizer import SimpleColorizer
    print("✅ SimpleColorizer imported successfully")
except ImportError as e:
    print(f"⚠️ Failed to import SimpleColorizer: {e}")
    SimpleColorizer = None

try:
    from ai_image_generator import AIImageGenerator
    print("✅ AIImageGenerator imported successfully")
except ImportError as e:
    print(f"⚠️ Failed to import AIImageGenerator: {e}")
    AIImageGenerator = None

app = Flask(__name__)
app.secret_key = 'deoldify_secret_key_2024'

# Configuration
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
GENERATED_FOLDER = 'generated_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['GENERATED_FOLDER'] = GENERATED_FOLDER

# Create directories
for folder in [UPLOAD_FOLDER, RESULT_FOLDER, GENERATED_FOLDER]:
    os.makedirs(folder, exist_ok=True)

# Initialize AI models
colorizer = SimpleColorizer() if SimpleColorizer else None
image_generator = AIImageGenerator() if AIImageGenerator else None
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def colorize_image_web(input_path, output_path, render_factor=25, model_type='artistic'):
    """
    Colorize image for web interface
    """
    try:
        # Save current directory and change to DeOldify
        original_dir = os.getcwd()
        deoldify_path = os.path.join(original_dir, 'deoldify_core')
        os.chdir(deoldify_path)
        
        # Import DeOldify
        from deoldify.visualize import get_image_colorizer
        
        print(f"Loading {model_type} colorizer...")
        
        # Get colorizer with map_location handling
        import torch
        import sys
        sys.path.insert(0, deoldify_path)
        from fastai.core import defaults
        device = 'cpu' if torch.cuda.device_count() == 0 else 'cuda'
        defaults.device = torch.device(device)
        print(f"Using device: {device}")
        
        if model_type.lower() == 'artistic':
            colorizer = get_image_colorizer(artistic=True)
        else:
            colorizer = get_image_colorizer(artistic=False)
        
        print("Colorizer loaded successfully")
        
        # Convert input path to relative path from DeOldify directory
        input_rel_path = os.path.join('..', input_path)
        
        print(f"Colorizing: {input_rel_path}")
        
        # Colorize the image
        result_path = colorizer.plot_transformed_image(
            path=input_rel_path, 
            render_factor=render_factor,
            display_render_factor=True,
            figsize=(20,20)
        )
        
        # Change back to original directory
        os.chdir(original_dir)
        
        # Copy result to output path
        import shutil
        deoldify_result_dir = os.path.join('deoldify_core', 'result_images')
        
        # Find the result file (should be the newest file in result_images)
        if os.path.exists(deoldify_result_dir):
            import glob
            result_files = glob.glob(os.path.join(deoldify_result_dir, '*'))
            if result_files:
                newest_result = max(result_files, key=os.path.getmtime)
                shutil.copy2(newest_result, output_path)
                return True
        
        return False
        
    except Exception as e:
        print(f"Error in colorization: {e}")
        # Make sure to change back to original directory
        try:
            os.chdir(original_dir)
        except:
            pass
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('ไม่มีไฟล์ที่เลือก')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('ไม่ได้เลือกไฟล์')
        return redirect(request.url)
    
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = secure_filename(file.filename)
        unique_id = str(uuid.uuid4())[:8]
        name, ext = os.path.splitext(filename)
        unique_filename = f"{name}_{unique_id}{ext}"
        
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file.save(file_path)
        
        # Get parameters with error handling
        try:
            render_factor = int(request.form.get('render_factor', 25) or 25)
            model_type = request.form.get('model_type', 'artistic')
        except (ValueError, TypeError) as e:
            flash(f'Invalid render factor: {str(e)}', 'error')
            return redirect(url_for('index'))
        
        # Generate output filename
        output_filename = f"colorized_{unique_filename}"
        output_path = os.path.join(app.config['RESULT_FOLDER'], output_filename)
        
        # Colorize the image
        success = colorize_image_web(file_path, output_path, render_factor, model_type)
        
        if success:
            return render_template('result.html', 
                                 original_file=unique_filename,
                                 result_file=output_filename,
                                 render_factor=render_factor,
                                 model_type=model_type)
        else:
            flash('เกิดข้อผิดพลาดในการแปลงภาพ')
            return redirect(url_for('index'))
    
    flash('ไฟล์ไม่ถูกต้อง กรุณาเลือกไฟล์รูปภาพ')
    return redirect(url_for('index'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_file(os.path.join(app.config['RESULT_FOLDER'], filename), as_attachment=True)

@app.route('/view/<path:filename>')
def view_file(filename):
    if filename.startswith('uploads/'):
        return send_file(filename)
    elif filename.startswith('results/'):
        return send_file(filename)
    else:
        return "File not found", 404

# ================== AI IMAGE GENERATION ROUTES ==================

@app.route('/generate')
def generate_page():
    """Show AI image generation page"""
    if not image_generator:
        flash('AI Image Generator is not available. Please install dependencies.', 'error')
        return redirect(url_for('index'))
    return render_template('generate.html')

@app.route('/generate_image', methods=['POST'])
def generate_image():
    """Generate image from text prompt"""
    if not image_generator:
        flash('AI Image Generator is not available. Please install dependencies.', 'error')
        return redirect(url_for('index'))
        
    try:
        prompt = request.form.get('prompt', '').strip()
        negative_prompt = request.form.get('negative_prompt', 'blurry, low quality, distorted')
        
        if not prompt:
            flash('Please enter a text prompt!', 'error')
            return redirect(url_for('generate_page'))
        
        # Get generation parameters with error handling
        try:
            width = int(request.form.get('width', 512) or 512)
            height = int(request.form.get('height', 512) or 512)
            steps = int(request.form.get('steps', 20) or 20)
            guidance = float(request.form.get('guidance', 7.5) or 7.5)
            
            # Handle seed parameter (can be empty)
            seed = request.form.get('seed', '').strip()
            if seed:
                seed = int(seed)
            else:
                seed = None
                
        except (ValueError, TypeError) as e:
            flash(f'Invalid parameter values: {str(e)}', 'error')
            return redirect(url_for('generate_page'))
        
        print(f"🎨 Generating image with prompt: {prompt}")
        
        # Generate image
        result_path = image_generator.generate_image(
            prompt=prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            num_inference_steps=steps,
            guidance_scale=guidance,
            seed=seed,
            output_dir=GENERATED_FOLDER
        )
        
        # Get just the filename for display
        filename = os.path.basename(result_path)
        
        flash(f'Image generated successfully! Prompt: "{prompt}"', 'success')
        return render_template('generate_result.html', 
                             result_image=filename,
                             prompt=prompt,
                             parameters={
                                 'negative_prompt': negative_prompt,
                                 'width': width,
                                 'height': height,
                                 'steps': steps,
                                 'guidance': guidance,
                                 'seed': seed
                             })
        
    except Exception as e:
        error_msg = f"Generation failed: {str(e)}"
        print(f"❌ {error_msg}")
        flash(error_msg, 'error')
        return redirect(url_for('generate_page'))

@app.route('/generate_variations', methods=['POST'])
def generate_variations():
    """Generate multiple variations of a prompt"""
    if not image_generator:
        flash('AI Image Generator is not available. Please install dependencies.', 'error')
        return redirect(url_for('index'))
        
    try:
        base_prompt = request.form.get('base_prompt', '').strip()
        variations_text = request.form.get('variations', '').strip()
        
        if not base_prompt or not variations_text:
            flash('Please enter both base prompt and variations!', 'error')
            return redirect(url_for('generate_page'))
        
        # Parse variations
        variations = [v.strip() for v in variations_text.split('\n') if v.strip()]
        
        if not variations:
            flash('Please enter at least one variation!', 'error')
            return redirect(url_for('generate_page'))
        
        print(f"🎨 Generating {len(variations)} variations for: {base_prompt}")
        
        # Generate variations
        results = image_generator.generate_variations(
            base_prompt=base_prompt,
            variations=variations,
            output_dir=GENERATED_FOLDER
        )
        
        # Filter successful results
        successful_results = [(var, res) for var, res in zip(variations, results) if res]
        
        if successful_results:
            flash(f'Generated {len(successful_results)} variations successfully!', 'success')
            return render_template('variations_result.html',
                                 results=successful_results,
                                 base_prompt=base_prompt)
        else:
            flash('Failed to generate any variations!', 'error')
            return redirect(url_for('generate_page'))
            
    except Exception as e:
        error_msg = f"Variation generation failed: {str(e)}"
        print(f"❌ {error_msg}")
        flash(error_msg, 'error')
        return redirect(url_for('generate_page'))

@app.route('/generated_images/<filename>')
def generated_image(filename):
    """Serve generated images"""
    try:
        return send_file(os.path.join(GENERATED_FOLDER, filename))
    except FileNotFoundError:
        return "Generated image not found", 404

if __name__ == '__main__':
    print("🎨 Starting DeOldify Web App...")
    print("📁 Upload folder:", UPLOAD_FOLDER)
    print("📁 Result folder:", RESULT_FOLDER)
    print("📁 Generated folder:", GENERATED_FOLDER)
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("✨ Ready to colorize and generate images!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
