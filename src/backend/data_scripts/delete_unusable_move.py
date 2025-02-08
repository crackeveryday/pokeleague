import pickle


with open("data/move_learned_by_more_than_5.pkl", "rb") as f:
    move_dict = pickle.load(f)

del move_dict['ボーンラッシュ']
del move_dict['ボルテッカー']
del move_dict['ハロウィン']
del move_dict['サウザンアロー']
del move_dict['サウザンウェーブ']
del move_dict['グランドフォース']
del move_dict['コアパニッシャー']
del move_dict['ぶちかまし']
del move_dict['アクセルブレイク']
del move_dict['イナズマドライブ']
del move_dict['おかたづけ']
del move_dict['ほうふく']

with open("data/move_learned_by_more_than_5.pkl", "wb") as f:
    pickle.dump(move_dict, f)