import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="기분별 영화 추천 🎬💖",
    page_icon="🍿",
    layout="centered"
)

# 제목
st.title("🎀 오늘의 기분에 맞는 영화 추천 🎀")
st.markdown("좋은 기분으로 영화 한 편 어떠세요? 🐰✨")

# 기분 선택
mood = st.radio(
    "오늘 당신의 기분은 어떤가요? 😺",
    ('행복해요 😄', '우울해요 😢', '긴장돼요 😰', '편안해요 😌', '신나요 🥳')
)

# 영화 추천 데이터
movies = {
    '행복해요 😄': [
        "라라랜드 (La La Land) 🎶",
        "월터의 상상은 현실이 된다 (The Secret Life of Walter Mitty) 🌈",
        "인사이드 아웃 (Inside Out) 🎨",
        "미녀와 야수 (Beauty and the Beast) 🏰"
    ],
    '우울해요 😢': [
        "어바웃 타임 (About Time) ⏳",
        "노트북 (The Notebook) 💌",
        "굿바이 크리스토퍼 로빈 (Goodbye Christopher Robin) 🐻",
        "이터널 선샤인 (Eternal Sunshine of the Spotless Mind) 💭"
    ],
    '긴장돼요 😰': [
        "인셉션 (Inception) 🌀",
        "셜록 홈즈 (Sherlock Holmes) 🕵️‍♂️",
        "히든 피겨스 (Hidden Figures) 🔍",
        "소셜 네트워크 (The Social Network) 💻"
    ],
    '편안해요 😌': [
        "하울의 움직이는 성 (Howl's Moving Castle) 🏡",
        "센과 치히로의 행방불명 (Spirited Away) 🍵",
        "모아나 (Moana) 🌊",
        "토이 스토리 (Toy Story) 🧸"
    ],
    '신나요 🥳': [
        "슈퍼배드 (Despicable Me) 😈",
        "라라랜드 (La La Land) 💃",
        "킹스맨 (Kingsman) 🎩",
        "스파이더맨: 노 웨이 홈 (Spider-Man: No Way Home) 🕷️"
    ]
}

# 추천 영화 표시
st.markdown("### 🎬 추천 영화 리스트")
for movie in movies[mood]:
    st.write(f"- {movie}")

# 귀여운 마무리
st.markdown("💖 오늘 기분에 맞는 영화와 함께 행복한 시간 보내세요! 🐱🍿")

