# from googletrans import Translator

# translator = Translator(service_urls=[
#     'translate.google.com',
#     'translate.google.co.kr',
# ])

# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

import deepl

auth_key = "1d7fb184-7786-841f-8961-7dc8d1e92f89:fx"  # Replace with your key
translator = deepl.Translator(auth_key) 

# Translate text into a target language, in this case, French
input_lang = input("Which target language?")
result = translator.translate_text("Hello, world!", target_lang=input_lang)
print(result)  # "Bonjour, le monde !"
# Note: printing or converting the result to a string uses the output text