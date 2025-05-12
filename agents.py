from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, load_tools
from langchain.agents import AgentType
import streamlit as st
import os
from langchain.tools import WikipediaQueryRun 
from langchain.utilities import WikipediaAPIWrapper


api_key = "AIzaSyBTpk_H6mW6ITjVfByKoVDdo83fY-mQckw"

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key,
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

tools = load_tools(["llm-math", "wikipedia"], llm=llm)


agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

st.set_page_config(page_title="Fresh Agent Demo👾🕵️")
st.header("LangChain with Agents🔎🧮")

input_text = st.text_input("Input:", key="input")
submit = st.button("Generate⚙️")

if submit:
    response = agent_chain.run(input=input_text)
    st.subheader("The Response is")
    st.write(response)
