
FROM python:3.11

# Set the working directory
WORKDIR /Movie_Recommender

# Copy requirements.txt to the container
COPY requirements.txt .

# Install build dependencies
RUN apt-get update && \
    apt-get install -y build-essential

# Install production dependencies.
RUN pip install -r requirements.txt

# Copy the local code to the container
COPY . .

# Expose port 8501
EXPOSE 8501

# Run the Streamlit app on container startup
CMD ["streamlit", "run", "--server.port", "8501", "--server.enableCORS", "false", "app.py"]
