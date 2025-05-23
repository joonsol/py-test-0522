import streamlit as st

# 타이틀
st.title("Streamlit 자동 배포 테스트")

# 문자열 입력
name = st.text_input("이름을 입력하세요")

age=st.number_input("나이를 입력하세요" ,min_value=0,max_value=100)

if st.button("확인"):
    st.success(f"{name}님 반가워요! 당신의 나이는 {age}세입니다.")




