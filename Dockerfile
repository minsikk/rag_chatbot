# 베이스 이미지
FROM python:3.11-slim

# 작업 디렉토리 생성
WORKDIR /app

# 필요한 패키지 복사 후 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 전체 코드 복사
COPY . .

# FastAPI 포트 노출
EXPOSE 8000

# 컨테이너 실행 명령
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
