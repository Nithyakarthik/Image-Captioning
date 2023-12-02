import requests
import streamlit as st
st.title("Image Description")

API_URL = "https://api-inference.huggingface.co/models/nlpconnect/vit-gpt2-image-captioning"
headers = {"Authorization": "Bearer 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"}

def query(filename):
    data=filename
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

imagelink=st.text_input("Enter Image Link")
button=st.button("SUBMIT")

if button:
    try:
        st.image(imagelink,caption="image uploaded")
        output=query(imagelink)
        st.write(output[0]["generated_text"])
    except:
        st.write("PASS A VAILD IMAGE URL")