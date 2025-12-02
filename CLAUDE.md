# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

ポケモンクイズアプリケーション。ランダムに選ばれた技を覚えるポケモンを60秒以内に5匹答えるゲーム。

## アーキテクチャ

### バックエンド (Flask)
- `src/backend/app.py`: Flaskアプリケーションのエントリーポイント
- `src/backend/models/game.py`: ゲームの状態管理（タイマー、正解チェック、ゲーム終了判定）
- `src/backend/services/`: ビジネスロジック層
  - `quiz_service.py`: ゲーム作成・回答提出の中核ロジック
  - `pokemon_service.py`: PokeAPI呼び出しでポケモン情報取得
  - `pokemon_name_converter.py`: ポケモン名の日英変換と正規化（フォルム違いに対応）
  - `move_name_converter.py`: 技名の日英変換

### フロントエンド (React + TypeScript + Vite)
- `src/frontend/src/App.tsx`: エントリーポイント
- `src/frontend/src/components/Game.tsx`: ゲームの状態管理とUI制御
- `src/frontend/src/components/Timer.tsx`: 60秒カウントダウン
- `src/frontend/src/components/AnswerForm.tsx`: 回答入力フォーム
- `src/frontend/src/services/gameApi.ts`: バックエンドAPI呼び出し

### データ層
- `data/pokemon_names_*.pkl`: ポケモン名の日英変換辞書
- `data/move_learned_by_more_than_5.pkl`: 5匹以上のポケモンが覚える技のリスト

## 開発コマンド

### Docker Compose起動
```bash
cd src
docker-compose up --build
```
- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:5000

### フロントエンド（個別実行）
```bash
cd src/frontend
npm install
npm run dev      # 開発サーバー起動
npm run build    # ビルド
npm run lint     # ESLint実行
```

### バックエンド（個別実行）
```bash
cd src/backend
pip install -r requirements.txt
python app.py    # Flask起動
```

### データスクリプト
```bash
cd src/backend/data_scripts
python prepare_all_poke_name.py   # ポケモン名辞書生成
python prepare_all_move_name.py   # 技名辞書生成
python delete_unusable_move.py    # 使用不可技の削除
```

## 重要な実装詳細

### 名前の正規化
`pokemon_name_converter.py`の`normalize_name()`でポケモン名を正規化し、フォルム違い（例: ニャースとガラルニャース）の判定を行う。正規化後の名前が一致すれば正解と判定。

### ゲームフロー
1. `quiz_service.create_new_game()`: ランダムに技を選び、その技を覚えるポケモンリストを取得
2. ユーザーが回答提出
3. `quiz_service.submit_answer()`: 正規化した名前で照合、正解なら`game.add_answer()`で回答追加
4. `game.check_game_status()`: 5匹正解で"clear"、60秒経過で"timeout"

### API外部依存
PokeAPI (https://pokeapi.co/api/v2) を使用してポケモン情報とスプライト画像を取得。

## テスト
テストファイルは現在存在しない。新規機能追加時はテスト駆動開発で進める。
