FROM python:3.10-alpine3.15

COPY . /app

WORKDIR /app

# Needed for Pillow, Numpy, and ffmpeg
RUN apk add --update --no-cache tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev g++ ffmpeg

RUN pip install --upgrade pip; pip install -r requirements.txt --no-cache-dir

CMD ["python main.py"]
