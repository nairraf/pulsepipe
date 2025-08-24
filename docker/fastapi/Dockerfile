# Use a slim Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Install dependencies early to leverage Docker layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire source code (modular structure assumed)
COPY . .

# Run FastAPI using Uvicorn
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]