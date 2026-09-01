# -*- coding: utf-8 -*-
"""直線エンティティの座標生成."""

import numpy as np

from generator.param_generator import ParamGenerator


class LineGenerator(ParamGenerator):
    """直線エンティティを生成するクラス."""

    def __init__(self, drawing_size: tuple[int, int] = (224, 224)):
        super().__init__(drawing_size)

    def gen_ent(self, size: int = 1, min_length: float = 20.0):
        """直線の始点終点を生成する.

        端点間距離が min_length 未満のときは再サンプリングする。
        """
        line_type = np.zeros((size, 1))
        pad = np.zeros((size, 8))
        lines = []

        for _ in range(size):
            while True:
                start = self.gen_cord(1)[0]
                end = self.gen_cord(1)[0]
                length = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                if length >= min_length:
                    lines.append([start, end])
                    break

        starts = np.array([line[0] for line in lines])
        ends = np.array([line[1] for line in lines])
        return np.hstack([line_type, starts, ends, pad])