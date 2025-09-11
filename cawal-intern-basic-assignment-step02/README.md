### Part2 Docker環境でPythonアプリをコンテナ化
- 課題のリンク:https://www.notion.so/2-1cd5b4c8502981c4b548dcc439bf2a3b?source=copy_link
- チケットのリンク:https://www.notion.so/IT-Step2-24e5b4c85029813ba746d65986aaba23?source=copy_link
**目的**: Dockerfileの作成と、PythonアプリのDocker化体験

**内容**:

- 最小構成の`Dockerfile`を作成し、ログファイルをマウントして結果を出力できるようにする
- `docker-compose`で開発用環境を立ち上げられるようにする
    - 課題1のスクリプトをDockerコンテナで動かせるようにする

**達成条件**:

- `Dockerfile`, `docker-compose.yml`を使って、`docker compose up`で実行可能
- `volumes`でホストの`access.log`をマウント
- 出力ファイルがホストからも見えること

**実行方法**:
- /rootにhostのカレントディレクトリをマウントして、workdirを/rootに変更
```docker run -it --rm -v `pwd`:/root -w /root python:3.9 python3 log_analyzer.py access.log```