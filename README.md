# codecheck

多くのコーディングテストで、標準入力からのデータ入力が強制される。つまり、コードの冒頭で
```python3
value = input()
```
とさせられる。

デバッグ時に厄介なので、画像のようにVScodeの`テスト`及び`pytest`を用いて、デバッグしやすくした。

![image](https://user-images.githubusercontent.com/101625248/236589094-23cd4d8d-f066-4bc0-a8ba-90156e624e13.png)

- [input](https://github.com/GawinGowin/codecheck/tree/main/src/input)  
テストケースの入力を記述

- [output](https://github.com/GawinGowin/codecheck/tree/main/src/output)  
入力に対しての正解を記述

## サンプルコード
- [main.py](https://github.com/GawinGowin/codecheck/tree/main/src/main.py) に記述済み 

二部探索：ALDS1_4_B(https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_4_B&lang=ja)  
自分なりの回答例(競技プログラミングは苦手なのでコードが正しい保証はない)

## 参考
https://rurukblog.com/post/Pytest-Discovery-Error/  
https://rinatz.github.io/python-book/ch08-02-pytest/#_14
