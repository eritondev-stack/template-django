FROM python:3.12-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
# cole os estáticos
RUN python manage.py collectstatic --noinput

EXPOSE 8000
# 1 worker para não precisar de Redis
CMD ["uvicorn", "config.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
