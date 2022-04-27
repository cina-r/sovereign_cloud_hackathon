import streamlit as st
import deepl

auth_key = "bf16c3b7-c877-103a-8e59-08527ae43ef9:fx"  # Replace with your key
translator = deepl.Translator(auth_key) 

# Apply a general css style to a streamlit page
# NOTE that this injects HTML via the unsafe_allow_html=True parameter
# def css_styling():
#     css = """
#         div[role="radiogroup"] {
#         border-left: 2px solid grey;
#         padding-left: 10px;
#         }
# 
#         MainMenu {visibility: hidden; }
#         footer {visibility: hidden;}
#     """
#     st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
# 
# css_styling()

# with st.sidebar:
#     # with st.echo():
#     st.write("This code will be printed to the sidebar.")

navi = st.sidebar.radio('Navigation', options=["Doctor's View", "Patient's View"])
if navi == "Doctor's View":

    st.markdown("""
    <style>
    .big-font {
        font-size:22px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">Doctor View</p>', unsafe_allow_html=True)

    sex = st.text_input(label="Sex:")
    # age = st.text_input(label="Age:")
    age = st.slider("Age:", 1, 100)
    size = st.text_input(label="Size:")
    weight = st.text_input(label="Weight:")

    # st.write("")
    # st.markdown('<p class="big-font">Diagnosis</p>', unsafe_allow_html=True)

    input_text = st.text_input(label="What do you want to get translated?")
    language = st.selectbox('Language', ['RU', 'DE', 'EN-GB', 'FR'])
    if input_text:
        result = translator.translate_text(input_text, target_lang=language)
        st.write(f"Translation: {result}")


# Play audio
audio_file = open('dog.wav', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/wav')
