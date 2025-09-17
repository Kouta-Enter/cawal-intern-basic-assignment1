# Pythonランタイムを親イメージとして使用
FROM python:3.9

# 作業ディレクトリを/rootに設定
WORKDIR /root

# 現在のディレクトリの内容をコンテナ内の/rootにコピー
COPY . /root

# requirements.txtで指定された必要なパッケージをインストール
RUN pip install -r requirements.txt

# ポートの公開
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]

# コンテナ起動時にweb.pyを実行
CMD ["python", "log_analyzer.py"]
