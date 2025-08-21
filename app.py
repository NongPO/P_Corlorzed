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

app = Flask(__name__)
app.secret_key = 'deoldify_secret_key_2024'

# Configuration
UPLOAD_FOLDER = 'uploads'
RESULT_FOLDER = 'results'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

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
        
        # Get colorizer
        if model_type.lower() == 'artistic':
            colorizer = get_image_colorizer(artistic=True)
        else:
            colorizer = get_image_colorizer(artistic=False)
        
        # Convert input path to relative path from DeOldify directory
        input_rel_path = os.path.join('..', input_path)
        
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
        
        # Get parameters
        render_factor = int(request.form.get('render_factor', 25))
        model_type = request.form.get('model_type', 'artistic')
        
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

if __name__ == '__main__':
    print("🎨 Starting DeOldify Web App...")
    print("📁 Upload folder:", UPLOAD_FOLDER)
    print("📁 Result folder:", RESULT_FOLDER)
    print("🌐 Open your browser and go to: http://localhost:5000")
    print("✨ Ready to colorize your images!")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
