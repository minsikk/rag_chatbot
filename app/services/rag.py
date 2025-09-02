import os

# 예시 문서 로드
doc_path = "data/knowledge_base/example.txt"
if os.path.exists(doc_path):
    with open(doc_path, "r", encoding="utf-8") as f:
        DOCUMENT_TEXT = f.read()
else:
    DOCUMENT_TEXT = ""

def answer_question(question: str) -> str:
    """부분 매칭 검색 + 대소문자 무시"""
    if not question.strip():
        return "질문을 입력해주세요."

    question_lower = question.lower()
    doc_lower = DOCUMENT_TEXT.lower()

    if any(word in doc_lower for word in question_lower.split()):
        return f"문서에서 찾은 답변: {DOCUMENT_TEXT[:150]}..."
    else:
        return f"문서에서 관련 내용을 찾을 수 없습니다. 질문: '{question}'"
