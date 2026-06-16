from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import random

app = FastAPI()

BOOKS = [
    {"title": "채식주의자", "author": "한강", "genre": "소설", "keywords": ["감성", "인간", "사회", "여성", "한국"], "description": "인간의 욕망과 폭력성을 날카롭게 파헤친 한강의 대표작", "read_hours": 6, "difficulty": "중급"},
    {"title": "82년생 김지영", "author": "조남주", "genre": "소설", "keywords": ["여성", "사회", "한국", "현실", "일상"], "description": "한국 사회 여성의 삶을 섬세하게 담아낸 소설", "read_hours": 4, "difficulty": "초급"},
    {"title": "아몬드", "author": "손원평", "genre": "소설", "keywords": ["감정", "성장", "인간", "청소년", "공감"], "description": "감정을 느끼지 못하는 소년의 성장 이야기", "read_hours": 5, "difficulty": "초급"},
    {"title": "파친코", "author": "이민진", "genre": "소설", "keywords": ["가족", "역사", "한국", "일본", "디아스포라"], "description": "4대에 걸친 재일 한국인 가족의 서사", "read_hours": 20, "difficulty": "중급"},
    {"title": "노르웨이의 숲", "author": "무라카미 하루키", "genre": "소설", "keywords": ["사랑", "청춘", "상실", "감성", "일본"], "description": "청춘의 사랑과 상실을 담은 하루키의 대표작", "read_hours": 8, "difficulty": "중급"},
    {"title": "데미안", "author": "헤르만 헤세", "genre": "소설", "keywords": ["성장", "철학", "자아", "청소년", "고전"], "description": "자아를 찾아가는 한 청년의 내면 여정", "read_hours": 5, "difficulty": "중급"},
    {"title": "아주 작은 습관의 힘", "author": "제임스 클리어", "genre": "자기계발", "keywords": ["습관", "성장", "목표", "생산성", "변화"], "description": "작은 습관이 만들어내는 놀라운 변화", "read_hours": 7, "difficulty": "초급"},
    {"title": "미라클 모닝", "author": "할 엘로드", "genre": "자기계발", "keywords": ["아침", "루틴", "습관", "생산성", "성공"], "description": "아침 루틴으로 삶을 바꾸는 방법", "read_hours": 5, "difficulty": "초급"},
    {"title": "그릿", "author": "앤절라 더크워스", "genre": "자기계발", "keywords": ["노력", "성공", "목표", "끈기", "성장"], "description": "재능보다 중요한 열정과 끈기에 대한 이야기", "read_hours": 8, "difficulty": "중급"},
    {"title": "부의 추월차선", "author": "엠제이 드마코", "genre": "자기계발", "keywords": ["돈", "성공", "부", "경제", "목표"], "description": "빠르게 경제적 자유를 얻는 사고방식", "read_hours": 9, "difficulty": "중급"},
    {"title": "삼체", "author": "류츠신", "genre": "SF", "keywords": ["우주", "외계", "과학", "미래", "물리"], "description": "중국 문화대혁명과 외계 문명의 만남을 그린 SF 대작", "read_hours": 18, "difficulty": "고급"},
    {"title": "파운데이션", "author": "아이작 아시모프", "genre": "SF", "keywords": ["우주", "문명", "미래", "과학", "고전"], "description": "은하 제국의 흥망성쇠를 다룬 SF의 고전", "read_hours": 12, "difficulty": "중급"},
    {"title": "마션", "author": "앤디 위어", "genre": "SF", "keywords": ["우주", "생존", "과학", "화성", "유머"], "description": "화성에 혼자 남겨진 우주인의 생존기", "read_hours": 10, "difficulty": "중급"},
    {"title": "1984", "author": "조지 오웰", "genre": "SF", "keywords": ["디스토피아", "사회", "미래", "자유", "고전"], "description": "전체주의 사회를 경고한 오웰의 디스토피아 소설", "read_hours": 9, "difficulty": "중급"},
    {"title": "해리포터와 마법사의 돌", "author": "J.K. 롤링", "genre": "판타지", "keywords": ["마법", "모험", "우정", "성장", "고전"], "description": "마법사 해리포터의 호그와트 첫 해 이야기", "read_hours": 8, "difficulty": "초급"},
    {"title": "반지의 제왕", "author": "J.R.R. 톨킨", "genre": "판타지", "keywords": ["모험", "마법", "전쟁", "우정", "고전"], "description": "절대반지를 파괴하기 위한 원정대의 여정", "read_hours": 30, "difficulty": "고급"},
    {"title": "나미야 잡화점의 기적", "author": "히가시노 게이고", "genre": "판타지", "keywords": ["감동", "인간", "따뜻함", "시간", "일본"], "description": "시간을 초월한 편지로 이어지는 따뜻한 이야기", "read_hours": 6, "difficulty": "초급"},
    {"title": "언어의 온도", "author": "이기주", "genre": "에세이", "keywords": ["언어", "감성", "위로", "일상", "한국"], "description": "말과 글이 가진 따뜻한 온도에 대한 에세이", "read_hours": 3, "difficulty": "초급"},
    {"title": "죽고 싶지만 떡볶이는 먹고 싶어", "author": "백세희", "genre": "에세이", "keywords": ["감정", "위로", "일상", "우울", "공감"], "description": "우울과 일상 사이를 오가는 솔직한 감정 기록", "read_hours": 4, "difficulty": "초급"},
    {"title": "어떻게 살 것인가", "author": "유시민", "genre": "에세이", "keywords": ["인생", "철학", "삶", "성찰", "한국"], "description": "삶의 방향을 묻는 유시민의 인생 에세이", "read_hours": 6, "difficulty": "중급"},
]

