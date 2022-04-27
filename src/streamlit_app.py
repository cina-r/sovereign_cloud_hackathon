import streamlit as st
import deepl
import lookup_dictionary
import speech_recognition as sr
import deepl

st.set_page_config(
    layout="wide", page_title="Health Care", page_icon="🚑"
)  # Use the full page instead of a narrow central column

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

#DeepL translator
auth_key = "bf16c3b7-c877-103a-8e59-08527ae43ef9:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

st.sidebar.image("logo.jpg")

navi = st.sidebar.radio('Navigation', options=["Doctor's View", "Patient's View"])

# Initialization
if 'diagnosis_text' not in st.session_state:
    st.session_state['diagnosis_text'] = ''
    st.session_state['age'] = 1
    st.session_state['name'] = ''
    st.session_state['sex'] = 'male'
    st.session_state['weight'] = 70
    st.session_state['height'] = 170


if navi == "Doctor's View":
    # st.markdown('<p class="big-font">Patient Info</p>', unsafe_allow_html=True)
    name, gender = st.columns([8, 2])
    st.session_state['name'] = name.text_input("Name:", value=st.session_state['name'])
    genders = ["male", "female", "diverse"]
    st.session_state['sex'] = gender.selectbox("Gender:", options=genders, index=genders.index(st.session_state['sex']))
    age, weight, height = st.columns([3, 3, 3])
    st.session_state['age'] = age.slider("Age:", 1, 100, value=st.session_state['age'])
    st.session_state['height'] = weight.slider("Height:", 20, 220, value = st.session_state['height'])
    st.session_state['weight'] = height.slider("Weight:", 1, 200, value = st.session_state['weight'])
    audio_file, audio_play = st.columns([3, 3])
    diagnosis_doc = audio_file.selectbox("Diagnosis:", ["audio-test-1.wav","audio-test-2.wav", "dementia.wav"])


    audio_file = open(diagnosis_doc, 'rb')
    audio_bytes = audio_file.read()
    audio_play.markdown("Listen to diagnosis:")
    audio_play.audio(audio_bytes, format='audio/wav')
    if st.button("Speech2Text"):
        r = sr.Recognizer()
        with sr.AudioFile(diagnosis_doc) as source:
            # listen for the data (load audio to memory)
            audio_data = r.record(source)
            # recognize (convert from speech to text)
            text = r.recognize_sphinx(audio_data)
            st.session_state['diagnosis_text'] = text
    st.session_state['diagnosis_text'] = st.text_area("", value=st.session_state['diagnosis_text'])
    # st.write(st.session_state['diagnosis_text'])


    # st.write("")
    # st.markdown('<p class="big-font">Diagnosis</p>', unsafe_allow_html=True)

    # input_text = st.text_input(label="What do you want to get translated?")
    # language = st.selectbox('Language', ['RU', 'DE', 'EN-GB', 'FR'])
    # if input_text:
    #     result = translator.translate_text(input_text, target_lang=language)
    #     st.write(f"Translation: {result}")


if navi == "Patient's View":
    # st.markdown('<p class="big-font">Diagonis</p>', unsafe_allow_html=True)
    # st.write("")

    st.write("Diagnosis explained:")
    if st.session_state['diagnosis_text']:
        medical_dictionary = lookup_dictionary.medical_dictionary('static/medical_dictionary.csv')
        enriched_diagnosis = lookup_dictionary.add_html_tags_to_text(st.session_state['diagnosis_text'], medical_dictionary.reduced_medical_dictionary_data(st.session_state['diagnosis_text']))

        st.markdown(enriched_diagnosis, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")
        st.markdown("---")
        st.markdown("**Glossary**")
        st.markdown(medical_dictionary.reduced_medical_dictionary_data_as_text(st.session_state['diagnosis_text']), unsafe_allow_html=True)

        auth_key = "bf16c3b7-c877-103a-8e59-08527ae43ef9:fx"  # Replace with your key
        translator = deepl.Translator(auth_key) 

        # Translate text into a target language, in this case, French
        language = ["DE", "EN-GB", "RU"]
        input_lang = st.selectbox("Language:", options=language)
        result = translator.translate_text(st.session_state['diagnosis_text'], target_lang=input_lang)
        st.write(result)  # "Bonjour, le monde !"
        # Note: printing or converting the result to a string uses the output text

        


    # input_text = st.text_input(label="In which language shall the diagnosis be translated?")
    # language = st.selectbox('In which language shall the diagnosis be translated?', ['RU', 'DE', 'EN-GB', 'FR'])
    # if diagnosis:
    #     result = translator.translate_text(diagnosis, target_lang=language)
    #     st.write(f"Translated diagnosis: {result}")

# Play audio
# audio_file = open('dog.wav', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/wav')
