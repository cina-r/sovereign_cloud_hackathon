import streamlit as st
import deepl
import lookup_dictionary
import speech_recognition as sr
import deepl

st.set_page_config(
    layout="wide", page_title="HealthCareAssist", page_icon="🚑"
)  # Use the full page instead of a narrow central column


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles.css")

# DeepL translator
auth_key = "1d7fb184-7786-841f-8961-7dc8d1e92f89:fx"  # Replace with your key
translator = deepl.Translator(auth_key)

st.sidebar.markdown("**HealthCareAssist** Pro", unsafe_allow_html=True)
st.sidebar.image("logo.jpg", width=128)
st.sidebar.markdown("powered by <font color=#e20075>Telekom</font> and <font color=#4285F4>Google</font>", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)
navi = st.sidebar.radio("", options=["Doctor's View", "Patient's View"])

# Initialization
if "diagnosis_text" not in st.session_state:
    st.session_state["diagnosis_text"] = ""
    st.session_state["age"] = 1
    st.session_state["name"] = ""
    st.session_state["sex"] = "male"
    st.session_state["weight"] = 70
    st.session_state["height"] = 170


patient_repo = {
    "Darth Vader": {"gender": "male", "age": 48, "weight": 89, "height": 180, "diagnosis": "heavy burnings"},
    "Han Solo": {"gender": "male", "age": 42, "weight": 82, "height": 182, "diagnosis": "trust issues"},
    "Lea Organa": {"gender": "female", "age": 37, "weight": 68, "height": 176, "diagnosis": "mentally instable"},
}


if navi == "Doctor's View":
    patient = st.selectbox("Patients", options=["New Patient", "Darth Vader", "Han Solo", "Lea Organa"])
    if patient == "New Patient":
        st.markdown("## New Patient")
        name, gender = st.columns([8, 2])
        st.session_state["name"] = name.text_input("Name:", value=st.session_state["name"])
        genders = ["male", "female", "diverse"]
        st.session_state["sex"] = gender.selectbox(
            "Gender:", options=genders, index=genders.index(st.session_state["sex"])
        )
        age, weight, height = st.columns([3, 3, 3])
        st.session_state["age"] = age.slider("Age:", 1, 100, value=st.session_state["age"])
        st.session_state["height"] = weight.slider("Height:", 20, 220, value=st.session_state["height"])
        st.session_state["weight"] = height.slider("Weight:", 1, 200, value=st.session_state["weight"])
        audio_file, audio_play = st.columns([3, 3])
        diagnosis_doc = audio_file.selectbox("Diagnosis:", ["fracture.wav", "inpatient.wav", "dementia.wav"])

        audio_file = open(diagnosis_doc, "rb")
        audio_bytes = audio_file.read()
        audio_play.markdown("Listen to diagnosis:")
        audio_play.audio(audio_bytes, format="audio/wav")
        if st.button("Speech2Text"):
            r = sr.Recognizer()
            with sr.AudioFile(diagnosis_doc) as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text)
                text = r.recognize_sphinx(audio_data)
                st.session_state["diagnosis_text"] = text
        st.session_state["diagnosis_text"] = st.text_area("", value=st.session_state["diagnosis_text"])
        if st.button("Save"):
            st.success("Patient data saved")
    else:
        name, gender = st.columns([8, 2])
        name.text_input("Name:", value=patient)
        genders = ["male", "female", "diverse"]
        gender.selectbox("Gender:", options=genders, index=genders.index(patient_repo[patient]["gender"]))
        age, weight, height = st.columns([3, 3, 3])
        age.slider("Age:", 1, 100, value=patient_repo[patient]["age"])
        weight.slider("Height:", 20, 220, value=patient_repo[patient]["height"])
        height.slider("Weight:", 1, 200, value=patient_repo[patient]["weight"])
        st.text_area("", value=patient_repo[patient]["diagnosis"])

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
    if st.session_state["diagnosis_text"]:
        medical_dictionary = lookup_dictionary.medical_dictionary("static/medical_dictionary.csv")
        enriched_diagnosis = lookup_dictionary.add_html_tags_to_text(
            st.session_state["diagnosis_text"],
            medical_dictionary.reduced_medical_dictionary_data(st.session_state["diagnosis_text"]),
        )

        st.markdown(enriched_diagnosis, unsafe_allow_html=True)

        st.write("\n")
        st.write("\n")
        st.markdown("---")
        st.markdown("**Glossary**")
        st.markdown(
            medical_dictionary.reduced_medical_dictionary_data_as_text(st.session_state["diagnosis_text"]),
            unsafe_allow_html=True,
        )

        auth_key = "bf16c3b7-c877-103a-8e59-08527ae43ef9:fx"  # Replace with your key
        translator = deepl.Translator(auth_key)

        # Translate text into a target language, in this case, French
        language = ["DE", "EN-GB", "RU"]
        input_lang = st.selectbox("Language:", options=language)
        result = translator.translate_text(st.session_state["diagnosis_text"], target_lang=input_lang)
        st.markdown(str(result), unsafe_allow_html=True)  # "Bonjour, le monde !"
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
