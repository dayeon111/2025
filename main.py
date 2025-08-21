import streamlit as st

# 🎨 이모지와 컬러풀한 제목
st.markdown(
    """
    <h1 style="text-align: center; color: #FF66B2;">
        🌟✨ MBTI 직업 추천 매직 사이트 ✨🌟
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")
st.write("😎 **당신의 성격 유형(MBTI)에 따라 찰떡같이 어울리는 직업을 추천해드립니다!** 🎯")

# 📌 MBTI별 직업 추천 데이터
job_recommendations = {
    "INTJ": {
        "emoji": "🧠🔮",
        "desc": "전략적이고 분석적인 천재형! 🚀",
        "jobs": ["전략가 📝", "과학자 🔬", "엔지니어 ⚙️", "기획자 📊"]
    },
    "ENTP": {
        "emoji": "⚡🎤",
        "desc": "아이디어 뱅크, 토론의 제왕! 💡",
        "jobs": ["기업가 💼", "방송인 📺", "마케팅 전문가 📢", "기획자 🎬"]
    },
    "INFJ": {
        "emoji": "🌸📖",
        "desc": "이상주의적인 조언자, 사람들의 멘토 🌱",
        "jobs": ["상담가 💬", "작가 ✍️", "교사 👩‍🏫", "심리학자 🧩"]
    },
    "ESFP": {
        "emoji": "🎶🎉",
        "desc": "무대 위의 슈퍼스타, 인생을 즐기는 자유인 🌈",
        "jobs": ["배우 🎭", "가수 🎤", "운동선수 🏅", "서비스직 🍹"]
    },
    "ISTJ": {
        "emoji": "📚🛠️",
        "desc": "신뢰와 원칙을 중시하는 철저한 관리자 🔒",
        "jobs": ["회계사 💵", "관리자 🗂️", "공무원 🏛️", "엔지니어 🔧"]
    },
    "ENFP": {
        "emoji": "🌈🔥",
        "desc": "열정 가득한 크리에이터, 세상을 빛내는 불꽃 ✨",
        "jobs": ["크리에이터 🎨", "광고 기획자 📸", "강사 🎤", "작가 📚"]
    },
}

# 🎯 MBTI 선택 박스
mbti = st.selectbox("👉 당신의 MBTI를 골라주세요! 👇", list(job_recommendations.keys()))

# 결과 출력
if mbti:
    st.markdown("---")
    st.subheader(f"{job_recommendations[mbti]['emoji']} {mbti} 유형 직업 추천 {job_recommendations[mbti]['emoji']}")
    st.write(f"💡 **{job_recommendations[mbti]['desc']}**")
    
    st.write("🌟 어울리는 직업 리스트 🌟")
    for job in job_recommendations[mbti]["jobs"]:
        st.markdown(f"- {job}")
    
    st.balloons()  # 🎈 풍선 이펙트
