### Part 3 簡易Web APIでログ解析結果を返す
- 課題のリンク:https://www.notion.so/2-1cd5b4c8502981c4b548dcc439bf2a3b?source=copy_link
- チケットのリンク:https://www.notion.so/IT-Step2-24e5b4c85029813ba746d65986aaba23?source=copy_link

**目的**: PythonでのWeb API実装とDocker連携を理解する

**内容**:

- FlaskでWeb APIを作成し、ログファイルを解析して結果をJSONで返す(GETリクエスト)
    - 各IPアドレスのアクセス回数をカウント
        - `/analyze`
    - 上位5件を出力
        - `/analyze?top=5`

**達成条件**:

- APIサーバがリクエストを受けてログを解析し、上位N件の結果を返す
- Docker Composeで起動
- curlやPostman or ブラウザで結果確認が可能

**フォルダ構成**:

```
cawal-intern-basic-assignment-step02/
  README.md
  Dockerfile
  docker-compose.yml
  log-analyzer.py
  requirements.txt
  appdata/
    access.log
```

**実行方法**

- `cawal-intern-basic-assignment-step02/`で`docker-compose up`を実行する
- ブラウザで`https://<ホストのIP>:5000`に飛ぶ。`success`と表示される。
- `https://<ホストのIP>:5000/analyze`で解析結果を表示する。
- `https://<ホストのIP>:5000/analyze?top=<表示件数>`で解析結果を上から指定した件数だけ表示する。