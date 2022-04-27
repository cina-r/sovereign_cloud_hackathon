import streamlit as st

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
st.write("Test")
x = st.selectbox('Klaus', ['a', 'b', 'c'])
st.write(f"You selected: {x}")

y = st.slider("MySlider", 1, 100)


# Play audio
audio_file = open('dog.wav', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/wav')


