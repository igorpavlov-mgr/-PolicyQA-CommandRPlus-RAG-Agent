
import os
import requests
from bs4 import BeautifulSoup
import gradio as gr
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage, SystemMessage
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from langchain.callbacks.manager import CallbackManager

# ENV VARS must be set in Hugging Face Space settings for API key and Langfuse
api_key = os.environ.get("COHERE_API_KEY")
langfuse_public_key = os.environ.get("LANGFUSE_PUBLIC_KEY")
langfuse_secret_key = os.environ.get("LANGFUSE_SECRET_KEY")

os.environ["LANGFUSE_PUBLIC_KEY"] = langfuse_public_key
os.environ["LANGFUSE_SECRET_KEY"] = langfuse_secret_key
os.environ["LANGFUSE_HOST"] = "https://cloud.langfuse.com"

# Load policy content from Cohere Docs
def fetch_policy():
    url = "https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        content_div = soup.find("div", class_="markdown") or soup.find("main") or soup
        return content_div.get_text(separator="\n").strip()[:1500]
    except Exception as e:
        return "⚠️ Failed to retrieve policy. " + str(e)

context = fetch_policy()

# Setup Langfuse and LLM
langfuse_callback = CallbackHandler()
llm = ChatCohere(
    cohere_api_key=api_key,
    model="command-r-plus",
    callback_manager=CallbackManager([langfuse_callback]),
    verbose=True,
)
langfuse = Langfuse()

def run_policy_check(query: str):
    trace = langfuse.trace(name="RAG_CommandRPlus_Trace", user_id="huggingface-demo")
    messages = [
        SystemMessage(content=f"This is the policy context from Cohere:\n{context}"),
        HumanMessage(content=query),
    ]
    response = llm.invoke(messages)
    trace.score(name="response_quality", value=1)
    trace.update(status="completed")
    return response.content

# Gradio interface
demo = gr.Interface(
    fn=run_policy_check,
    inputs=gr.Textbox(label="Ask a question about acceptable use of Command R+", lines=3),
    outputs=gr.Textbox(label="Cohere Command R+ Answer"),
    title="Policy QA with Cohere Command R+",
    description="This agent retrieves the Cohere Acceptable Use Policy and answers your ethical use-case questions using LangChain + Command R+.",
)

if __name__ == "__main__":
    demo.launch()
