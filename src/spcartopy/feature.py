# Copyright (c) 2025 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""SPC `Feature` instances."""

from datetime import datetime
import re

import cartopy.crs
from cartopy.feature import Feature
from cartopy.io.shapereader import FionaReader

import spcartopy.io.shapereader as shapereader
import spcartopy.io.textreader as textreader

_SPC_GEOM_CACHE = {}
_SPC_RECORD_CACHE = {}
_SPC_SHP_CRS = cartopy.crs.PlateCarree()


class ConvectiveOutlookFeature(Feature):
    """An interface to SPC Convective Outlook geoJSON files.

    See https://www.spc.noaa.gov/products/outlook.
    """

    def __init__(self, fday, ftime, year, month, day, hazard, **kwargs):
        super().__init__(_SPC_SHP_CRS, **kwargs)
        self.fday = fday
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.hazard = hazard
        self.product = 'convective_outlook'
        self.timestamp = datetime(self.year, self.month, self.day)
        self._set_plot_properties(self.records())

    def _set_plot_properties(self, records):
        """Set basic cartopy plotting keyword arguments for `ConvectiveOutlookFeature`."""
        self.facecolors = []
        self.edgecolors = []
        self.short_labels = []
        self.long_labels = []

        for rec in records:
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
        """Parse records from SPC geoJSONs."""
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_RECORD_CACHE:
            path = shapereader.spc_convective(fday=self.fday,
                                    ftime=self.ftime,
                                    year=self.year,
                                    month=self.month,
                                    day=self.day,
                                    hazard=self.hazard,
                                    product=self.product)
            if self.hazard in ['hail', 'wind', 'torn']:
                records = tuple(
                    shapereader.SPCReader(path).records(filter_keys={'LABEL': 'SIGN'})
                )
            else:
                records = tuple(shapereader.SPCReader(path).records())
            _SPC_RECORD_CACHE[key] = records
        else:
            records = _SPC_RECORD_CACHE[key]

        return iter(records)

    def geometries(self):
        """Parse geometries from SPC convective geoJSONs."""
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.spc_convective(fday=self.fday,
                                    ftime=self.ftime,
                                    year=self.year,
                                    month=self.month,
                                    day=self.day,
                                    hazard=self.hazard,
                                    product=self.product)
            if self.hazard in ['hail', 'wind', 'torn']:
                geometries = tuple(shapereader.SPCReader(path).geometries(
                    filter_keys={'LABEL': 'SIGN'})
                )
            else:
                geometries = tuple(shapereader.SPCReader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        return iter(geometries)


class FireOutlookFeature(Feature):
    """An interface to SPC Fire Weather Outlook geoJSON files.

    See https://www.spc.noaa.gov/products/fire_wx.
    """

    def __init__(self, fday, ftime, year, month, day, hazard, **kwargs):
        super().__init__(_SPC_SHP_CRS, **kwargs)
        self.fday = fday
        self.ftime = ftime
        self.year = year
        self.month = month
        self.day = day
        self.hazard = hazard
        self.product = 'fire_outlook'
        self.timestamp = datetime(self.year, self.month, self.day)
        self._set_plot_properties(self.records())

    def _set_plot_properties(self, records):
        """Set basic cartopy plotting keyword arguments for `FireOutlookFeature`."""
        self.facecolors = []
        self.edgecolors = []
        self.short_labels = []
        self.long_labels = []

        for rec in records:
            if self.hazard in ['dryt', 'drytcat']:
                self.facecolors.append('none')
            else:
                self.facecolors.append(rec.attributes['fill'])
            self.edgecolors.append(rec.attributes['stroke'])
            self.short_labels.append(rec.attributes['LABEL'])
            self.long_labels.append(rec.attributes['LABEL2'])

        if self.hazard is not None and self.hazard in ['dryt', 'drytcat']:
            self._kwargs['hatch'] = self._kwargs.get('hatch', 'xx')
        self._kwargs['facecolor'] = self._kwargs.get('facecolor', self.facecolors)
        self._kwargs['edgecolor'] = self._kwargs.get('edgecolor', self.edgecolors)

    def records(self):
        """Parse records from SPC fire geoJSONs."""
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_RECORD_CACHE:
            path = shapereader.spc_fire(fday=self.fday,
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
        """Parse geometries from SPC fire geoJSONs."""
        key = (self.ftime, self.year, self.month, self.day, self.hazard)
        if key not in _SPC_GEOM_CACHE:
            path = shapereader.spc_fire(fday=self.fday,
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


class MDFeature(Feature):
    """MD Feature."""

    def __init__(self, year, number, **kwargs):
        super().__init__(_SPC_SHP_CRS, **kwargs)
        self.year = year
        self.number = number

    def geometries(self):
        """Parse geometries from SPC convective geoJSONs."""
        key = (self.year, self.number)
        geometries = []
        if key not in _SPC_GEOM_CACHE:
            path = textreader.spc_md(year=self.year, number=self.number)
            geometries = tuple(FionaReader(path).geometries())
            _SPC_GEOM_CACHE[key] = geometries
        else:
            geometries = _SPC_GEOM_CACHE[key]

        return iter(geometries)


class Day1ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 1 convevtive outlooks."""

    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 1
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day2ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 2 convevtive outlooks."""

    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 2
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day3ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 3 convevtive outlooks."""

    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 3
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day4ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 4 convevtive outlooks."""

    def __init__(self, year, month, day, **kwargs):
        fday = 4
        ftime = None
        hazard = None
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day5ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 5 convevtive outlooks."""

    def __init__(self, year, month, day, **kwargs):
        fday = 5
        ftime = None
        hazard = None
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day6ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 6 convevtive outlooks."""

    def __init__(self, year, month, day, **kwargs):
        fday = 6
        ftime = None
        hazard = None
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day7ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 7 convevtive outlooks."""

    def __init__(self, year, month, day, **kwargs):
        fday = 7
        ftime = None
        hazard = None
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day8ConvectiveOutlookFeature(ConvectiveOutlookFeature):
    """Subclass for Day 8 convevtive outlooks."""

    def __init__(self, year, month, day, **kwargs):
        fday = 8
        ftime = None
        hazard = None
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day1FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 1 fire outlooks."""

    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 1
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day2FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 2 fire outlooks."""

    def __init__(self, ftime, year, month, day, hazard, **kwargs):
        fday = 2
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day3FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 3 fire outlooks."""

    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 3
        ftime = 1200
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day4FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 4 fire outlooks."""

    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 4
        ftime = 1200
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day5FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 5 fire outlooks."""

    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 5
        ftime = 1200
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day6FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 6 fire outlooks."""

    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 6
        ftime = 1200
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day7FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 7 fire outlooks."""

    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 7
        ftime = 1200
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)


class Day8FireOutlookFeature(FireOutlookFeature):
    """Subclass for Day 8 fire outlooks."""

    def __init__(self, year, month, day, hazard, **kwargs):
        fday = 8
        ftime = 1200
        super().__init__(fday, ftime, year, month, day, hazard, **kwargs)
