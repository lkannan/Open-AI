from dotenv import load_dotenv
import os
import streamlit as st
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib

matplotlib.use("TkAgg")

load_dotenv()

API_KEY = os.getenv("API_KEY")
openai = OpenAI(API_KEY)

pandas_ai = PandasAI(openai)

st.title("promp driven analysis of incidents")
uploaded_file = st.file_uploader("Upload a csv file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

prompt = st.text_area("Enter a prompt")

if st.button("Submit"):
    if prompt:
        with st.spinner("waiting for openAI response..."):
            st.write(pandas_ai.run(df, prompt))
    else:
        st.warning("Please enter a prompt")
