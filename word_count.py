""""step1-課題3:任意のテキストファイル(英語のテキスト）を読み込み、行数・単語数・文字数を出力"""
import sys
import os
args = sys.argv
if len(args)<2:
    print('error:読み込むファイルを指定してください。\n$python3 word_count.py >> <<')
else:
    if not os.path.exists(args[1]):
        print("ファイルがありません")
    else:
        with open(args[1], 'r', encoding='utf-8') as f:
            s = f.read()
            lines=len(s.splitlines())
            words=len(s.split())
            length=len(s)
        with open('word_count_result.txt', 'w', encoding='utf-8') as f:
            f.write('行数：'+str(lines) +'\n単語数:'+ str(words)+'\n文字数:'+str(length))
