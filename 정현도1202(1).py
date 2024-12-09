import streamlit as st

st.title('st.form')
#'with' 표기법을 사용한 전체 예시
st.header('1. with 표기법 사용 예시')
st.subheader('팝콘 키오스크')
with st.form('my_form'):
    st.subheader('** 팝콘 주문하기**')
    #입력 위젯
    pop_val = st.selectbox('맛',['오리지널', '더블치즈', '카라멜', '바질어니언'])
    popsize_val = st.selectbox('팝콘 사이즈', ['M', 'L'])
    drink_val = st.selectbox('음료수', ['콜라','사이다','환타'])
    drinksize_val = st.selectbox('음료수 사이즈', ['M', 'L'])
    submitted = st.form_submit_button('제출')#모든 양식은 제출 버튼을 가져야 함

if submitted:
    st.markdown(f'''
                주문하신 내용:
            - 팝콘: '{pop_val}'
            - 팝콘 사이즈: '{popsize_val}'
            - 음료수: '{drink_val}'
            - 음료수 사이즈: '{drinksize_val}'
            ''')
else:
    st.write('주문하세요!')
