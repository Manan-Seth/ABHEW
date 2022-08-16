import numpy as np
import streamlit as st
from keras.models import load_model
import app1
import app2
import app4
import app3
import app5
import app7
import app8
PAGES = {
    "PCOS Predictor":app1 ,
    "Breast Cancer Predictor" : app2,
    "Heart Disease Predictor":app3 ,
    "Pre-cancerous lesions predictor ": app4,
    "Malaria Detection":app5 ,
    "Covid19": app7 ,
    "Mask Detection": app8




}
st.sidebar.title('AI Based Healthcare Engine for Women')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
st.sidebar.header('About Me')
st.sidebar.write('Hi! I am Manan Seth - physics undergraduate at IIT Bombay.I developed this app with'
                 'an objective to develop and hone my ML/Ai and computer vision skills while trying to make a '
                 'small contribution to the field of healthcare')

st.sidebar.write("[Azure Health Bot](http://t.me/Help1106_Bot)")