import streamlit as st
from main import ingest_url
from agent import agent

st.set_page_config(page_title="Financial AI Agent", layout="wide")

st.title("Financial News AI Agent")

# =========================
# URL INPUT
# =========================
url = st.text_input(
    "Enter Article URL")

# =========================
# LOAD ARTICLE
# =========================
if st.button("Load Article"):
    with st.spinner("Processing article..."):
        try:
            ingest_url(url)
            st.success("Article loaded successfully!")
        except Exception as e:
            st.error(f"Error: {e}")

# =========================
# QUESTION INPUT
# =========================
query = st.text_input("Ask a question")

# =========================
# RUN AGENT
# =========================
if st.button("Analyze") and query:
    with st.spinner("Analyzing..."):
        try:
            response_placeholder = st.empty()

            for event in agent.stream(
                {"messages": [{"role": "user", "content": query}]},
                stream_mode="values",
            ):
                response_placeholder.markdown(
                    event["messages"][-1].content
                )

        except Exception as e:
            st.error(f"Error: {e}")