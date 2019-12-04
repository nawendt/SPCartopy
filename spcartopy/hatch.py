"""
This module contains hatching for SPC plots
"""

import matplotlib.hatch
from matplotlib.patches import Polygon


class SPCHatch(matplotlib.hatch.Shapes):
    """
    Specialises :class:`matplotlib.hatch.Shapes` to create hatching
    that appears with SPC probabalistic forecasts denoting significant
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
