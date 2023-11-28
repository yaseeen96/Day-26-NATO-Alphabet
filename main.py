import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

name = input("Enter your name: ").strip()

new_alphabet = {row.letter:row.code for (_,row) in alphabets.iterrows()}


phonetic_list = [new_alphabet[letter.upper()] for letter in name]

print(phonetic_list)