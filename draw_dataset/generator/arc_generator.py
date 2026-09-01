# -*- coding: utf-8 -*-
"""円弧エンティティの座標生成."""

import math
import numpy as np

from generator.param_generator import ParamGenerator


class ArcGenerator(ParamGenerator):
    """円弧エンティティを生成するクラス."""

    def __init__(self, drawing_size: tuple[int, int] = (224, 224)):
        super().__init__(drawing_size)

    @staticmethod
    def _point_on_arc(center_x: float, center_y: float, radius: float, angle_deg: float) -> tuple[float, float]:
        radians = math.radians(angle_deg)
        return (
            center_x + radius * math.cos(radians),
            center_y - radius * math.sin(radians),
        )

    def _arc_fits_canvas(
        self,
        center_x: float,
        center_y: float,
        radius: float,
        start_angle: float,
        sweep_angle: float,
    ) -> bool:
        step_count = max(2, int(math.ceil(sweep_angle)) + 1)
        for angle in np.linspace(start_angle, start_angle + sweep_angle, step_count):
            point_x, point_y = self._point_on_arc(center_x, center_y, radius, float(angle))
            if not (0.0 <= point_x <= self.sizeX and 0.0 <= point_y <= self.sizeY):
                return False
        return True

    def gen_ent(
        self,
        size: int = 1,
        min_radius: float = 10.0,
        min_arc_angle: float = 10.0,
        max_radius: float = 158.0,
        min_rendered_length: float = 30.0,
    ):
        """円弧の中心、半径、開始角、掃引角を生成する.

        収まらない円弧は r <- 0.95 * r で縮小し、
        半径が小さくなりすぎたものは再サンプリングする。
        """
        line_type = np.zeros((size, 1))
        pad = np.zeros((size, 7))
        centers = np.zeros((size, 2))
        radii = np.zeros((size, 1))
        start_angles = np.zeros((size, 1))
        sweep_angles = np.zeros((size, 1))

        for index in range(size):
            while True:
                center_x, center_y = self.gen_cord(1)[0]
                radius = float(self.rng.uniform(min_radius, max_radius))
                start_angle = float(self.rng.uniform(0.0, 360.0))
                sweep_angle = float(self.rng.uniform(min_arc_angle, 270.0))

                while radius >= min_radius and not self._arc_fits_canvas(
                    center_x,
                    center_y,
                    radius,
                    start_angle,
                    sweep_angle,
                ):
                    radius *= 0.95

                if radius < min_radius:
                    continue

                if radius * math.radians(sweep_angle) < min_rendered_length:
                    continue

                centers[index] = (center_x, center_y)
                radii[index, 0] = radius
                start_angles[index, 0] = start_angle
                sweep_angles[index, 0] = sweep_angle
                break

        return np.hstack([line_type, pad, centers, radii, start_angles, sweep_angles])