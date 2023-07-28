# Use the official Python base image
FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    python3-dev \
    postgresql \
    postgresql-contrib

# Set the working directory in the container
WORKDIR /app

# Copy your Django app code into the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt
# Install the OpenAI library
RUN pip install --no-cache-dir openai

# Set the environment variable for the OpenAI API key
ENV OPENAI_API_KEY="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"

# Set the environment variable for the Bard API key
ENV BARD_API_KEY="ZAg7RrKFc0wJsb_x6oyIqJLL--PDSWnnlzKklbeb9hpIToVDN0cKmxxpPliSvLzYxsAFEA."

# Set environment variables for PostgreSQL database configuration
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=mydatabaseuser
ENV POSTGRES_PASSWORD=mydatabasepassword
ENV POSTGRES_HOST=db  

# Expose the port on which your Django app runs (if needed)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
