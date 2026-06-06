import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translation Tool")

text = st.text_area("Enter Text")

source = st.selectbox(
    "Source Language",
    ["English", "Hindi", "Telugu"]
)

target = st.selectbox(
    "Target Language",
    ["English", "Hindi", "Telugu"]
)

lang_codes = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te"
}

if st.button("Translate"):
    translated = GoogleTranslator(
        source=lang_codes[source],
        target=lang_codes[target]
    ).translate(text)

    st.write("Translated Text:")
    st.success(translated)