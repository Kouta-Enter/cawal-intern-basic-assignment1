## step2 
### 概要

**目的**: Pythonの基本文法とファイル操作に慣れる、Web APIの基礎的な使い方がわかる

- 研修課題
    - S1 Pythonスクリプトでログ解析ツールを作成
    - S2 Docker環境でPythonアプリをコンテナ化
    - S3 簡易Web APIでログ解析結果を返す
- 使用技術
    - Python
    - Linux
    - Flask
    - Docker
    - Git
- 分析対象のアクセスログ
    - ChatGPT上で、apacheのアクセスログのサンプルを出力
### Part1 Pythonスクリプトでログ解析ツールを作成

**内容**:

- Linux上にあるApacheのアクセスログ（`access.log`）を読み込み、
    - 各IPアドレスのアクセス回数をカウント
    - 上位5件を出力
- 結果は日付付きファイル（`result_YYYYMMDD.txt`）として保存

**達成条件**:

- Pythonスクリプト1本で動作
- Linux CLIから実行できる
- エラー処理を最低限実装（ファイルが存在しない等）