# Copyright (c) 2026 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Hatching for SPC outlook plots."""

import matplotlib.hatch
from matplotlib.path import Path


class SPCHatch(matplotlib.hatch.Shapes):
    """SPC hatching style.

    Create hatching that appears with SPC probabalistic forecasts denoting significant
    tornadoes, wind, or hail. This hatching is also used for Intensity Level 1.
    """

    filled = False
    size = 1.0
    path = Path([(0, 0), (0.4, 0.4)], [Path.MOVETO, Path.LINETO])

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('S')) * density
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        super().__init__(hatch, density)


matplotlib.hatch._hatch_types.append(SPCHatch)
