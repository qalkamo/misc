# readme



## 12/31

### vcf install
```pip install PyVCF==0.3.0```
vcf.gz.tbiを読み込む方法に手こずっていて特に進捗なし
txt, csvなどに変換できれば

### v2ファイル追加機能
９番目、１０番目…の列情報を追加
読み込む行の最大値(`last_line`)で指定できるようにした。

## 12/29
入力例:
```bash
input file name:
test2.txt
output file name:
test2output.txt
```

また検索単語は、word_listに入れておく
* get_wordlistのis_newlineは、word_list.txtで各単語の列挙の際に改行を行ったかどうかを表す。

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