import streamlit as st
import datetime
import pandas as pd
import numpy as np

# 타이틀
st.title("Streamlit 자동 배포 테스트")

# 문자열 입력
name = st.text_input("이름을 입력하세요")

age=st.number_input("나이를 입력하세요" ,min_value=0,max_value=100)

gender = st.radio("성별을 입력하세요",["남","여"])
if st.button("확인"):
    st.success(f"{name}님 반가워요! 당신의 나이는 {age}세 성별은 {gender}입니다.")

# 이미지
st.image("./img/1.jpg",caption="로고이미지")

# 비디오
st.video("./img/2.mp4")


dob=st.date_input("생년월일 선택",datetime.date(2000,1,1))


agree =st.checkbox("약관에 동의합니다.")
subject=st.selectbox("좋아하는 과목",["파이썬","자바"])

upload_file=st.file_uploader("파일을 업로드 하세요",type=["txt","csv"])

if upload_file:
    st.text("업로드된 파일 내용:")
    st.text(upload_file.read().decode("utf-8"))


data=pd.DataFrame(np.random.randn(10,2),columns=["A","B"])

st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)


col1, col2= st.columns(2)

col1.write("왼쪽 컬럼입니다.")
col2.write("오른쪽 컬럼입니다.")


tab1, tab2 = st.tabs(["tab1","tab2"])

with tab1:
    st.write("첫번째 탭 입니다.")
with tab2:
    st.write("두번째 탭 입니다.")

with st.sidebar:
    st.write("여기는 사이드 바입니다.")
    st.selectbox("옵션 선택",["A","B","C"])