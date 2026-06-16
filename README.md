# 📚 오늘의 책 추천
> 장르 · 기분 · 키워드 기반 개인 맞춤 책 추천 웹 애플리케이션

## 프로젝트 소개

사용자가 원하는 장르, 현재 기분, 관심 키워드를 입력하면
FastAPI 백엔드가 점수 기반 매칭 알고리즘으로 최적의 책 3권을 추천합니다.
추천 결과에는 책 정보와 함께 예상 독서 시간 및 난이도가 함께 제공됩니다.

## 주요 기능

- 장르 선택: 소설 / 자기계발 / SF / 판타지 / 에세이
- 기분 선택: 위로받고 싶어요 / 동기부여가 필요해요 / 재미있는 거 / 깊이 생각하고 싶어요
- 키워드 직접 입력 (쉼표로 구분, 복수 입력 가능)
- 추천 결과: 도서명 · 저자 · 설명 · 예상 독서 시간 · 난이도 표시

## 시스템 구조

```
book-recommender/
├── front/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── back/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
├── docker-compose.yml
└── .gitignore
```

## 실행 방법

```bash
docker-compose up --build
```

- Streamlit: http://localhost:8501
- FastAPI docs: http://localhost:8000/docs
