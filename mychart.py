# チャート関係
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

class MyChart():
    # csvファイルパス
    source_file_name = None

    # グラフタイプ (line/circlecross/pluscross/period/default)
    type_string = "line"

    # グラフタイトル
    chart_title = "sample chart"

    # DownからUpまでの1ストロークごとにグラフの色を変えるかどうか
    change_color_per_stroke = True

    # 軸の反転
    invert_xaxis = False
    invert_yaxis = True

    # X,Y軸のスワップ
    xy_swap = False

    # グラフのアスペクト比を固定する
    fix_aspect_ratio = True

    def showChart(self):
        # csvファイルパスが指定されていない場合は何もしない
        if self.source_file_name is None:
            return

        # csvファイルをヘッダなしで読み込み
        csv_input = pd.read_csv(filepath_or_buffer=self.source_file_name, encoding="ms932", sep=",", header=None)

        # チャート表示をきれいにする？
        sns.set_style("whitegrid")

        # チャート名を表示
        fig = plt.figure()

        ax = fig.add_subplot(111)
        ax.set_title(self.chart_title)

        # チャートの縦横比を固定
        if self.fix_aspect_ratio:
            ax.set_aspect('equal', 'datalim')

        # X, Y軸を反転させる
        if self.invert_xaxis:
            ax.invert_xaxis()
        if self.invert_yaxis:
            ax.invert_yaxis()
        
        # 3列目が"U"のデータの行数を抽出して、そこでplotを区切る
        # "U"出現ごとにプロットマークを変える
        prev = 0
        if self.type_string == "circlecross":
            mark_A = "o"
            mark_B = "x"
        elif self.type_string == "period" :
            mark_A = ","
            mark_B = ","
        elif self.type_string == "pluscross" :
            mark_A = "+"
            mark_B = "x"
        else:
            mark_A = "."
            mark_B = "."

        mark = mark_A

        if self.change_color_per_stroke:
            for i in csv_input.loc[csv_input[2]=="U"].index :
                if self.xy_swap:
                    y = csv_input.iloc[:, 0].head(i).tail(i-prev)
                    x = csv_input.iloc[:, 1].head(i).tail(i-prev)
                else:
                    x = csv_input.iloc[:, 0].head(i).tail(i-prev)
                    y = csv_input.iloc[:, 1].head(i).tail(i-prev)

                if self.type_string == "line" :
                    ax.plot(x, y, marker=None, lineStyle="solid")
                else :
                    ax.plot(x, y, marker=mark, lineStyle="none")

                prev = i+1
                mark = mark_B if mark == mark_A else mark_A
        else:
            x = csv_input.iloc[:,0]
            y = csv_input.iloc[:,1]
            ax.plot(x,y,marker=".", lineStyle="none")
        
        # 表示
        plt.show()
