import streamlit as st
from anthropic_script import summarize_and_get_keywords as anthropic_summarize
from openai_script import summarize_and_get_keywords as openai_summarize


def main():
    st.markdown("<h1 style='text-align: center; color: white;'>URL Summarizer and Keyword Extractor</h1>", unsafe_allow_html=True)

    url = st.text_input("Enter the URL:", "")

    st.markdown("""
    <style>
    div.stButton > button:first-child {
        margin: auto;
    }
    </style>""", unsafe_allow_html=True)

    button = st.button("Summarize", key="summarize")

    col1, col2 = st.columns([1, 1], gap="medium")

    anthropic_container = col1.container()
    openai_container = col2.container()

    with anthropic_container:
        st.image("./logo/anth_logo.jpeg", width=50)
        st.subheader("Anthropic Results")

    with openai_container:
        st.image("./logo/openai_logo.jpeg", width=50)
        st.subheader("OpenAI Results")

    if button:
        if url:
            with anthropic_container:
                try:
                    anthropic_result = anthropic_summarize(url)
                    st.markdown(f"<div style='white-space: normal;'>{anthropic_result}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")

            with openai_container:
                try:
                    openai_result = openai_summarize(url)
                    st.markdown(f"<div style='white-space: normal;'>{openai_result}</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")
        else:
            st.error("Please enter a URL.")


if __name__ == "__main__":
    main()
