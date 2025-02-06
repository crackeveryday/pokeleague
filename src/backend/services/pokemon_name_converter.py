from pathlib import Path
import pickle
import jaconv
import re
from difflib import get_close_matches

class PokemonNameConverter:
    def __init__(self):
        self.en_to_ja_data_file = Path("data/pokemon_names_en_ja.pkl")
        self.ja_to_en_data_file = Path("data/pokemon_names_ja_en.pkl")
        self.en_to_ja = {}  # 英語→日本語
        self.ja_to_en = {}  # 日本語→英語
        self.load_data()

    def load_data(self):
        """pklファイルからデータを読み込む"""
        try:
            with self.en_to_ja_data_file.open('rb') as f:
                self.en_to_ja = pickle.load(f)
            with self.ja_to_en_data_file.open('rb') as f:
                self.ja_to_en = pickle.load(f)
        except FileNotFoundError:
            print("辞書ファイルが見つかりません")
        except Exception as e:
            print(f"辞書ファイルの読み込みに失敗: {e}")

    def save_data(self):
        """データをpklファイルとして保存"""
        self.en_to_ja_data_file.parent.mkdir(parents=True, exist_ok=True)
        with self.en_to_ja_data_file.open('wb') as f:
            pickle.dump(self.en_to_ja, f)

    def normalize_name(self, name: str) -> str:
        """名前を正規化（ひらがな化、空白削除など）"""
        name = jaconv.kata2hira(name)  # カタカナ→ひらがな
        name = name.lower()  # 小文字化
        name = re.sub(r'[\s・]', '', name)  # スペースと記号の削除
        return name

    def get_japanese_name(self, en_name: str) -> str | None:
        """英語名から日本語名を取得"""
        return self.en_to_ja.get(en_name.lower())

    def convert_to_english(self, ja_name: str) -> str | None:
        """日本語名から英語名を取得（あいまい検索付き）"""
        # 完全一致を試行
        if ja_name in self.ja_to_en:
            return self.ja_to_en[ja_name]

        # 正規化して検索
        normalized = self.normalize_name(ja_name)
        normalized_dict = {self.normalize_name(k): v for k, v in self.ja_to_en.items()}
        if normalized in normalized_dict:
            return normalized_dict[normalized]

        # # あいまい検索を試行
        # matches = get_close_matches(
        #     normalized,
        #     [self.normalize_name(name) for name in self.ja_to_en.keys()],
        #     n=1,
        #     cutoff=0.8
        # )
        # if matches:
        #     # 元の名前を探して返す
        #     for orig_name, en_name in self.ja_to_en.items():
        #         if self.normalize_name(orig_name) == matches[0]:
        #             return en_name
        return None
