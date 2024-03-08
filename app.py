# Bring in deps
import os 
from apikey import apikey 

import streamlit as st 
from openai import OpenAI

client = OpenAI(api_key=apikey)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 
import streamlit as st
import pandas as pd
from io import StringIO


os.environ['OPENAI_API_KEY'] = apikey
# App framework
st.title('XLS wizard')

# file upload
uploaded_file = st.file_uploader("Choose an Excel file", type=['xls', 'xlsx'])
if uploaded_file is not None:
    # Assuming the uploaded file is an Excel file,
    # use Pandas to read the Excel file.
    df = pd.read_excel(uploaded_file)
    st.write(df)
    response = client.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt=f"Given the following data from an Excel file:\n{df.describe()} Only share the formula. Don't share anything else",
    max_tokens=100
    )
    st.write(response.choices[0].text)



