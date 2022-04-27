# from googletrans import Translator

# translator = Translator(service_urls=[
#     'translate.google.com',
#     'translate.google.co.kr',
# ])

# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')

import deepl

auth_key = "bf16c3b7-c877-103a-8e59-08527ae43ef9:fx"  # Replace with your key
translator = deepl.Translator(auth_key) 

# Translate text into a target language, in this case, French
input_lang = input("Which target language?")
result = translator.translate_text("Hello, world!", target_lang=input_lang)
print(result)  # "Bonjour, le monde !"
# Note: printing or converting the result to a string uses the output text