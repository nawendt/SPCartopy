"""
Module containing legend objects for plotting.

"""

from spcartopy.colors import Outlooks

from matplotlib.patches import Rectangle

class SPCLegend(object):
    """
    SPC Legends

    """

    @classmethod
    def convectiveCategorical(cls):
        handles = []
        labels = []
        for cat, props in Outlooks.categorical.items():
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'], fc=props['fc']))
            labels.append(props['label'])

        return tuple([handles, labels])