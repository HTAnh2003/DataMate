import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import streamlit as st

def execute_plt_code(code: str, df: pd.DataFrame):
    try:
        code = code.strip('```python\n').strip('```')
        local_vars = {
            "plt": plt,
            "df": df,
            "sns": sns,
        }
        print("_____code______")
        print(code)
        print("___________")
        compiled_code = compile(code, "<string>", "exec")
        exec(compiled_code, globals(), local_vars)

        return plt.gcf()
    
    except Exception as e:
        st.error(f"Error executing code: {e}")
        return None