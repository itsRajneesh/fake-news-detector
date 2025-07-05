# Use official Python 3.10 image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . .

# Expose port (Render uses 10000+ by default)
EXPOSE 10000

# Start the app with gunicorn
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:10000"]
