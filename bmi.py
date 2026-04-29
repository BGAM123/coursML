import streamlit as st
st.title('welcome to BMI calculetor')

weight = st.number_input('Enter your weight in kgs')
statut = st.radio('Select your height format:',('cms','meters','feet'))

try:
    if statut == 'cms':
        height = st.number_input('cms')
        bmi = weight/((height/100)**2)

    elif statut == 'meters':
        height = st.number_input('meters')
        bmi = weight/((height)**2)

    else:
        height = st.number_input('feet')
        bmi = weight/((height/3.28)**2)
except:
    print('zero ne divise aucun nombre')

if(st.button('Calculate BMI')):
    st.write('your bmi is : {}'.format(round(bmi)))

    if bmi < 16:
        st.error('you are extremely underweight')
    elif(bmi >= 16 and bmi< 18.5):
        st.warning('you are healthy')
    elif(bmi >= 18.5 and bmi < 25):
        st.warning('you are healthy')
    elif(bmi >= 25 and bmi < 30):
        st.warning('you are overweight')
    elif(bmi >= 30 and bmi < 35):
        st.warning('you are obese')
    else:
        st.error('you are extremely obese')
    