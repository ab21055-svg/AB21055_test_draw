# -*- coding: utf-8 -*-
"""直線ラベルの変換補助."""

from __future__ import annotations

import math


LINE_LABEL_FIELDS = (
    'image',
    'center_x',
    'center_y',
    'half_length',
    'cos2_theta',
    'sin2_theta',
)


def raw_line_row_to_center_label(row: list[float] | tuple[float, ...]) -> tuple[float, float, float, float, float]:
    """端点形式の raw 行を center / half_length / cos2θ / sin2θ へ変換する."""
    start_x = float(row[1])
    start_y = float(row[2])
    end_x = float(row[3])
    end_y = float(row[4])

    dx = end_x - start_x
    dy = end_y - start_y
    length = math.hypot(dx, dy)

    center_x = (start_x + end_x) / 2.0
    center_y = (start_y + end_y) / 2.0
    half_length = length / 2.0

    length_sq = dx * dx + dy * dy
    cos2_theta = (dx * dx - dy * dy) / length_sq
    sin2_theta = (2.0 * dx * dy) / length_sq

    return center_x, center_y, half_length, cos2_theta, sin2_theta