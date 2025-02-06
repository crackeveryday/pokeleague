from pathlib import Path
import pickle

class MoveNameConverter:
    def __init__(self):
        self.data_file = Path("data/move_learned_by_more_than_5.pkl")
        self.ja_to_en = {}  # 日本語→英語
        self.load_data()

    def load_data(self):
        """pklファイルからデータを読み込む"""
        try:
            with self.data_file.open('rb') as f:
                self.ja_to_en = pickle.load(f)
        except FileNotFoundError:
            print("技名辞書ファイルが見つかりません")
