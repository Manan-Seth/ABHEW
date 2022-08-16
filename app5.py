import streamlit as st
from tensorflow.keras.models import load_model
from files_upload import FilesUpload

def app():

    st.title("Malaria Detector Wep App")
    files_upload = FilesUpload()
    img = files_upload.run()
    if st.button("Predict"):
        st.text('Wait...Model is being loaded!')
        model = load_model('malaria_detector.h5')
        st.success("Model Loaded")

        if model.predict(img)[0][0] > 0.5:
            st.text("Uninfected")

        else:
            st.text("If irrelevent image is uploaded then model will assume it is infected")
            st.text("Infected/Parasitized")
