FROM python:3.12-slim

# 環境変数
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# アプリ用ディレクトリ
WORKDIR /app

# システムパッケージと証明書ストアを最新化（eMudhra証明書問題への対応）
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    update-ca-certificates && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app/
RUN python manage.py collectstatic --no-input
CMD ["sh", "-c", "gunicorn config.wsgi:application --bind 0.0.0.0:$PORT"]