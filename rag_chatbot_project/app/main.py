from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.routers import chat

app = FastAPI(title="RAG Chatbot")

# 1️⃣ 라우터 먼저 등록
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# 2️⃣ StaticFiles 나중에 등록
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 실제 배포 시 도메인 제한 가능
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "RAG 챗봇 서버 실행 중"}
