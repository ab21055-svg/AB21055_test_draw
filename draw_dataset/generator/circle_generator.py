# -*- coding: utf-8 -*-
"""円エンティティの座標生成."""

import numpy as np

from generator.param_generator import ParamGenerator


class CircleGenerater(ParamGenerator):
    """円エンティティを生成するクラス."""

    def __init__(self, drawing_size: tuple[int, int] = (224, 224)):
        super().__init__(drawing_size)

    def gen_ent(self, size: int = 1, min_radius: float = 5.0):
        """円の中心と半径を生成する.

        中心はキャンバス内の一様乱数。
        半径は min_radius から max_r - 5 の範囲でサンプルする。
        """
        centers = np.zeros((size, 2))
        radii = np.zeros(size)
        pad = np.zeros((size, 5))

        for index in range(size):
            while True:
                center = self.gen_cord(1)[0]
                center_x, center_y = center
                max_radius = min(center_x, center_y, self.sizeX - center_x, self.sizeY - center_y)
                upper_radius = max_radius - 5.0
                if upper_radius >= min_radius:
                    centers[index] = center
                    radii[index] = self.rng.uniform(min_radius, upper_radius)
                    break

        return np.hstack([pad, centers, radii.reshape(size, 1), pad])