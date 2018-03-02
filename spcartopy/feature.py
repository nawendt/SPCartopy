"""
This module defines :class:`Feature` instances, for use with
ax.add_feature().

"""

from cartopy.feature import Feature
import cartopy.crs
import spcartopy.colors as spccolors
import spcartopy.io.shapereader as shapereader

_SPC_GEOM_CACHE = {}
_SPC_SHP_CRS = cartopy.crs.LambertConformal(central_longitude=0,
                                            central_latitude=0,
                                            standard_parallels=(33,45))

class ConvectiveOutlookFeature(Feature):
    """
    An interface to SPC Convective Outlook shapefiles.

    See http://www.spc.noaa.gov/products/outlook/archive

    """
    def __init__(self, fday, ftime, year, month, day, product, **kwargs):
        """
        Parameters
        ----------
        fday
            The forecast day of the outlook (e.g., 1, 2)
        ftime
            The forecast time of the outlook (e.g., 1630). Note that and
             outlook such as the 0100 UTC outlook will be entered as 100.
        year
            Year of outlook issuance.
        month
            Month of outlook issuance.
        day
            Day of outlook issuance.
        product
            The SPC outlook product type.

        Other Parameters
        ----------------
        **kwargs
            Keyword arguments to be used when drawing this feature.

        """
        super().__init__(_SPC_SHP_CRS, **kwargs)
        self.fday = fday
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.product = product

        # Default drawing parameters
        if self.product == 'hail':
            self._kwargs.setdefault('facecolor', spccolors.hail_colors)
            self._kwargs.setdefault('edgecolor', spccolors.hail_colors)
        elif self.product == 'wind':
            self._kwargs.setdefault('facecolor', spccolors.wind_colors)
            self._kwargs.setdefault('edgecolor', spccolors.wind_colors)
        elif self.product == 'torn':
            self._kwargs.setdefault('facecolor', spccolors.torn_colors)
            self._kwargs.setdefault('edgecolor', spccolors.torn_colors)
        elif self.product == 'cat':
            self._kwargs.setdefault('facecolor', spccolors.cat_colors)
            self._kwargs.setdefault('edgecolor', spccolors.cat_colors)
        elif self.product == 'sighail':
            self._kwargs.setdefault('hatch', 'x')
            self._kwargs.setdefault('facecolor', 'none')
            self._kwargs.setdefault('edgecolor', 'black')

    def geometries(self):
        key = (self.fday, self.ftime, self.year, self.month, self.day, self.product)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.convective_outlook(fday=self.fday,
                                                  ftime=self.ftime,
                                                  year=self.year,
                                                  month=self.month,
                                                  day=self.day,
                                                  product=self.product)
            geometries = tuple(shapereader.Reader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        # Reversed so that cat/prob colors will be plotted with correct geom
        return reversed(geometries)

