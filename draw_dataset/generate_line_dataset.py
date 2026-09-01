#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""直線データセットを生成する実行ファイル.

ここを変える:
1. 画像枚数を変える -> COUNT
2. データセット名を変える -> DATASET_NAME

実行方法:
    python generate_line_dataset.py
"""

from __future__ import annotations

import csv
import shutil
from pathlib import Path

from generator.line_generator import LineGenerator
from img_writer.line_to_img import Line2Img
from line_label_utils import LINE_LABEL_FIELDS, raw_line_row_to_center_label


# 画像枚数
COUNT = 100

# 出力フォルダ名と raw CSV 名
DATASET_NAME = 'test_line_data_n1'

DRAWING_SIZE = (224, 224)
IMG_SIZE = (224, 224)


def reset_dataset_dir(dataset_dir: Path) -> None:
    if dataset_dir.exists():
        shutil.rmtree(dataset_dir)
    dataset_dir.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, header: list[str], rows: list[list[float | str]]) -> None:
    with open(path, 'w', newline='', encoding='utf-8') as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def main() -> None:
    root = Path(__file__).resolve().parent / 'imgs'
    dataset_dir = root / DATASET_NAME
    reset_dataset_dir(dataset_dir)

    params = LineGenerator(drawing_size=DRAWING_SIZE).gen_ent(COUNT, min_length=20.0)
    Line2Img(drawing_size=DRAWING_SIZE, img_size=IMG_SIZE).draw_imgs(params, str(dataset_dir))

    raw_rows = []
    label_rows = []
    for index, row in enumerate(params):
        image_name = f'p{index:05d}.jpg'
        raw_rows.append([image_name, *map(float, row), 2.0])
        label_rows.append([image_name, *raw_line_row_to_center_label(row)])

    write_csv(
        dataset_dir / f'{DATASET_NAME}.csv',
        ['image', 'line_type', 'start_x', 'start_y', 'end_x', 'end_y', 'pad1', 'pad2', 'pad3', 'pad4', 'pad5', 'pad6', 'pad7', 'pad8', 'label'],
        raw_rows,
    )
    write_csv(dataset_dir / 'labels.csv', list(LINE_LABEL_FIELDS), label_rows)

    print('Generated line dataset:', dataset_dir)
    print('Count:', COUNT)


if __name__ == '__main__':
    main()