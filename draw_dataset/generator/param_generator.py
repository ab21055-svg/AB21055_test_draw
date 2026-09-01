# -*- coding: utf-8 -*-
"""学習データ用の基本座標生成クラス."""

import numpy as np


class ParamGenerator:
    """任意の座標を生成するクラス."""

    def __init__(self, drawing_size: tuple[int, int] = (224, 224)):
        self.drawing_size = drawing_size
        self.sizeX = drawing_size[0]
        self.sizeY = drawing_size[1]
        self.rng = np.random.default_rng()

    def gen_cord(self, size: int = 1):
        """任意サイズの xy 座標行列を作る."""
        paramx = self.sizeX * self.rng.random((size, 1))
        paramy = self.sizeY * self.rng.random((size, 1))
        return np.hstack([paramx, paramy])