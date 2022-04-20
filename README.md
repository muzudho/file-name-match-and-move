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

## Case 2

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

# コメント付き
^\d{6}__[^_]*__\d{2}-?\d+(?:o|\d)*(__[^\.]*)?\.png$

# バージョン番号部のoも数字とみなす場合
^\d{6}__[^_]*__\d{2}-?(?:o|\d)*(__[^\.]*)?\.png$

# jpg もある
^\d{6}__[^_]*__\d{2}-?(?:o|\d)*(__[^\.]*)?\.(?:png|jpg)$
```
