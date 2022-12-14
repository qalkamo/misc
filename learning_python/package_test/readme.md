# `__init__.py`のはたらき

`__init__.py`のimportの初期化を行うことができる。

importする際はimportする関数がどこにあるかの階層構造を書かないと行けないが、
`__init__.py`にその階層構造を書いておけば、
外部ファイルでその階層構造を書く必要がなくなる。

例えば、`module`には`main.py`が入っておりその中に`chkprint2`が入っているが、
このとき`chkprint2`をimportする際には、通常は、
```
from module.main import chkprint2
```
となしなければならない。しかし、`__init__.py`に
```
from .main import chkprint2
```
と書いておくことで、外部ファイルからimportする際に`.main`を省略して書くことができる。

```
from module import chkprint2
chkprint2()
```
または、
```
import module
module.chkprint2()
```

## `__init__.py`における`__all__`
`__all__`を定義しておくことで、`import *`をしたときにどのファイルからimportするかを指定することができる。