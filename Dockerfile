FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    libgl1-mesa-glx \
    libgl1-mesa-dri \
    ffmpeg \
    swig \
    && rm -rf /var/lib/apt/lists/*

# Copy everything into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -e .

CMD ["tail", "-f", "/dev/null"]