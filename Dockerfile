FROM python:3.10.6-buster

COPY . .

WORKDIR /app

# Needed ffmpeg clears apt cache after upgerade
RUN apt-get update && apt-get install -y ffmpeg \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip; pip install -r requirements.txt --no-cache-dir

RUN mkdir -p ./anipy-cli_output/download

RUN mv /app/config.py /usr/local/lib/python3.10/site-packages/anipy_cli/config.py

ENTRYPOINT ["python", "main.py"]
