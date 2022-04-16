import os
import re

def input_re_pattern(prompt_message):
    """ファイル名パターンの入力"""
    print(prompt_message)

    patternText = input()

    pattern = re.compile(patternText)

    print(r"""
Numbering
---------""")

    return pattern

def list_name_matched_files(files, pattern):
    """パターンに一致したファイル名の一覧"""
    for i, file in enumerate(files):
        basename = os.path.basename(file)
        result = pattern.match(basename)
        if result:
            # Matched
            # グループ数
            groupCount = len(result.groups())
            buf = f"({i+1}) {basename}"
            for j in range(0, groupCount):
                buf += f" \\{j+1}=[{result.group(j+1)}]"
            print(buf)
        else:
            # Unmatched
            print(f"( ) {basename}")
