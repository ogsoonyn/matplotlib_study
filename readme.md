# matplotlib練習

matplotlibでグラフ表示する練習として作成したコード。
D&Dしたファイルをチャート表示する。

## 実行環境

### Python 3のインストール

[Python.org](https://www.python.org/downloads/)からインストーラを入手。
バージョンは3.7.4で確認。

### パッケージのインストール

matplotlib関連のパッケージをインストール。

```shell
pip install matplotlib pandas numpy seaborn
```

kivy関連のパッケージをインストール。

```shell
pip install kivy pygame cython docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
```

## 使い方

実行すると出てくるウィンドウに、csvファイルをD&Dすると、
データをプロットして出力する。

### 入力データルール

1行3パラメータのcsvファイルとする。
ヘッダは無し。

`<x>,<y>,<event>`

```csv
100,100,D
102,98,M
103,99,M
105,95,M
108,92,U
```
