# 🎨 DeOldify AI Studio Docker Image
# Supports both image colorization and AI generation
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    wget \
    curl \
    git \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY deoldify_core/requirements.txt deoldify_requirements.txt
COPY requirements-ai-generation.txt ai_requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r deoldify_requirements.txt
RUN pip install --no-cache-dir -r ai_requirements.txt

# Install FastAI version for compatibility
RUN pip install fastai==1.0.61

# Copy application code
COPY . .

# Create necessary directories
RUN mkdir -p uploads results generated_images output_images deoldify_core/models

# Download models on first run (optional, can be mounted as volume)
# RUN python download_models.py

# Expose port
EXPOSE 5000

# Environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=production
ENV PYTHONPATH=/app

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/ || exit 1

# Run the application
CMD ["python", "app.py"]
