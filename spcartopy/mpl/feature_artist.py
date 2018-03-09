import warnings

import cartopy.mpl.feature_artist
import cartopy.mpl.patch as cpatch
import matplotlib.collections


class FeatureArtist(cartopy.mpl.feature_artist.FeatureArtist):

    def draw(self):
        """
        Draw the geometries of the feature that intersect with the extent of
        the :class:`spcartopy.mpl.GeoAxes` instance to which this
        object has been added.

        """

        print('TEST')
