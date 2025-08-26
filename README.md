# CAWAL IT基礎研修課題
- リンク:https://www.notion.so/IT-1cd5b4c8502981d7b71ac0eabb4349ad
## step1
- 課題のリンク:https://www.notion.so/1-1cd5b4c8502980c3b616db00d3713bd8?source=copy_link
- チケットのリンク:https://www.notion.so/IT-Step1-24e5b4c8502981dab0b6dc3f6ab23b51?source=copy_link
- Python 3.9.23で動作確認済み
### 【Part1】じゃんけんゲームを作ろう（標準入力と条件分岐）- janken.py

**目的**: `input()` の使い方とif文のロジック構築

**内容**:

- プレイヤー vs コンピュータのじゃんけん
- プレイヤーから「グー / チョキ / パー」を入力で受け取った場合、ランダムに勝敗を判定
- プレイヤーから「グー / チョキ / パー」以外の入力を受け取った場合、エラーメッセージを表示

**実行例**
```
あなたの出す手を入力>グー
あなた： グー
相手： チョキ
->勝ち!

```
### 【Part2】ToDoリスト管理スクリプト（リスト・辞書の操作）- todo.py

**目的**: Pythonのデータ構造（list, dict）を活用する

**内容**:

- コマンドでタスクを追加・表示・完了・削除できるToDoアプリ（簡易CLI）
    - コマンドはadd,done,delete,list,q,saveの6種
        |コマンド|引数       |意味                |
        |------:|----------:|-------------------:|
        |add    |タスク名    |タスクを追加する     |
        |done   |インデックス|タスクを完了する     |
        |delete |インデックス|タスクを削除する     |
        |list   |無し       |タスクの一覧を表示する|
        |q      |無し       |プログラムを終了する  |
        |save   |無し       |タスクを保存する     |
        - 引数が必要なコマンドを引数なしで入力すると、使い方が表示される
        - 引数が必要なコマンドを無効な引数で実行すると、エラーメッセージを表示する

- **設計方針:**
    - タスクの構造: {”title”: タスク名}のdictで保存
    - タスクリスト: listで管理
    - 永続化プログラムを終了してもタスクを保存しておくために、jsonファイルに保存
    - CLI（コマンドラインインターフェース）: ユーザーがコマンドを打ち込んで操作
- **実行例**
```
>list
(タスクなし)
>add task1
「task1」を追加しました。
>list
[1] task1

```
### 【Part3】ファイルを読み込んでデータを処理してみよう - word_count.py

**目的**: ファイル操作（読み書き）と文字列処理の理解

**内容**:

- 任意のテキストファイル（英語のテキスト）を読み込み、行数・単語数・文字数を出力（`wc`コマンド風）
- 文字数にはスペースや改行文字も含める。

**実行例**
- test.txt:
```
Flowers are the reproductive structures of flowering plants. Typically they are structured in four circular levels
around the end of a stalk. These include: sepals, modified leaves that support the flower; petals, often designed to
attract pollinators; male parts, where pollen is presented; and female parts, where pollen is received and its movement
is facilitated to the egg. Pollen, produced in the male sex cells, is transported between the male and female parts of
flowers in pollination. Pollen movement may be caused by animals or factors such as wind or water. After pollination,
the female part of the flower forms a fruit, and the other floral structures die. The fruit protects the seed and aids
in its dispersal. Flowers first evolved between 150 and 190 million years ago, in the Jurassic. Plants with flowers
dominate the majority of the world's ecosystems, and themselves range from tiny orchids and major crop plants to large
trees.
```

`$ python word_count.py test.txt`をターミナルで実行すると、word_count_result.txtが生成される。
word_count_result.txt:
```
行数：9
単語数:154
文字数:957
```