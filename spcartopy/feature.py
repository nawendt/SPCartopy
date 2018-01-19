"""
This module defines :class:`Feature` instances, for use with
ax.add_feature().

"""

from cartopy.feature import Feature
import cartopy.crs

import spcartopy.io.shapereader as shapereader

_SPC_GEOM_CACHE = {}


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
        super().__init__(cartopy.crs.PlateCarree(),
                         **kwargs)
        self.fday = fday
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.product = product

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

        return iter(geometries)
