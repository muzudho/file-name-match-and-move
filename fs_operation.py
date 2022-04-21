# File system operation

import os
import glob


def input_change_current_directory(prompt_message):
    """カレント ディレクトリーを替えます"""
    path = input(prompt_message)

    # カレントディレクトリを移動
    os.chdir(path)


def list_current_directory_files_no_echo():
    return glob.glob("./*")

def list_current_directory_files():
    """カレント ディレクトリーのファイルを一覧します"""
    print(f"""
Files
-----""")

    files = list_current_directory_files_no_echo()

    # 一覧します
    for file in files:
        basename = os.path.basename(file)
        print(basename)

    return files


def list_directory_files(dir_path):
    """指定のディレクトリーのファイルを一覧します"""
    if not(dir_path.endswith("/") or dir_path.endswith("\\")):
        dir_path += os.path.sep

    print(f"Destination directory: {dir_path}")

    print(f"""
Destination Files
-----------------""")

    files = glob.glob(f"{dir_path}*")

    # 一覧します
    for file in files:
        basename = os.path.basename(file)
        print(basename)

    return files


def input_y(prompt_message):
    """はい？"""
    print(prompt_message)

    answer = input()

    return answer.upper() == "Y"
