"""
This module defines :class:`Feature` instances, for use with
ax.add_feature().

"""

from datetime import datetime
import re

from cartopy.feature import Feature
import cartopy.crs
import spcartopy.io.shapereader as shapereader

_SPC_GEOM_CACHE = {}
_SPC_RECORD_CACHE = {}
_SPC_SHP_CRS = cartopy.crs.PlateCarree()


class ConvectiveOutlookFeature(Feature):
    """
    An interface to SPC Convective Outlook geoJSON files.

    See https://www.spc.noaa.gov/products/outlook

    """
    def __init__(self, fday, ftime, year, month, day, hazard, **kwargs):
        super(ConvectiveOutlookFeature, self).__init__(_SPC_SHP_CRS, **kwargs)
        self.fday = fday
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.hazard = hazard
        self.product = 'convective_outlook'
        self.timestamp = datetime(self.year, self.month, self.day)
        self._set_plot_properties(self.geometries(), self.records())

    def _set_plot_properties(self, geometries, records):
        """
        Sets basic cartopy plotting keyword arguments appropriate for the :class:`ConvectiveOutlookFeature`.

        """
        self.facecolors = []
        self.edgecolors = []
        self.short_labels = []
        self.long_labels = []

        for geom, rec in zip(geometries, records):
            for _polygon in geom:
                self.facecolors.append(rec.attributes['fill'])
                self.edgecolors.append(rec.attributes['stroke'])
                self.short_labels.append(rec.attributes['LABEL'])
                self.long_labels.append(rec.attributes['LABEL2'])

        if self.hazard is not None and re.search('^sig', self.hazard):
            self._kwargs['hatch'] = self._kwargs.get('hatch', 'SS')
            self._kwargs['facecolor'] = self._kwargs.get('facecolor', 'none')
        else:
            self._kwargs['facecolor'] = self._kwargs.get('facecolor', self.facecolors)

        self._kwargs['edgecolor'] = self._kwargs.get('edgecolor', self.edgecolors)

    def records(self):
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_RECORD_CACHE:
            path = shapereader.SPCC(fday=self.fday,
                                    ftime=self.ftime,
                                    year=self.year,
                                    month=self.month,
                                    day=self.day,
                                    hazard=self.hazard,
                                    product=self.product)
            if self.hazard in ['hail', 'wind', 'torn']:
                records = tuple(shapereader.SPCReader(path).records(filter={'LABEL': 'SIGN'}))
            else:
                records = tuple(shapereader.SPCReader(path).records())
            _SPC_RECORD_CACHE[key] = records
        else:
            records = _SPC_RECORD_CACHE[key]

        return iter(records)

    def geometries(self):
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.SPCC(fday=self.fday,
                                    ftime=self.ftime,
                                    year=self.year,
                                    month=self.month,
                                    day=self.day,
                                    hazard=self.hazard,
                                    product=self.product)
            if self.hazard in ['hail', 'wind', 'torn']:
                geometries = tuple(shapereader.SPCReader(path).geometries(filter={'LABEL': 'SIGN'}))
            else:
                geometries = tuple(shapereader.SPCReader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        return iter(geometries)


class FireOutlookFeature(Feature):
    """
    An interface to SPC Fire Weather Outlook geoJSON files.

    See https://www.spc.noaa.gov/products/fire_wx

    """
    def __init__(self, fday, ftime, year, month, day, hazard, **kwargs):
        super(FireOutlookFeature, self).__init__(_SPC_SHP_CRS, **kwargs)
        self.fday = fday
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.hazard = hazard
        self.product = 'fire_outlook'
        self.timestamp = datetime(self.year, self.month, self.day)
        self._set_plot_properties(self.geometries(), self.records())

    def _set_plot_properties(self, geometries, records):
        """
        Sets basic cartopy plotting keyword arguments appropriate for the :class:`FireOutlookFeature`.

        """
        self.facecolors = []
        self.edgecolors = []
        self.short_labels = []
        self.long_labels = []

        for geom, rec in zip(geometries, records):
            for _polygon in geom:
                self.facecolors.append(rec.attributes['fill'])
                self.edgecolors.append(rec.attributes['stroke'])
                self.short_labels.append(rec.attributes['LABEL'])
                self.long_labels.append(rec.attributes['LABEL2'])

        if self.hazard is not None and self.hazard in ['dryt', 'drytcat']:
            self._kwargs['hatch'] = self._kwargs.get('hatch', 'xx')
        self._kwargs['facecolor'] = self._kwargs.get('facecolor', self.facecolors)
        self._kwargs['edgecolor'] = self._kwargs.get('edgecolor', self.edgecolors)

    def records(self):
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_RECORD_CACHE:
            path = shapereader.SPCF(fday=self.fday,
                                    ftime=self.ftime,
                                    year=self.year,
                                    month=self.month,
                                    day=self.day,
                                    hazard=self.hazard,
                                    product=self.product)

            records = tuple(shapereader.SPCReader(path).records())
            _SPC_RECORD_CACHE[key] = records
        else:
            records = _SPC_RECORD_CACHE[key]

        return iter(records)

    def geometries(self):
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.SPCF(fday=self.fday,
                                    ftime=self.ftime,
                                    year=self.year,
                                    month=self.month,
                                    day=self.day,
                                    hazard=self.hazard,
                                    product=self.product)

            geometries = tuple(shapereader.SPCReader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        return iter(geometries)


class Day1ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 1 convevtive outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 1
        super(Day1ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day2ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 2 convevtive outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 2
        super(Day2ConvectiveOutlookFeature, self).__init__(fday,ftime, year, month,
                                                           day, hazard, **kwargs)


class Day3ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 3 convevtive outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 3
        super(Day3ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day4ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 4 convevtive outlooks.

    """
    def __init__(self, year, month, day, **kwargs):
        fday = 4
        ftime = None
        hazard = None
        super(Day4ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day5ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 5 convevtive outlooks.

    """
    def __init__(self, year, month, day, **kwargs):
        fday = 5
        ftime = None
        hazard = None
        super(Day5ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day6ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 6 convevtive outlooks.

    """
    def __init__(self, year, month, day, **kwargs):
        fday = 6
        ftime = None
        hazard = None
        super(Day6ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day7ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 7 convevtive outlooks.

    """
    def __init__(self, year, month, day, **kwargs):
        fday = 7
        ftime = None
        hazard = None
        super(Day7ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day8ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.ConvectiveOutlookFeature` for
    Day 8 convevtive outlooks.

    """
    def __init__(self, year, month, day, **kwargs):
        fday = 8
        ftime = None
        hazard = None
        super(Day8ConvectiveOutlookFeature, self).__init__(fday, ftime, year, month,
                                                           day, hazard, **kwargs)


class Day1FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 1 fire outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 1
        super(Day1FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day2FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 2 fire outlooks.

    """
    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 2
        super(Day2FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day3FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 3 fire outlooks.

    """
    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 3
        ftime = 1200
        super(Day3FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day4FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 4 fire outlooks.

    """
    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 4
        ftime = 1200
        super(Day4FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day5FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 5 fire outlooks.

    """
    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 5
        ftime = 1200
        super(Day5FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day6FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 6 fire outlooks.

    """
    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 6
        ftime = 1200
        super(Day6FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day7FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 7 fire outlooks.

    """
    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 7
        ftime = 1200
        super(Day7FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)


class Day8FireOutlookFeature(FireOutlookFeature):
    """
    Subclass of :class:`spcartopy.feature.FireOutlookFeature` for
    Day 8 fire outlooks.

    """
    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 8
        ftime = 1200
        super(Day8FireOutlookFeature, self).__init__(fday, ftime, year, month,
                                                     day, hazard, **kwargs)
