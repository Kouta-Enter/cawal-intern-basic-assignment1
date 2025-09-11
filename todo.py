"""todoリスト管理スクリプト step1 課題2"""
import json
import os

DATA_PATH = './CAWAL/basicassignment01/todo_save.json'

def _ensure_file():
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    if not os.path.exists(DATA_PATH):
        with open(DATA_PATH, 'w', encoding='utf-8') as f:
            json.dump({}, f, ensure_ascii=False, indent=2)

def load_tasks():
    """ファイルからタスクを読み込む（dict形式で保存→listで返す）"""
    _ensure_file()
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        todo_dict = json.load(f)
        if not isinstance(todo_dict, dict):
            todo_dict = {}
    # dict → list に直してプログラム内で扱いやすくする
    tasks = [todo_dict[k] for k in sorted(todo_dict.keys(), key=int)]
    return tasks

def save_tasks(tasks):
    """タスクをファイルに保存する（dict形式で保存）"""
    todo_dict = {str(i): task for i, task in enumerate(tasks)}
    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(todo_dict, f, ensure_ascii=False, indent=2)

def list_tasks(tasks):
    """タスク一覧を表示"""
    if not tasks:
        print("(タスクなし)")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"[{i}] {task}")

def add_task(tasks, task):
    """新たなタスクを追加"""
    tasks.append(task)
    print(f"「{task}」を追加しました。")
    return tasks

def _pop_index_strict(index_str, tasks, action_label):
    if not index_str.isdigit():
        print(f"error: {action_label} >> {index_str} <<\nexpected an index number")
        return None
    idx = int(index_str)
    if 1 <= idx <= len(tasks):
        return idx - 1
    print(f"error: {action_label} >> {index_str} <<\n"
          "there is not a task in this index number. input 'list' to check the task.")
    return None

def done_task(index_str, tasks):
    """指定された番号のタスクを完了（削除＋完了メッセージ）"""
    i = _pop_index_strict(index_str, tasks, "done")
    if i is None:
        return tasks
    finished = tasks.pop(i)
    print(f"完了しました。({finished})")
    return tasks

def delete_task(index_str, tasks):
    """タスクの削除"""
    i = _pop_index_strict(index_str, tasks, "delete")
    if i is None:
        return tasks
    removed = tasks.pop(i)
    print(f"削除しました。({removed})")
    return tasks

def deal_tasks(tasks):
    """メインの入力ループとコマンド分岐"""
    try:
        raw = input(">").strip()
    except EOFError:
        return 0

    if not raw:
        return 1

    parts = raw.split()
    cmd = parts[0].lower()

    if cmd == 'list':
        list_tasks(tasks)
        return 1

    if cmd == 'done':
        if len(parts) < 2:
            print("使い方: done <番号>")
            return 1
        done_task(parts[1], tasks)
        return 1

    if cmd == 'delete':
        if len(parts) < 2:
            print("使い方: delete <番号>")
            return 1
        delete_task(parts[1], tasks)
        return 1

    if cmd == 'add':
        if len(parts) < 2:
            print("使い方: add <タスク内容>")
            return 1
        task = raw[len(parts[0]):].strip()
        add_task(tasks, task)
        return 1

    if cmd == 'save':
        save_tasks(tasks)
        print("保存しました。")
        return 1

    if cmd == 'q':
        return 0

    print("error: >>", cmd, "<<\nkeyword is only list, add, done, delete, save, and q!")
    return 1


if __name__ == "__main__":
    todo_list = load_tasks()
    LOOP = 1
    while LOOP:
        LOOP = deal_tasks(todo_list)
