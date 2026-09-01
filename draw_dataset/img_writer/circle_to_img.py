# -*- coding: utf-8 -*-
"""円画像を作成するモジュール."""

import numpy as np
from PIL import ImageDraw

from img_writer.param_to_img import Param2Img


class Circle2Img(Param2Img):
    """指定サイズの画像へ円を描画するクラス."""

    def draw_ent(self, param: np.ndarray, target: ImageDraw.ImageDraw = None,
                 color=(0, 0, 0), lineweight=1):
        draw = self.draw if target is None else target
        center = param[5:7]
        radius = param[7]

        start_corner = [center[0] - radius, center[1] + radius]
        end_corner = [center[0] + radius, center[1] - radius]
        xy = self.convert_cood(start_corner), self.convert_cood(end_corner)
        draw.ellipse(xy, fill=None, outline=color, width=max(1, int(lineweight)))