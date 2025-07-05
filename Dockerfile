# Chọn Python base image
FROM python:3.10-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy requirements & cài đặt
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install fastapi uvicorn

# Copy toàn bộ code
COPY . .

# Chạy API
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
