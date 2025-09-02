from fastapi import APIRouter
from pydantic import BaseModel
from app.services.rag import answer_question

router = APIRouter()

class Question(BaseModel):
    question: str

@router.post("/")  # prefix /chat와 합쳐서 최종 경로 /chat/
async def chat(q: Question):
    answer = answer_question(q.question)
    return {"answer": answer}
