# チャート関係
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

class MyChart():
    source_file_name = None

    type_string = "line"

    chart_title = "sample chart"

    change_color_per_stroke = True

    invert_xaxis = False
    invert_yaxis = True

    fix_aspect_ratio = True

    def showChart(self):
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
        mark_A = "o"
        mark_B = "x"
        mark = mark_A

        for i in csv_input.loc[csv_input[2]=="U"].index :
            x = csv_input.iloc[:, 0].head(i).tail(i-prev)
            y = csv_input.iloc[:, 1].head(i).tail(i-prev)

            if self.type_string == "line" :
                ax.plot(x, y, marker=None, lineStyle="solid")
            elif self.type_string == "point" :
                ax.plot(x, y, marker=mark, lineStyle="none")
            else :
                ax.plot(x, y, marker=".", lineStyle="none")

            prev = i+1
            mark = mark_B if mark == mark_A else mark_A

        # 表示
        plt.show()
