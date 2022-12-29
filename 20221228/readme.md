# readme

## 12/29
入力例:
```bash
input file name:
test2.txt
output file name:
test2output.txt
list of words you are looking for:
stop hello world
```

実行時間が名称のディレクトリにファイルが作成され、単語が含まれる行がいくつかあるかをリストとして出力する。
作成されたファイルには出力されるべき行と行数が書かれている
```
stop: 4
hello: 1
world: 0
```

## 12/28
* txt fileに所定の単語が何個入っているかを数える関数
* 行列の、ある列に「Aという要素」がある行をすべて書き出して、新しい行列を作る、ような関数

## 実行
対象のtxtファイルを `count_words.py` と同じディレクトリに入れて、以下をターミナル上で実行する。
```bash
python count_words.py
```

ファイル名と探している単語が聞かれるので、適宜入力する