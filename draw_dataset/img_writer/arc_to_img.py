# -*- coding: utf-8 -*-
"""円弧画像を作成するモジュール."""

import numpy as np
from PIL import ImageDraw

from img_writer.param_to_img import Param2Img


class Arc2Img(Param2Img):
    """指定サイズの画像へ円弧を描画するクラス."""

    def draw_ent(self, param: np.ndarray, target: ImageDraw.ImageDraw = None,
                 color=(0, 0, 0), lineweight=1):
        draw = self.draw if target is None else target
        center = param[8:10]
        radius = param[10]
        start_corner = [center[0] - radius, center[1] + radius]
        end_corner = [center[0] + radius, center[1] - radius]
        start_angle = param[11]
        sweep_angle = param[12]
        end_angle = start_angle + sweep_angle
        xy = self.convert_cood(start_corner), self.convert_cood(end_corner)
        draw.arc(xy, start_angle, end_angle, fill=color, width=max(1, int(lineweight)))