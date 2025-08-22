import streamlit as st
import random

# -----------------------------
# 영화 데이터 (기분별 추천)
# -----------------------------
movies = {
    "😊 기쁠 때": [
        {"title": "라라랜드 🎶✨", 
         "desc": "반짝이는 음악과 달콤한 사랑 이야기 💛 기분이 더 업업↗️",
         "poster": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land.png",
         "trailer": "https://www.youtube.com/watch?v=0pdqf4P9MB8"},
        {"title": "인턴 👔💼", 
         "desc": "따뜻하고 긍정적인 분위기로 마음이 포근해져요 ☕🌸",
         "poster": "https://upload.wikimedia.org/wikipedia/en/c/c9/The_Intern_Poster.jpg",
         "trailer": "https://www.youtube.com/watch?v=ZU3Xban0Y6A"},
    ],
    "😢 슬플 때": [
        {"title": "인사이드 아웃 🌈😭", 
         "desc": "눈물 나지만 따뜻한 감동 🍭 감정을 이해할 수 있어요 💕",
         "poster": "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
         "trailer": "https://www.youtube.com/watch?v=seMwpP0yeu4"},
        {"title": "세상의 모든 계절 🍂👨‍👩‍👧", 
         "desc": "인생의 희노애락을 담은 감동적인 가족 이야기 💌",
         "poster": "https://upload.wikimedia.org/wikipedia/en/f/f5/Another_Year.jpg",
         "trailer": "https://www.youtube.com/watch?v=yYbV5pFzLrE"},
    ],
    "😡 화날 때": [
        {"title": "분노의 질주 🚗💨🔥", 
         "desc": "시원한 액션으로 스트레스 팡팡! 💥",
         "poster": "https://upload.wikimedia.org/wikipedia/en/7/7e/Fast_%26_Furious_Poster.jpg",
         "trailer": "https://www.youtube.com/watch?v=2TAOizOnNPo"},
        {"title": "킬 빌 ⚔️🖤", 
         "desc": "강렬한 액션으로 화난 마음을 날려버리세요! 💣",
         "poster": "https://upload.wikimedia.org/wikipedia/en/c/cf/Kill_Bill_Volume_1.png",
         "trailer": "https://www.youtube.com/watch?v=7kSuas6mRpk"},
    ],
    "😴 지칠 때": [
        {"title": "월터의 상상은 현실이 된다 🌍✨", 
         "desc": "모험과 여행으로 지친 마음에 힐링을 💫🍀",
         "poster": "https://upload.wikimedia.org/wikipedia/en/e/e4/The_Secret_Life_of_Walter_Mitty_poster.jpg",
         "trailer": "https://www.youtube.com/watch?v=QD6cy4PBQPI"},
        {"title": "먹고 기도하고 사랑하라 🍝🧘‍♀️💖", 
         "desc": "여행과 자기 치유, 마음의 힐링 타임 🎀",
         "poster": "https://upload.wikimedia.org/wikipedia/en/7/7f/Eat_pray_love_ver2.jpg",
         "trailer": "https://www.youtube.com/watch?v=mjay5vgIwt4"},
    ],
    "💘 사랑하고 싶을 때": [
        {"title": "노트북 📖💞", 
         "desc": "달달한 사랑 이야기에 푹 빠져보세요 💋",
         "poster": "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg",
         "trailer": "https://www.youtube.com/watch?v=FC6biTjEyZw"},
        {"title": "어바웃 타임 ⏰❤️", 
         "desc": "시간여행 + 로맨스 = 완벽 조합 🥰",
         "poster": "https://upload.wikimedia.org/wikipedia/en/8/85/About_Time_poster.jpg",
         "trailer": "https://www.youtube.com/watch?v=T7A810duHvw"},
    ],
}

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="기분별 영화 추천 🎬🍿", page_icon="🍿", layout="wide")

st.markdown("<h1 style='text-align: center;'>✨ 오늘 내 기분에 맞는 영화는? ✨</h1>", unsafe_allow_html=True)
st.write("👉 지금 기분을 선택하면 그에 맞는 영화를 랜덤으로 추천해드려요 🎁")

# 푸린 이미지 (상단에 귀엽게 배치 💖)
st.image("https://archives.bulbagarden.net/media/upload/thumb/f/fb/039Jigglypuff.png/250px-039Jigglypuff.png", 
         caption="귀여운 푸린이랑 함께하는 영화 추천 🍬🎤", width=180)

# 기분 선택
mood = st.radio("🌈 지금 내 기분은...?", list(movies.keys()))

if mood:
    choice = random.choice(movies[mood])  # 랜덤 영화 추천
    
    st.markdown(f"### 🎉 오늘의 추천 영화는... **{choice['title']}** 🎉")
    st.image(choice["poster"], width=250)
    st.write(f"💡 {choice['desc']}")
    st.video(choice["trailer"])
    st.success("🍀 즐거운 영화 감상 되세요! 🍀")
