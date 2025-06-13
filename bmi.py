import streamlit as st 
st.set_page_config(layout='wide')
st.header('''
BMI CALCULATOR
''')
st.subheader('This app calculate your boby mass index (bmi)')
weigh=st.number_input('Enter your weight(kg)')
heigh=st.number_input('Enter your height(m)')
def bmi(weight,height):
   try:
     bm = weight / (height) ** 2
   except Exception:
      st.warning("can't divide by zero")
      return None
   if bm < 18.5:
      st.warning('Underweight')
   elif bm >= 18.5 and bm < 24.9:
      st.success('Normal')
   elif bm >= 25 and bm < 29.9:
      st.warning('Overweight')
   else:
      st.error('Obese')
   return bm
if (st.button('calculate')):
   cal=bmi(weigh,heigh)
   st.write(cal)