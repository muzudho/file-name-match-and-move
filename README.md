# file-name-match-and-move

ファイル名のパターンが一致したら、別ディレクトリーへ移動する（＾～＾）

# Run

```shell
python main.py

# ファイルに出力するなら
python main.py > foo.log
```

# Case study

## Case 1

例えばファイル名を以下のように付けているとする。  

```plaintext
201504__shogi__michi10-18
```

これを以下のディレクトリーへ移動したい。  

```plaintext
./done-add-timestamp
```

ならば正規表現は以下のようにする。  

```plaintext
^\d{6}__.*__\d{2}-?[^\.]*.png$
```

文字列フォーマットは以下のようにする。  

```plaintext
{0}{2}-{1}
```

既に `01-` が含まれていれば `01-01-` のように増えていく不具合がある。  

## Case 1

例えばファイル名を以下のように付けているとする。  

```plaintext
202201__go__25-16.png
202201__go__25-16o2.png
```

これを以下のディレクトリーへ移動したい。  

```plaintext
./renamed
```

ならば正規表現は以下のようにする。  

```plaintext
^\d{6}__[^_]*__\d{2}-?\d+(?:o|\d)*.png$
```

文字列フォーマットは以下のようにする。  

```plaintext
{0}{2}-{1}
```
