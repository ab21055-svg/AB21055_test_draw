# -*- coding: utf-8 -*-
"""直線画像を作成するモジュール."""

import numpy as np
from PIL import ImageDraw

from img_writer.param_to_img import Param2Img


class Line2Img(Param2Img):
    """指定サイズの画像へ直線を描画するクラス."""

    def draw_ent(self, param: np.ndarray, target: ImageDraw.ImageDraw = None,
                 color=(0, 0, 0), lineweight=1):
        draw = self.draw if target is None else target
        start = param[1:3]
        end = param[3:5]
        xy = self.convert_cood(start), self.convert_cood(end)
        draw.line(xy, fill=color, width=max(1, int(lineweight)))