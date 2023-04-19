# Copyright (c) 2023 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Hatching for SPC outlook plots."""

import matplotlib.hatch
from matplotlib.patches import Polygon


class SPCHatch(matplotlib.hatch.Shapes):
    """SPC hatching style.

    Create hatching that appears with SPC probabalistic forecasts denoting significant
    tornadoes, wind, or hail.
    """

    filled = True
    size = 1.0
    path = Polygon([[0, 0], [0.4, 0.4]], closed=True, fill=False).get_path()

    def __init__(self, hatch, density):
        self.num_rows = (hatch.count('S')) * density
        self.shape_vertices = self.path.vertices
        self.shape_codes = self.path.codes
        matplotlib.hatch.Shapes.__init__(self, hatch, density)


matplotlib.hatch._hatch_types.append(SPCHatch)
