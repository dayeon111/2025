import streamlit as st

# MBTI별 직업 추천 데이터
job_recommendations = {
    "INTJ": ["전략가", "과학자", "엔지니어", "기획자"],
    "ENTP": ["기업가", "방송인", "마케팅 전문가", "기획자"],
    "INFJ": ["상담가", "작가", "교사", "심리학자"],
    "ESFP": ["배우", "가수", "운동선수", "서비스직"],
    "ISTJ": ["회계사", "관리자", "공무원", "엔지니어"],
    "ENFP": ["크리에이터", "광고 기획자", "강사", "작가"],
    # 필요하면 더 추가!
}

# 웹앱 제목
st.title("MBTI 기반 직업 추천 웹앱")

# 설명
st.write("당신의 MBTI를 선택하면 어울리는 직업을 추천해드립니다!")

# MBTI 선택
mbti = st.selectbox("MBTI 유형을 선택하세요:", list(job_recommendations.keys()))

# 결과 출력
if mbti:
    st.subheader(f"✅ {mbti} 유형에 어울리는 직업 추천")
    recommendations = job_recommendations[mbti]
    for job in recommendations:
        st.write(f"- {job}")

