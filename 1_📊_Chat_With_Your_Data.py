import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv

from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from src.logger.base import BaseLogger
from src.models.llms import load_llms_model
from src.utils import execute_plt_code

# Load the environment variables
load_dotenv()

logger = BaseLogger()
MODEL_NAME = "gpt-3.5-turbo"

def process_query(agent, query):
    response = agent(query)
    response_code = response['intermediate_steps'][-1][0].tool_input['query']

    if "plt" in response_code:
        st.write("### Plotting the data ###")
        st.write(response['output'])
        fig = execute_plt_code(response_code, st.session_state.df)
        if fig is not None:
            st.pyplot(fig)
        st.write("**Executed code:**")
        st.code(response_code)
        str_display = response['output'] + "\n" + f"```python\n{response_code}```"
        st.session_state.history.append({query, str_display})

    else:
        st.write(response['output'])
        st.session_state.history.append({query, response['output']})

def display_chat_history():
    st.write("### Chat History ###")
    for i, (query, response) in enumerate(st.session_state.history):
        st.write(f"**Query {i+1}:** {query}")
        st.write(f"**Response:** {response}")

def main():

    # set up streamlit interface
    st.set_page_config(
        page_title="DataMate - Your Data Analysis Assistant", 
        page_icon="📊", 
        layout="centered", # Options: "centered" or "wide"
        initial_sidebar_state="expanded",  # Options: "collapsed", "expanded"
    )
    st.header("🧠DataMate📊 - Your Data Analysis Assistant")
    st.write("### 🤖Welcome to DataMate! Let's start analyzing your data! ###")

    # Load llms model
    llm = load_llms_model(MODEL_NAME)
    logger.info(f"### Successfully loaded the model: {MODEL_NAME} !###")

    # Upload CSV file
    with st.sidebar:
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    # Initial chat history
    if "history" not in st.session_state:
        st.session_state.history = []

    # Read the CSV file
    if uploaded_file is not None:
        st.session_state.df = pd.read_csv(uploaded_file)
        st.write("### Data Preview ###", st.session_state.df.head())

        # Create data analysis agent to query with our data
        agent = create_pandas_dataframe_agent(
            llm=llm,
            df=st.session_state.df,
            agent_type="tool-calling",
            allow_dangerous_code=True,
            verbose=True,
            return_intermediate_steps=True,
        )
        logger.info("### Successfully loaded data analysis agent! ###")

        # Input query and process the query
        query = st.text_input("Enter your question here:")
        if st.button("Run query"):
            with st.spinner("Processing your question..."):
                process_query(agent, query)

    # Display chat history
    st.divider()
    display_chat_history()

if __name__ == "__main__":
    main()
