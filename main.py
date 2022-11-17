import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
       latest_interation.text(f'Iteration{i+1}')
       bar.progress(i+1)
       time.sleep(0.1)

'Done!!'

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')

expander.write('問い合わせ内容')

text = st.text_input('あなたの趣味を教えて下さい')
condistion = st.slider('あなたの調子は？',0,100,50)

st.write('あなたの趣味：',text)
st.write('コンディション：',condistion)



option = st.selectbox(
   'あなたが好きな数字を教えてください',
   list(range(1,11))
   )

st.write('あなたの好きな数字は、',option,'です')


