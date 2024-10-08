import streamlit as st
import random

st.title(':sparkles: 로또 생성기 :sparkles:')
st.subheader('로또를 생성해 주세요!')

button = st.button('로또를 생성해 주세요!')

if button:
    lotto_numbers = [sorted(random.sample(range(1, 46), 6)) for _ in range(5)]
    
    st.write(f'''
행운의 번호:
 :green[{lotto_numbers[0]}]\n
행운의 번호:
 :green[{lotto_numbers[1]}]\n
행운의 번호:
 :green[{lotto_numbers[2]}]\n
행운의 번호:
 :green[{lotto_numbers[3]}]\n
행운의 번호:
 :green[{lotto_numbers[4]}]''')

