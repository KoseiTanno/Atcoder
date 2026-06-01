#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
ABC の「今日解く問題フォルダ」を自動で用意するルーティン。

ルール:
  - 過去問を降順 (… → ABC384 → ABC383 → …) に、1日1コンテストずつ用意する。
  - 各フォルダに a.py / b.py を「# 私の回答」ヘッダ＋問題URL付きで作成する。
  - 既にあるファイルは絶対に上書きしない（解いた answer が消えない）。
  - 同じ日に複数回実行しても、その日のフォルダ作成は1回だけ（二重作成しない）。

launchd（または cron）から毎朝呼ばれる想定。手動で `python3 new_day.py` してもよい。
"""

import datetime
import os
import re
import sys

# --- 設定 -------------------------------------------------------------------
REPO = os.path.dirname(os.path.abspath(__file__))   # このスクリプトが置かれたリポジトリ
ABC_DIR = os.path.join(REPO, "ABC")
STAMP = os.path.join(REPO, ".new_day_stamp")        # 今日分を作成済みかの記録
PROBLEMS = ["a", "b"]                               # 作成する問題（a.py, b.py）

# ファイルの中身。{n}=コンテスト番号, {p}=問題記号(a/b)
TEMPLATE = (
    "# https://atcoder.jp/contests/abc{n}/tasks/abc{n}_{p}\n"
    "# 私の回答\n"
    "\n"
)
# ---------------------------------------------------------------------------


def existing_numbers():
    """ABC/ 配下の数字フォルダ番号を昇順で返す。"""
    nums = []
    for name in os.listdir(ABC_DIR):
        if re.fullmatch(r"\d+", name) and os.path.isdir(os.path.join(ABC_DIR, name)):
            nums.append(int(name))
    return sorted(nums)


def pick_target(nums):
    """次に解くコンテスト番号を決める（降順ルール）。"""
    # まず、既存フォルダのうち a.py が無い（＝まだ手を付けていない）ものを優先。
    for n in nums:
        if not os.path.exists(os.path.join(ABC_DIR, str(n), "a.py")):
            return n
    # 全部 a.py 済みなら、最小番号の1つ下を新規作成。
    return nums[0] - 1


def main():
    today = datetime.date.today().isoformat()

    # 1日1回だけ（手動とlaunchdが重なっても二重作成しない）
    if os.path.exists(STAMP):
        with open(STAMP) as f:
            if f.read().strip() == today:
                print(f"[{today}] 本日分は作成済みです。")
                return

    nums = existing_numbers()
    if not nums:
        print("ABC フォルダが見つかりません。", file=sys.stderr)
        sys.exit(1)

    target = pick_target(nums)
    folder = os.path.join(ABC_DIR, str(target))
    os.makedirs(folder, exist_ok=True)

    created = []
    for p in PROBLEMS:
        path = os.path.join(folder, "{}.py".format(p))
        if not os.path.exists(path):              # 既存ファイルは上書きしない
            with open(path, "w") as f:
                f.write(TEMPLATE.format(n=target, p=p))
            created.append("{}.py".format(p))

    # 今日分を記録
    with open(STAMP, "w") as f:
        f.write(today)

    if created:
        print(f"[{today}] ABC{target} を用意しました: {', '.join(created)}")
    else:
        print(f"[{today}] ABC{target} は既に用意済みでした。")
    print(f"  問題ページ: https://atcoder.jp/contests/abc{target}/tasks")


if __name__ == "__main__":
    main()