# 기분/상황별 추천 키워드 매핑
MOOD_KEYWORDS = {
    "위로받고 싶어요": ["위로", "감동", "따뜻함", "공감", "감성"],
    "동기부여가 필요해요": ["성공", "성장", "목표", "끈기", "습관", "변화"],
    "그냥 재미있는 거": ["모험", "유머", "마법", "우정", "생존"],
    "깊이 생각하고 싶어요": ["철학", "자아", "사회", "디스토피아", "인간"],
}

# 기분별 추천 멘트
MOOD_MESSAGES = {
    "위로받고 싶어요": "마음이 힘들 때 곁에 두기 좋은 책이에요 🤗",
    "동기부여가 필요해요": "다시 불꽃을 지펴줄 책이에요 🔥",
    "그냥 재미있는 거": "페이지가 술술 넘어가는 책이에요 😄",
    "깊이 생각하고 싶어요": "읽고 나면 세상이 달라 보이는 책이에요 🤔",
}

class RecommendRequest(BaseModel):
    genre: Optional[str] = None
    keywords: Optional[str] = None
    mood: Optional[str] = None

def calculate_score(book, genre, keyword_list):
    score = 0
    if genre and book["genre"] == genre:
        score += 10
    for kw in keyword_list:
        kw = kw.strip()
        if any(kw in bk for bk in book["keywords"]):
            score += 5
        if kw in book["description"]:
            score += 2
        if kw in book["title"]:
            score += 3
    return score

@app.get("/")
def root():
    return {"message": "Book Recommender API is running 📚"}

@app.post("/recommend")
def recommend(request: RecommendRequest):
    genre = request.genre.strip() if request.genre else None
    keyword_list = [kw.strip() for kw in request.keywords.split(",")] if request.keywords else []

    # 기분 키워드 추가
    mood_message = ""
    if request.mood and request.mood in MOOD_KEYWORDS:
        keyword_list += MOOD_KEYWORDS[request.mood]
        mood_message = MOOD_MESSAGES[request.mood]

    scored = []
    for book in BOOKS:
        score = calculate_score(book, genre, keyword_list)
        if score > 0:
            scored.append((score, book))

    scored.sort(key=lambda x: x[0], reverse=True)

    if scored:
        top_score = scored[0][0]
        top_books = [b for s, b in scored if s == top_score]
        random.shuffle(top_books)
        result = top_books[:3]
        if len(result) < 3:
            rest = [b for s, b in scored if s < top_score]
            result += rest[:3 - len(result)]
    else:
        pool = [b for b in BOOKS if b["genre"] == genre] if genre else BOOKS
        result = random.sample(pool, min(3, len(pool)))

    return {
        "genre": genre or "전체",
        "keywords": [kw for kw in (request.keywords.split(",") if request.keywords else [])],
        "mood": request.mood or "",
        "mood_message": mood_message,
        "recommendations": result
    }