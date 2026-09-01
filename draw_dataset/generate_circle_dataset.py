#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""円データセットを生成する実行ファイル.

1. 画像枚数を変える -> COUNT
2. データセット名を変える -> DATASET_NAME

実行方法:
    python generate_circle_dataset.py
"""

from __future__ import annotations

import csv
import shutil
from pathlib import Path

from generator.circle_generator import CircleGenerater
from img_writer.circle_to_img import Circle2Img


# 画像枚数
COUNT = 100

# 出力フォルダ名と raw CSV 名
DATASET_NAME = 'test_circle_data_n1'

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

    params = CircleGenerater(drawing_size=DRAWING_SIZE).gen_ent(COUNT, min_radius=5.0)
    Circle2Img(drawing_size=DRAWING_SIZE, img_size=IMG_SIZE).draw_imgs(params, str(dataset_dir))

    raw_rows = []
    label_rows = []
    for index, row in enumerate(params):
        image_name = f'p{index:05d}.jpg'
        raw_rows.append([image_name, *map(float, row), 1.0])
        label_rows.append([image_name, float(row[5]), float(row[6]), float(row[7])])

    write_csv(
        dataset_dir / f'{DATASET_NAME}.csv',
        ['image', 'line_type', 'pad1', 'pad2', 'pad3', 'pad4', 'center_x', 'center_y', 'radius', 'pad5', 'pad6', 'pad7', 'pad8', 'pad9', 'label'],
        raw_rows,
    )
    write_csv(dataset_dir / 'labels.csv', ['image', 'center_x', 'center_y', 'radius'], label_rows)

    print('Generated circle dataset:', dataset_dir)
    print('Count:', COUNT)


if __name__ == '__main__':
    main()