import os
import re
import shutil


def input_re_pattern(prompt_message):
    """ファイル名パターンの入力"""
    print(prompt_message)

    patternText = input()

    pattern = re.compile(patternText)

    return pattern


def list_can_move_files(files, pattern, dest_dir):
    """パターンに一致し、移動も可能なファイル名の一覧"""

    print("""
Numbering
---------""")

    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched

            dest_file = os.path.join(dest_dir, basename)
            if os.path.exists(dest_file):
                # ファイルが既存
                print(f"( ) {file} ----> {dest_file} ready exists")
                continue

            # ファイルを移動可能
            print(f"({i+1}) {file} ----> {dest_file}")
        else:
            # Unmatched
            print(f"( ) {file}")


def move_files(files, pattern, dest_dir):
    """パターンに一致したファイルを移動"""

    print("""
Result
------""")

    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched

            dest_file = os.path.join(dest_dir, basename)
            if os.path.exists(dest_file):
                # ファイルが既存
                print(f"( ) {basename} ready exists")
                continue

            # ファイルを移動
            print(f"({i+1}) {basename} ----> {dest_file}")
            shutil.move(file, dest_file)
        else:
            # Unmatched ----> Ignored
            pass
