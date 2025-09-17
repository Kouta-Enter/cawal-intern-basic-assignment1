#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
log_analyzer.py

Usage:
    - docker-compose up
    - view http://35.74.238.217:5000

What it does:
- Counts requests per IP address
- Prints the top 5 IPs by request count
- Saves the full result to result_YYYYMMDD.txt (using today's date)
"""

import datetime as dt
import json
import re
from collections import Counter
from pathlib import Path
import sys
import flask

app = flask.Flask(__name__)

# IPv4にマッチ
IPv4_AT_LINE_START = re.compile(r"^((\d{1,3}\.){3}\d{1,3}\s)")
# "::"による省略のないIPv6にマッチ
IPv6_AT_LINE_START_1 = re.compile(r"^(([a-f0-9]{1,4}:){7}[a-f0-9]{1,4}\s)")
# "::"で省略されたIPv6にマッチ
IPv6_AT_LINE_START_2 = re.compile(
    r"^(([a-f0-9]{1,4}:){0,6}[a-f0-9]{0,4}::([a-f0-9]{1,4}:){0,6}[a-f0-9]{0,4}\s)"
)
IPv4_MAPPED = re.compile(r"^(::ffff:(\d{1,3}\.){3}\d{1,3}\s)")
LINE_WRITTEN = re.compile(r"\S")


def count_ips(log_path: Path) -> Counter:
    """ログファイルを読み込み、各IPアドレスのアクセス回数を数える。"""
    counts = Counter()
    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m4 = IPv4_AT_LINE_START.match(line)
            m6_1 = IPv6_AT_LINE_START_1.match(line)
            m6_2 = IPv6_AT_LINE_START_2.match(line)
            m4_mapped = IPv4_MAPPED.match(line)
            l = LINE_WRITTEN.match(line)
            if m4:
                ip = m4.group(1)
                counts[ip] += 1
                continue
            if m6_1:
                ip = m6_1.group(1)
                counts[ip] += 1
                continue
            if m6_2:
                ip = m6_2.group(1)
                counts[ip] += 1
                continue
            if m4_mapped:
                ip = m4_mapped.group(1)
                counts[ip] += 1
                continue
            if l:
                counts["not_start_with_ip"] += 1
        return counts


def save_results(counts: Counter, outfile: Path) -> None:
    """集計結果を日付付きのファイルに保存する。"""
    with outfile.open("w", encoding="utf-8") as w:
        w.write("# Requests per IP\n")
        w.write(
            f"# Source: generated from log on {dt.datetime.now():%Y-%m-%d %H:%M:%S}\n\n"
        )
        if counts["not_start_with_ip"] >= 1:
            w.write(
                "先頭がIPアドレスでない行を検知しました。\n\
logが想定と異なる可能性があります。\n\
引数に指定したファイルの内容を確認してください。\n"
            )
        for ip, cnt in counts.most_common():
            if ip == "not_start_with_ip":
                continue
            w.write(f"{ip}\t{cnt}\n")


@app.route("/")
def hello():
    """test"""
    return "success"


@app.route("/analyze", methods=["GET"])
def getdata():
    """GETリクエストのキーに応じてlog_analyzer.pyを動かし、jsonを受け取る"""
    p = Path("./appdata/access.log")
    if not p.exists():
        print("Error: file not found -> ./access.log", file=sys.stderr)
        return "Error: file not found"
    counts = count_ips(p)
    # Save all results with today's date
    today = dt.date.today().strftime("%Y%m%d")
    outname = f"/root/appdata/result_{today}.txt"
    outpath = Path(outname)
    save_results(counts, outpath)
    get_key = flask.request.args.get("top", type=int)
    output = {}
    if not get_key:
        for ip, cnt in counts.most_common():
            if ip == "not_start_with_ip":
                continue
            output[ip] = cnt
        json_out = json.dumps(output, indent=4)
        return json_out
    else:
        for ip, cnt in counts.most_common(get_key):
            if ip == "not_start_with_ip":
                continue
            output[ip] = cnt
        json_out = json.dumps(output, indent=4)
        return json_out


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
