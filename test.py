import streamlit as st

st.set_page_config(page_title="🎬 기분별 영화 추천", page_icon="🎥", layout="centered")

st.title("🎬 오늘의 기분별 영화 추천 🍿")

# 기분 선택
mood = st.selectbox(
    "오늘 기분은 어때? 😆😢😡😴😍😎",
    ["행복해 😆", "슬퍼 😢", "화나 😡", "피곤해 😴", "설레 😍", "차분해 😎"]
)

# 기분별 영화 데이터
movies = {
    "행복해 😆": [
        {"title": "인사이드 아웃", "poster": "https://upload.wikimedia.org/wikipedia/ko/0/05/Inside_Out_%28Korean_poster%29.jpg"},
        {"title": "라라랜드", "poster": "https://upload.wikimedia.org/wikipedia/ko/f/fd/La_La_Land.png"},
    ],
    "슬퍼 😢": [
        {"title": "빌리 엘리어트", "poster": "https://upload.wikimedia.org/wikipedia/ko/5/5e/Billy_Elliot_poster.jpg"},
        {"title": "마더", "poster": "https://upload.wikimedia.org/wikipedia/ko/1/1e/Mother_2009.jpg"},
    ],
    "화나 😡": [
        {"title": "조커", "poster": "https://upload.wikimedia.org/wikipedia/ko/e/e5/Joker_%28film%29_poster.jpg"},
        {"title": "매드맥스: 분노의 도로", "poster": "https://upload.wikimedia.org/wikipedia/ko/0/09/Mad_Max_Fury_Road_poster.jpg"},
    ],
    "피곤해 😴": [
        {"title": "월-E", "poster": "https://upload.wikimedia.org/wikipedia/ko/c/c1/WALL-E_poster.jpg"},
        {"title": "코코", "poster": "https://upload.wikimedia.org/wikipedia/ko/8/88/Coco_%282017%29.jpg"},
    ],
    "설레 😍": [
        {"title": "어바웃 타임", "poster": "https://upload.wikimedia.org/wikipedia/ko/3/3c/About_Time_poster.jpg"},
        {"title": "노팅 힐", "poster": "https://upload.wikimedia.org/wikipedia/ko/3/38/Notting_Hill_poster.jpg"},
    ],
    "차분해 😎": [
        {"title": "인터스텔라", "poster": "https://upload.wikimedia.org/wikipedia/ko/b/bd/인터스텔라_포스터.jpg"},
        {"title": "비포 선라이즈", "poster": "https://upload.wikimedia.org/wikipedia/ko/2/2c/Before_Sunrise.jpg"},
    ]
}

# 선택한 기분에 맞는 영화 추천
st.subheader(f"{mood} 기분엔 이런 영화 어때? 🎥")

for movie in movies[mood]:
    st.image(movie["poster"], caption=movie["title"], width=250)


