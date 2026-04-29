import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import time
db = pd.read_csv('bank.csv')
st.set_page_config(page_title='Real Time', page_icon='✅', layout='wide')

#Dashboard title
st.title('Real Time Analytics')
#filtre sur job
job_filter = st.selectbox('Select a job',pd.unique(db['job']))
db = db[db['job']== job_filter]

#Creation d' indication
avg_age = np.mean(db['age'])
count_married = int(db[(db['marital']== 'married')]['marital'].count())
balance = np.mean(db['balance'])

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(label= 'Age🪦', value=round(avg_age), delta=round(avg_age))
kpi2.metric(label= 'Married Count 👙', value=count_married, delta=round(count_married))
kpi3.metric(label= 'Balance ⚖️', value= f"${round(balance,2)}", delta=round(balance/count_married)*100 )


#Graphique
col1, col2= st.columns(2)
with col1:
    st.markdown('###First Chart')
    fig1=plt.figure()
    sns.barplot(data=db, y='age', x='marital', palette='muted')
    st.pyplot(fig1)

with col1:
    st.markdown('###Second Chart')
    fig2=plt.figure()
    sns.histplot(data=db, x='age', )
    st.pyplot(fig2)

st.markdown('### Detailed Data View')
st.dataframe(db)
time.sleep(1)