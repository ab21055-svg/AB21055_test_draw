#　概要

円，直線，円弧の3つのデータセットの作成を行う

- 実行するのは次の3つ。
- `generate_circle_dataset.py`
- `generate_line_dataset.py`
- `generate_arc_dataset.py`


## 実行方法

1．  `pip install -r requirements.txt`
2． 生成したい図形に応じて次のどれかを実行する
- 円: `python generate_circle_dataset.py`
- 直線: `python generate_line_dataset.py`
- 円弧: `python generate_arc_dataset.py`


例えば `generate_circle_dataset.py` を開くと、このような部分があります。

```
COUNT = 100
DATASET_NAME = 'test_circle_data_n1'

```

- `COUNT`: そのデータセットの画像枚数
- `DATASET_NAME`: そのデータセットの出力フォルダ名

直線は `generate_line_dataset.py`、円弧は `generate_arc_dataset.py` に同じ形で書いてあります。


## 出力先

生成されたデータセットは `imgs/` の下に出ます。

- `python generate_circle_dataset.py` を実行した場合: `imgs/test_circle_data_n1`
- `python generate_line_dataset.py` を実行した場合: `imgs/test_line_data_n1`
- `python generate_arc_dataset.py` を実行した場合: `imgs/test_arc_data_n1`

各フォルダには以下が入ります。

- `p00000.jpg` 形式の画像
- 元パラメータ CSV
- `labels.csv`