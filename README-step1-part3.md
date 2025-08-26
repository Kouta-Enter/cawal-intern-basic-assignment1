## 【Part3】ファイルを読み込んでデータを処理してみよう - word_count.py
**目的**: ファイル操作（読み書き）と文字列処理の理解

**内容**:

任意のテキストファイル（英語のテキスト）を読み込み、行数・単語数・文字数を出力（wcコマンド風）
文字数にはスペースや改行文字も含める。

**実行例**:

test.txt:
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
`$ python word_count.py test.txt`をターミナルで実行すると、word_count_result.txtが生成される。 word_count_result.txt:
```
行数：9
単語数:154
文字数:957
```