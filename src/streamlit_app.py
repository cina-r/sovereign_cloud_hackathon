import streamlit as st
import deepl
import lookup_dictionary

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

#DeepL translator
auth_key = "bf16c3b7-c877-103a-8e59-08527ae43ef9:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

st.markdown("""
    <style>
    .big-font {
        font-size:22px !important;
    }
    </style>
    """, unsafe_allow_html=True)


navi = st.sidebar.radio('Navigation', options=["Patient Info", "Diagnosis"])

if navi == "Patient Info":
    # st.markdown('<p class="big-font">Patient Info</p>', unsafe_allow_html=True)

    name = st.text_input(label="Name:")
    sex = st.text_input(label="Sex:")
    # age = st.text_input(label="Age:")
    age = st.slider("Age:", 1, 100)
    size = st.text_input(label="Height:")
    weight = st.text_input(label="Weight:")

    # st.write("")
    # st.markdown('<p class="big-font">Diagnosis</p>', unsafe_allow_html=True)

    # input_text = st.text_input(label="What do you want to get translated?")
    # language = st.selectbox('Language', ['RU', 'DE', 'EN-GB', 'FR'])
    # if input_text:
    #     result = translator.translate_text(input_text, target_lang=language)
    #     st.write(f"Translation: {result}")


if navi == "Diagnosis":
    # st.markdown('<p class="big-font">Diagonis</p>', unsafe_allow_html=True)
    # st.write("")
    diagnosis_doc = st.text_input(label="Diagnosis:")

    st.write("Diagnosis explained:")
    if diagnosis_doc:
        medical_dictionary = lookup_dictionary.medical_dictionary('static/medical_dictionary.csv')
        enriched_diagnosis = lookup_dictionary.add_html_tags_to_text(diagnosis_doc, medical_dictionary.reduced_medical_dictionary_data(diagnosis_doc))

        st.markdown(enriched_diagnosis, unsafe_allow_html=True)


    # input_text = st.text_input(label="In which language shall the diagnosis be translated?")
    # language = st.selectbox('In which language shall the diagnosis be translated?', ['RU', 'DE', 'EN-GB', 'FR'])
    # if diagnosis:
    #     result = translator.translate_text(diagnosis, target_lang=language)
    #     st.write(f"Translated diagnosis: {result}")

# Play audio
# audio_file = open('dog.wav', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/wav')
