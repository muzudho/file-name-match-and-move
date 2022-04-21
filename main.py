import os
import sys
from fs_operation import input_y, input_change_current_directory, \
    list_current_directory_files, list_directory_files, list_current_directory_files_no_echo
from this_operation import input_re_pattern, list_can_move_files, move_files

# 日本のWindows は "cp932" なので、Unicodeに変換
sys.stdout.reconfigure(encoding='utf-8')

# ディレクトリー選択
while True:
    # どのディレクトリーですか？
    input_change_current_directory("""Which directory?
Example: .
""")

    print(f"Current directory: {os.getcwd()}")

    # カレント ディレクトリーのファイルを一覧します
    files = list_current_directory_files()

    # このディレクトリーで合っていますか？
    is_y = input_y("""
Are you sure this is the right directory (y/n)?""")

    if is_y:
        break
    else:
        print("Canceld")

# 移動先ディレクトリー選択
while True:
    dest_dir = input("""Which destination directory?
Example: ./example
""")

    # その ディレクトリーのファイルを一覧します
    _dest_files = list_directory_files(dest_dir)

    # このディレクトリーで合っていますか？
    is_y = input_y("""
Are you sure this is the right directory (y/n)?""")

    if is_y:
        break
    else:
        print("Canceld")

is_dirty_files = False

while True:

    if is_dirty_files:
        files = list_current_directory_files_no_echo()

    is_dirty_files = True

    # 正規表現のパターンを入力してください
    while True:

        # ファイル名パターンの入力
        pattern = input_re_pattern(r"""
Please enter a regular expression pattern.
Example: ^\d{6}__.*__\d{2}-?[^\.]*.txt$""")

        # パターンに一致し、移動も可能なファイル名の一覧
        list_can_move_files(files, pattern, dest_dir)

        # マッチしましたか？
        is_match = input_y("""
Was there a match (y/n)?""")

        if is_match:
            break
        else:
            print("Canceld")

    # 実行しますか？ (y/n)
    is_yes = input_y("""
Do you want to run it (y/n)?
""")

    if is_yes:
        move_files(files, pattern, dest_dir)
    else:
        print("Canceld")

    # コンティニューしますか？ (y/n)
    is_yes = input_y("""
Continue (y/n)?
""")

    if is_yes:
        pass
    else:
        print("Canceld")
        break
