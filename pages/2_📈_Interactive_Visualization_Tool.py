import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd

def main():
    st.set_page_config(
        page_title="Interactive Visualization Tool", 
        page_icon="📈" ,
        layout="wide", # Options: "centered" or "wide"
        # initial_sidebar_state="collapsed",  # Options: "collapsed", "expanded"
    )

    st.header("📈 Interactive Visualization Tool")
    st.write("### 🤖Welcome to the Interactive Visualization Tool! Let's start visualizing your data! ###")

    with st.sidebar:
        # Move the file uploader to the top
        uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

        if uploaded_file is not None:
            st.session_state.df = pd.read_csv(uploaded_file)
            st.write("### Data Preview ###")
            st.write(st.session_state.df.head())
        elif "df" in st.session_state:
            st.write("### Data Preview ###")
            st.write(st.session_state.df.head())
        else:
            st.write("No data uploaded yet. Please upload a CSV file.")


    # Render the interactive visualization tool
    if st.session_state.get("df") is not None:
        renderer = StreamlitRenderer(st.session_state.df)
        renderer.explorer()
    else:
        st.info("Please upload a CSV file to start visualizing your data!")

if __name__ == "__main__":
    main()
