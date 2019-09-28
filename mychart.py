# チャート関係
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def showChart(file_name):
    # csvファイルをヘッダなしで読み込み
    csv_input = pd.read_csv(filepath_or_buffer=file_name, encoding="ms932", sep=",", header=None)

    # チャート表示をきれいにする？
    sns.set_style("whitegrid")

    # チャート名を表示
    plt.title(file_name)

    # チャートの縦横比を固定
    plt.axes().set_aspect('equal', 'datalim')

    # 3列目が"U"のデータの行数を抽出して、そこでplotを区切る
    # "U"出現ごとにプロットマークを変える
    prev = 0
    mark_A = "o"
    mark_B = "x"
    mark = mark_A

    for i in csv_input.loc[csv_input[2]=="U"].index :
        x = csv_input.iloc[:, 0].head(i).tail(i-prev)
        y = csv_input.iloc[:, 1].head(i).tail(i-prev)
        plt.plot(x, y, marker=None, lineStyle="solid")
        #plt.plot(x, y, marker=mark, lineStyle="none") # marker
        prev = i+1
        mark = mark_B if mark == mark_A else mark_A

    # 表示
    plt.show()

    return