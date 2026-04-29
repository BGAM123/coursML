# mettre du text dans le streamlit
import streamlit as st
st.title('Web application')
#mettre un header
st.header('Streamlit app')
st.subheader('Streamlit web app')
st.text('Good streamlit app')
st.write('ML app')

#Caractere speciaux gras et italique
st.markdown('** hello word***')
st.markdown('https://www.bing.com/search?pglt=299&q=institut+francais+cameroun&cvid=aeba19b77c144bfe874b1706ebd360aa&gs_lcrp=EgRlZGdlKgYIABBFGDkyBggAEEUYOTIGCAEQABhA0gEJMTM0MzNqMGo3qAIIsAIB&FORM=ANSPA1&PC=U531')

#Indicateurs
st.metric(label='Wind speed', value='120ms', delta='+1.4ms=1')
st.image('onepiece.png', caption='This is an image', width=600)
st.video('Naruto Shippuden  Ending 6  Broken youth.mp4')
st.audio('Damiano David  Born With a Broken Heart (Official Video).mp3')

#selecteurs

state = st.checkbox('Checkbox', value=True)
if state:
    st.write('Your checkbox the box')
else:
    pass

radio_btn = st.radio('Radio Button ',('US','UK','Canada'))

btn = st.button('Click Me')
select = st.selectbox('select box', ('Audi','BWN','Ferrari'))
multi_select = st.multiselect('quel est ton nom : ', ('afana','miguel','pipus','biango'))

#Import de document
#Iploader une image
image = st.file_uploader('***Upload an image***', type=['png','jpeg'])
if image:
    st.image(image)

#Upload d'une video
video = st.file_uploader('***Upload a video***', type=['avi','mp3'])
if video:
    st.video(video)

#slider
st.slider('***this is a slider***', min_value=50, max_value=100, value=70)

st.text_input('Entrer your course title')