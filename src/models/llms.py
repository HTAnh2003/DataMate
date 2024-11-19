from langchain_openai import ChatOpenAI

def load_llms_model(model_name: str):
    """
    Load the Large Language Model for DataMate
    """
    if "gpt" in model_name:
        return ChatOpenAI(
            model_name=model_name,
            temperature=0.1,
            max_tokens=1000,
        )
    elif "gemini" in model_name:
        pass
    else:
        raise ValueError("Model not supported")