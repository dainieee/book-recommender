import streamlit as st
import requests
import os

FASTAPI_URL = os.getenv("FASTAPI_URL", "http://localhost:8000")

st.set_page_config(
    page_title="📚 오늘의 책 추천",
    page_icon="📚",
    layout="centered"
)

st.title("📚 오늘의 책 추천")
st.markdown("장르, 기분, 키워드를 입력하면 지금 당신에게 딱 맞는 책을 추천해드려요!")
st.divider()

# 입력 섹션
col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox(
        "📖 장르 선택",
        options=["선택 안 함", "소설", "자기계발", "SF", "판타지", "에세이"],
        index=0
    )

with col2:
    mood = st.selectbox(
        "💭 지금 기분이 어때요?",
        options=["선택 안 함", "위로받고 싶어요", "동기부여가 필요해요", "그냥 재미있는 거", "깊이 생각하고 싶어요"],
        index=0
    )

keywords = st.text_input(
    "🔍 키워드 직접 입력 (쉼표로 구분, 선택사항)",
    placeholder="예: 성장, 감동, 우정"
)

st.markdown("")

if st.button("책 추천받기 ✨", type="primary", use_container_width=True):
    selected_genre = None if genre == "선택 안 함" else genre
    selected_mood = None if mood == "선택 안 함" else mood
    selected_keywords = keywords.strip() if keywords.strip() else None

    if not selected_genre and not selected_mood and not selected_keywords:
        st.warning("장르, 기분, 키워드 중 하나 이상 선택해주세요!")
    else:
        with st.spinner("딱 맞는 책을 찾는 중..."):
            try:
                response = requests.post(
                    f"{FASTAPI_URL}/recommend",
                    json={
                        "genre": selected_genre,
                        "keywords": selected_keywords,
                        "mood": selected_mood
                    },
                    timeout=10
                )
                response.raise_for_status()
                data = response.json()

                st.divider()

                # 기분 멘트 표시
                if data.get("mood_message"):
                    st.info(f"**{data['mood_message']}**")

                st.subheader("추천 결과")

                books = data.get("recommendations", [])
                if books:
                    for i, book in enumerate(books, 1):
                        with st.container(border=True):
                            col_a, col_b = st.columns([3, 1])
                            with col_a:
                                st.markdown(f"### {i}. {book['title']}")
                                st.markdown(f"**저자:** {book['author']}  |  **장르:** {book['genre']}")
                                st.markdown(f"**키워드:** {' · '.join(book['keywords'])}")
                                st.markdown(f"{book['description']}")
                            with col_b:
                                st.markdown(f"⏱️ **예상 독서 시간**")
                                st.markdown(f"### {book['read_hours']}시간")
                                difficulty_color = {"초급": "🟢", "중급": "🟡", "고급": "🔴"}
                                st.markdown(f"{difficulty_color.get(book['difficulty'], '⚪')} {book['difficulty']}")
                else:
                    st.info("조건에 맞는 책을 찾지 못했어요. 다른 조건을 입력해보세요!")

            except requests.exceptions.ConnectionError:
                st.error("서버에 연결할 수 없어요. FastAPI 서버가 실행 중인지 확인해주세요.")
            except requests.exceptions.Timeout:
                st.error("요청 시간이 초과됐어요. 다시 시도해주세요.")
            except Exception as e:
                st.error(f"오류가 발생했어요: {str(e)}")

st.divider()
st.caption("📖 Book Recommender · Powered by FastAPI + Streamlit")