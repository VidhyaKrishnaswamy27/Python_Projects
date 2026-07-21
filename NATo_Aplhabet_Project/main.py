import pandas as pd
from numpy.f2py.crackfortran import word_pattern

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_dataframe=pd.read_csv('../.venv/nato_phonetic_alphabet.csv')

phonetic_dict={row.letter:row.code for (index,row) in phonetic_dataframe.iterrows()}
# print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_text:
    user_text=input("Enter your word:").upper()
    try:
        new_list=[phonetic_dict[letter] for letter in user_text]
    except KeyError:
        print ("Sorry, letters only in alphabet please")
        generate_text()
    else:
        print(f"Your NATO Phonetic Alphabets are {new_list}")
