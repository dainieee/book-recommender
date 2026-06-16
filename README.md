# 📚 오늘의 책 추천

장르와 키워드를 입력하면 딱 맞는 책을 추천해주는 웹 앱입니다.

## 기술 스택

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Container:** Docker, Docker Compose
- **Deploy:** AWS EC2

## 실행 방법

### Docker Compose로 실행 (권장)

```bash
docker-compose up --build
```

- Streamlit: http://localhost:8501
- FastAPI docs: http://localhost:8000/docs

### 로컬 실행

**백엔드**
```bash
cd back
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

**프론트엔드**
```bash
cd front
pip install -r requirements.txt
streamlit run app.py
```

## 프로젝트 구조

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

## API

`POST /recommend`

```json
{
  "genre": "소설",
  "keywords": "성장, 감동"
}
```

응답:
```json
{
  "genre": "소설",
  "keywords": ["성장", "감동"],
  "recommendations": [...]
}
```