import pandas as pd
import csv

class medical_dictionary():
    """
    Class to lookup explanations of specific medical words
    """

    def __init__(self, path_to_dictionary):
        """
        Standard constructor
        """
        self.dictionary = {}

        with open(path_to_dictionary, mode='r') as inp:
            reader = csv.reader(inp)
            self.dictionary = {rows[0]:rows[1] for rows in reader}

    def remove_punctuation(self, input_text):
        return input_text.replace('.', '').replace(',', '').replace(';', '').replace('!', '')

    def preprocess_input_text(self, input_text):
        """
        Preprocess input text (remove . , ; ! and make all lower case)
        """
        return self.remove_punctuation(input_text.lower())

    def reduced_medical_dictionary_data(self, input_text):
        """
        Reduce medical dictionary data to relevant entries from input_text
        """
        reduced_dict = {}
        for word in self.preprocess_input_text(input_text).split():
            if word in self.dictionary:
                reduced_dict[word] = self.dictionary[word]
        return reduced_dict


    def reduced_medical_dictionary_data_as_text(self, input_text):
        """
        Reduce medical dictionary data to relevant entries from input_text as text
        """
        reduced_dict_as_text = ''
        reduced_dict = self.reduced_medical_dictionary_data(input_text)
        for key in reduced_dict:
            reduced_dict_as_text += f"Explanation of {key}: {self.dictionary[key]} \n\n"
        return reduced_dict_as_text

    def enrich_text_with_medical_dictionary_data(self, input_text):
        """
        Enrich text with medical dictionary data
        """
        enriched_text = ""
        for word in input_text.split():
            preprocessed_word = self.preprocess_input_text(word)
            enriched_text += word + " "
            if preprocessed_word in self.dictionary:
                enriched_text += f"({self.dictionary[preprocessed_word]}) "
        return enriched_text

def add_html_tags_to_text(text, term_dict):
    for key in term_dict:
        text = text.replace(key, '<abbr style="background-color:Yellow;" title="' + term_dict[key] + '">' + key + '</abbr>')
    return text

if __name__ == "__main__":
    medical_dictionary = medical_dictionary('src/static/medical_dictionary.csv')
    print("Reduced dict:")
    print(medical_dictionary.reduced_medical_dictionary_data("Patient has an abdominal abscess."))
    print("Reduced dict as text:")
    print(medical_dictionary.reduced_medical_dictionary_data_as_text("Patient has an abdominal abscess."))
    print("Enrichted text:")
    print(medical_dictionary.enrich_text_with_medical_dictionary_data("Patient has an abdominal abscess."))