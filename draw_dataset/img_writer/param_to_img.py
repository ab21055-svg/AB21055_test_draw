# -*- coding: utf-8 -*-
"""画像サイズ設定と図形描画のベースクラス."""

from pathlib import Path as plib

import numpy as np
from PIL import Image, ImageDraw


class Param2Img:
    """座標を指定サイズの画像に描画するベースクラス."""

    canvas: Image.Image | None = None

    def __init__(self, drawing_size: tuple[int, int] = (224, 224), img_size: tuple[int, int] = (224, 224),
                 background: tuple[int, int, int] = (255, 255, 255)):
        self.drawing_size = drawing_size
        self.img_size = img_size
        self.background = background
        self.reset_img()
        self.dim_rate = (img_size[0] / drawing_size[0], img_size[1] / drawing_size[1])

    def reset_img(self):
        self.canvas = Image.new(mode='RGB', size=self.img_size, color=self.background)
        self.draw = ImageDraw.Draw(self.canvas)

    def convert_cood(self, xy: list[float]) -> tuple[float, float]:
        xy[1] = self.drawing_size[1] - xy[1]
        return xy[0] * self.dim_rate[0], xy[1] * self.dim_rate[1]

    def save_img(self, directory, name):
        path = plib(directory) / name
        self.canvas.save(fp=path, quality=95)

    def draw_imgs(self, params: np.ndarray, directory: str):
        for index, param in enumerate(params):
            name = 'p{:0=5}.jpg'.format(index)
            self.draw_ent(param)
            self.save_img(directory, name)
            self.reset_img()

    def draw_ent(self, param: np.ndarray, target: ImageDraw.ImageDraw | None = None,
                 color=(0, 0, 0), lineweight=1):
        pass