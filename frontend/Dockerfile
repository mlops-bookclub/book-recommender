FROM python:3.12-slim


WORKDIR /app

# Install dependencies first (layer-cached separately from source code)
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy application source
COPY frontend/src ./src/

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "./src/main.py", "--server.port=8501", "--server.address=0.0.0.0"]
