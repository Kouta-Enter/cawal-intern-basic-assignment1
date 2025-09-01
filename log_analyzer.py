#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
log_analyzer.py

Usage:
    python log_analyzer.py access.log

What it does:
- Counts requests per IP address
- Prints the top 5 IPs by request count
- Saves the full result to result_YYYYMMDD.txt (using today's date)
"""

import argparse
import datetime as dt
import re
from collections import Counter
from pathlib import Path
import sys


IP_AT_LINE_START = re.compile(r"^(\S+)\s")  # First token on each line


def parse_args() -> argparse.Namespace:
    """コマンドライン引数を処理する。"""
    p = argparse.ArgumentParser(description="Count requests per IP from an access.log.")
    p.add_argument("logfile", type=Path, help="Path to access.log")
    p.add_argument(
        "-n", "--top", type=int, default=5, help="How many top IPs to print (default: 5)"
    )
    return p.parse_args()


def count_ips(log_path: Path) -> Counter:
    """ログファイルを読み込み、各IPアドレスのアクセス回数を数える。"""
    counts = Counter()
    with log_path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            m = IP_AT_LINE_START.match(line)
            if not m:
                continue
            ip = m.group(1)
            counts[ip] += 1
    return counts


def save_results(counts: Counter, outfile: Path) -> None:
    """集計結果を日付付きのファイルに保存する。"""
    with outfile.open("w", encoding="utf-8") as w:
        w.write("# Requests per IP\n")
        w.write(f"# Source: generated from log on {dt.datetime.now():%Y-%m-%d %H:%M:%S}\n\n")
        for ip, cnt in counts.most_common():
            w.write(f"{ip}\t{cnt}\n")


def main() -> int:
    """全体の処理をまとめる実行部分。"""
    args = parse_args()
    if not args.logfile.exists():
        print(f"Error: file not found -> {args.logfile}", file=sys.stderr)
        return 1

    if args.top<1:
        print(f"Error:invalid value ->{args.top}")
        return 1

    counts = count_ips(args.logfile)

    # Print top N
    print(f"Top {min(args.top, len(counts))} IPs:")
    for ip, cnt in counts.most_common(args.top):
        print(f"{ip}\t{cnt}")

    # Save all results with today's date
    today = dt.date.today().strftime("%Y%m%d")
    outname = f"result_{today}.txt"
    outpath = Path(outname)
    save_results(counts, outpath)
    print(f"\nSaved full results to: {outpath.resolve()}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
