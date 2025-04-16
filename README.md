
# Policy Q&A RAG Agent Powered by Command R+

This project implements a lightweight Retrieval-Augmented Generation (RAG) agent designed to answer ethical and acceptable use questions using Cohere's [Command R+](https://cohere.com/products/command-r) model.

The agent retrieves and parses the live [Cohere Acceptable Use Policy](https://docs.cohere.com/docs/cohere-labs-acceptable-use-policy), and uses LangChain + Command R+ to answer user questions with context grounding. The app also includes full observability via Langfuse for traceability, scoring, and token-level insight.

# Features

- **Live policy retrieval** from Cohere documentation
- **Command R+** powered inference using LangChain
- **System message context injection** for grounding
- **Gradio UI** for user interaction
- **Langfuse tracing** with full input/output telemetry

# How to Run on Hugging Face Spaces

1. Clone or upload this repo to a new Hugging Face Space (Gradio SDK)
2. Create the following **Environment Variables** under "Settings":
   - 'COHERE_API_KEY'
   - 'LANGFUSE_PUBLIC_KEY'
   - 'LANGFUSE_SECRET_KEY'
3. Add this to your 'requirements.txt':

'''
gradio
cohere
langchain
langchain-cohere
langfuse
beautifulsoup4
requests
'''

4. The app will run automatically via 'app.py'

# Example Use Case

**Question:**  
_Is it acceptable to use Command R+ to simulate public figures in political satire?_

**Response:**  
Command R+ responds with a detailed explanation of ethical boundaries, policy restrictions, legal responsibility, and transparency — grounded in the live Cohere Acceptable Use Policy.

# Observability

All interactions are logged in [Langfuse](https://cloud.langfuse.com), including:
- Trace name
- Role-based message breakdown
- Token usage
- Output quality scoring

# Tech Stack

- [LangChain](https://www.langchain.com/)
- [Cohere Command R+](https://cohere.com/)
- [Langfuse](https://langfuse.com/)
- [Gradio](https://gradio.app/)

# Author

Built by Igor Pavlov as a showcase of RAG, Cohere Command R+ LLM, model observability, ethical AI use.

# License

MIT License — for educational and demonstration purposes.

# Live Demo
Try it out on [Hugging Face Spaces](https://huggingface.co/spaces/igorpavlov-mgr/PolicyQA-CommandRPlus-RAG-Agent)
