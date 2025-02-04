import pickle

with open('en_ja_dict.pkl', 'rb') as f:
    en_ja_dict = pickle.load(f)

ja_en_dict = {v: k for k,v in en_ja_dict.items()}
print(ja_en_dict)
with open('ja_en_dict.pkl', 'wb') as f:
    pickle.dump(ja_en_dict, f)