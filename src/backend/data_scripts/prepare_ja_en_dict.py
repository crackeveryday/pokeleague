import pickle

with open('pokemon_names_en_ja.pkl', 'rb') as f:
    en_ja_dict = pickle.load(f)

ja_en_dict = {v: k for k,v in en_ja_dict.items()}
print(ja_en_dict)
with open('pokemon_names_ja_en.pkl', 'wb') as f:
    pickle.dump(ja_en_dict, f)