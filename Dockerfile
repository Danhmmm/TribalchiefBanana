# Dùng Python base image
FROM python:3.10-slim

# Cài đặt một số gói bổ sung cần thiết cho torch
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Đặt thư mục làm việc
WORKDIR /app

# Copy requirements & cài đặt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy toàn bộ code
COPY . .

# Chạy chương trình
CMD ["python", "Cloud.py"]
