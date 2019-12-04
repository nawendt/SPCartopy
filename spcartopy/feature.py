"""
This module defines :class:`Feature` instances, for use with
ax.add_feature().

"""

from datetime import datetime

from cartopy.feature import Feature
import cartopy.crs
import spcartopy.colors as spccolors
import fiona
import spcartopy.io.shapereader as shapereader

_D1_OUTLOOK_CHANGE_DATE = datetime(2014, 10, 22, 15)
_D2_OUTLOOK_CHANGE_DATE = datetime(2012, 9, 12, 17)
_SPC_GEOM_CACHE = {}
_SPC_SHP_CRS = cartopy.crs.LambertConformal(central_longitude=0,
                                            central_latitude=0,
                                            standard_parallels=(33, 45))


class ConvectiveOutlookFeature(Feature):
    """
    An interface to SPC Convective Outlook shapefiles.

    See http://www.spc.noaa.gov/products/outlook/archive

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        super(ConvectiveOutlookFeature, self).__init__(_SPC_SHP_CRS, **kwargs)
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.hazard = hazard
        self.product = 'convective_outlook'
        self.timestamp = datetime(self.year, self.month, self.day)



class Day1ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 1 convevtive outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        super(Day1ConvectiveOutlookFeature, self).__init__(ftime, year, month,
                                                           day, hazard, **kwargs)
        self.fday = 1
        self._set_outlook_type(self.timestamp)
        self._set_plot_properties()

    def _color_by_attr(self, colors):
        """
        Associate correct outlook colors to each polygon.
        """
        path = shapereader.SPC(fday=self.fday,
                               ftime=self.ftime,
                               year=self.year,
                               month=self.month,
                               day=self.day,
                               hazard=self.hazard,
                               product=self.product)
        gattr = []
        with fiona.open(path) as shp:
            for geom in shp:
                dn = geom['properties']['DN']
                gattr.append(colors[dn])

        return gattr

    def _set_plot_properties(self):
        """
        Sets basic cartopy plotting keyword arguments appropriate for the :class:`ConvectiveOutlookFeature`.
        """
        if self.hazard == 'hail':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.hail_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard == 'wind':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.wind_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard == 'torn':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.torn_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard == 'cat':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.cat_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard in ['sighail', 'sigtorn', 'sigwind']:
            self._kwargs.setdefault('hatch', 'SS')
            self._kwargs['facecolor'] = 'none'
            self._kwargs.setdefault('edgecolor', 'black')

    def _set_outlook_type(self, outlook_date, change_date=_D1_OUTLOOK_CHANGE_DATE):
        if outlook_date < change_date:
            self.outlook_type = 'legacy'
        else:
            self.outlook_type = 'current'

    def geometries(self):
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.SPC(fday=self.fday,
                                   ftime=self.ftime,
                                   year=self.year,
                                   month=self.month,
                                   day=self.day,
                                   hazard=self.hazard,
                                   product=self.product)
            geometries = tuple(shapereader.Reader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        return iter(geometries)


class Day2ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 2 convevtive outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        super(Day2ConvectiveOutlookFeature, self).__init__(ftime, year, month,
                                                           day, hazard, **kwargs)
        self.fday = 2
        self._set_outlook_type(self.timestamp)
        self._set_plot_properties()

    def _color_by_attr(self, colors):
        """
        Associate correct outlook colors to each polygon.
        """
        path = shapereader.SPC(fday=self.fday,
                               ftime=self.ftime,
                               year=self.year,
                               month=self.month,
                               day=self.day,
                               hazard=self.hazard,
                               product=self.product)
        gattr = []
        with fiona.open(path) as shp:
            for geom in shp:
                dn = geom['properties']['DN']
                gattr.append(colors[dn])

        return gattr

    def _set_plot_properties(self):
        """
        Sets basic cartopy plotting keyword arguments appropriate for the :class:`ConvectiveOutlookFeature`.
        """
        if self.hazard == 'hail':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.hail_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard == 'wind':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.wind_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard == 'torn':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.torn_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard == 'cat':
            self._prob_colors = self._color_by_attr(self._kwargs.pop('colors', spccolors.cat_colors))
            self._kwargs['facecolor'] = self._prob_colors
            self._kwargs['edgecolor'] = self._prob_colors
        elif self.hazard in ['sighail', 'sigtorn', 'sigwind']:
            self._kwargs.setdefault('hatch', 'SS')
            self._kwargs['facecolor'] = 'none'
            self._kwargs.setdefault('edgecolor', 'black')

    def _set_outlook_type(self, outlook_date, change_date=_D2_OUTLOOK_CHANGE_DATE):
        if outlook_date < change_date:
            self.outlook_type = 'legacy'
        else:
            self.outlook_type = 'current'

    def geometries(self):
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.SPC(fday=self.fday,
                                   ftime=self.ftime,
                                   year=self.year,
                                   month=self.month,
                                   day=self.day,
                                   hazard=self.hazard,
                                   product=self.product)
            geometries = tuple(shapereader.Reader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        return iter(geometries)
