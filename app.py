# Bring in deps
import os 
from apikey import apikey 

import streamlit as st 
import openai
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 
import streamlit as st
import pandas as pd
from io import StringIO


os.environ['OPENAI_API_KEY'] = apikey
openai.api_key = apikey
# App framework
st.title('BISA YOUTUBE')
# file upload
uploaded_file = st.file_uploader("Choose an Excel file", type=['xls', 'xlsx'])
if uploaded_file is not None:
    # Assuming the uploaded file is an Excel file,
    # use Pandas to read the Excel file.
    df = pd.read_excel(uploaded_file)
    st.write(df)

# prompt input
prompt = st.text_input('Plug in your prompt here') 


response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  temperature=0.7,
  max_tokens=100,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


st.write(response.choices[0].text)