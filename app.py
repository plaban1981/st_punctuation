import streamlit as st
from PIL import Image
import requests
import pandas as pd
import os
import json
#
image_path = "image.jpg"
image = Image.open(image_path)

st.set_page_config(page_title="Punctuation Correction App", layout="centered")
st.image(image, caption='Punctuation Correction')
#
# page header
st.title(f"Punctuation Correction App")
with st.form("Punctuation Correction"):
   text1 = st.text_input("Enter text here")
   submit = st.form_submit_button("Correction")
   #
   if submit:    
        print(text1)
        #
        with open("input.txt", "wb") as f:
            f.write(text1.encode("utf-8"))
        os.chmod("input.txt", 0o777)
        # Keyword Extraction API
        url = "https://app.aimarketplace.co/api/marketplace/models/punctuation-corrector-8e21ca7b/predict/"
        payload={'data': open('input.txt','rb')}
        headers = {'Authorization': 'Api-Key HPjMlYo1.gMkJ0iXTzsGSvmVFS6oUNT86BPR4S99h','Cache-Control': 'no-cache'}

        response = requests.request("POST", url, headers=headers, files=payload)
        #
        print(response.text)
        # output header
        st.header("Corrected Text")
        # output results
        st.success(response.text.split('response')[1].split("Corrected Text")[1].replace("}","").replace(']',"").replace('"',"").replace('\\','').replace('"','').replace(":",""))