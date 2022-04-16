# File system operation

import os
import glob


def input_change_current_directory(prompt_message):
    """カレント ディレクトリーを替えます"""
    print(prompt_message)

    path = input()

    # カレントディレクトリを移動
    os.chdir(path)


def list_current_directory_files():
    """カレント ディレクトリーのファイルを一覧します"""
    print(f"""
Files
-----""")

    files = glob.glob("./*")

    # とりあえず一覧します
    for file in files:
        basename = os.path.basename(file)
        print(basename)

    return files


def input_y(prompt_message):
    """はい？"""
    print(prompt_message)

    answer = input()

    return answer.upper == "Y"
