import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="🎬 기분별 영화 추천", page_icon="🍿", layout="wide")

st.title("🍿 기분별 영화 추천 사이트 🎬")
st.write("✨ 지금 기분에 맞는 영화를 추천해드려요! ✨")

# 기분 선택
mood = st.selectbox(
    "지금 기분을 골라주세요 💖",
    ["😊 행복해!", "😢 슬퍼...", "🤔 생각 많아", "😡 화나!", "😴 그냥 쉬고 싶어"]
)

# 영화 데이터 (제목 + 이미지 URL)
movies = {
    "😊 행복해!": [
        {"title": "인사이드 아웃", "poster": "https://upload.wikimedia.org/wikipedia/ko/6/64/Inside_Out_poster.jpg"},
        {"title": "라라랜드", "poster": "https://upload.wikimedia.org/wikipedia/ko/0/00/La_La_Land.png"},
        {"title": "주토피아", "poster": "https://upload.wikimedia.org/wikipedia/ko/e/e6/Zootopia.jpg"}
    ],
    "😢 슬퍼...": [
        {"title": "너의 이름은", "poster": "https://upload.wikimedia.org/wikipedia/ko/c/c6/Your_Name_poster.jpg"},
        {"title": "미 비포 유", "poster": "https://upload.wikimedia.org/wikipedia/en/7/72/Me_Before_You_%28film%29.jpg"},
        {"title": "월-E", "poster": "https://upload.wikimedia.org/wikipedia/ko/3/3c/WALL-E_poster.jpg"}
    ],
    "🤔 생각 많아": [
        {"title": "인셉션", "poster": "https://upload.wikimedia.org/wikipedia/ko/0/0a/Inception_poster.jpg"},
        {"title": "인터스텔라", "poster": "https://upload.wikimedia.org/wikipedia/ko/b/b4/인터스텔라.jpg"},
        {"title": "이터널 선샤인", "poster": "https://upload.wikimedia.org/wikipedia/en/e/e6/Eternal_Sunshine_of_the_Spotless_Mind.png"}
    ],
    "😡 화나!": [
        {"title": "매드맥스: 분노의 도로", "poster": "https://upload.wikimedia.org/wikipedia/ko/3/3c/Mad_Max_Fury_Road.jpg"},
        {"title": "킬 빌", "poster": "https://upload.wikimedia.org/wikipedia/ko/1/1e/Kill_Bill_Volume_1_poster.jpg"},
        {"title": "조커", "poster": "https://upload.wikimedia.org/wikipedia/ko/4/4f/Joker_2019.jpg"}
    ],
    "😴 그냥 쉬고 싶어": [
        {"title": "센과 치히로의 행방불명", "poster": "https://upload.wikimedia.org/wikipedia/ko/7/7e/Spirited_Away_poster.jpg"},
        {"title": "코코", "poster": "https://upload.wikimedia.org/wikipedia/ko/2/28/Coco_poster.jpg"},
        {"title": "하울의 움직이는 성", "poster": "https://upload.wikimedia.org/wikipedia/ko/a/a0/Howls_Moving_Castle.jpg"}
    ]
}

# 선택한 기분에 맞는 영화 보여주기
st.subheader(f"{mood} 기분일 때 추천 영화 🎥")

cols = st.columns(3)
for idx, movie in enumerate(movies[mood]):
    with cols[idx % 3]:
        st.image(movie["poster"], caption=movie["title"], use_column_width=True)

