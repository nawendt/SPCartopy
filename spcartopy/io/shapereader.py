"""
This module contains custom extensions to download and process SPC geoJSON files.

"""

import os
import re

from cartopy.io import Downloader
from cartopy.io.shapereader import FionaReader, FionaRecord
from cartopy import config


def SPC(fday, ftime, year, month, day, hazard, product):
    """
    Return the path to the requested SPC Convective Outlook geoJSON.

    """
    outlook_downloader = Downloader.from_config(('geoJSON', 'Day{fday:1d}Outlook'.format(fday=fday),
                                                 fday, ftime, year, month, day, hazard, product))
    format_dict = {'config': config, 'ftime': ftime, 'year': year,
                   'month': month, 'day': day, 'hazard': hazard, 'product': product}

    return outlook_downloader.path(format_dict)


class SPCReader(FionaReader):
    """
    Specializes :class:`cartopy.io.shapereader.FionaReader` to properly read and
    filter SPC geoJSON files.

    """

    def __init__(self, filename, bbox=None):
        super(SPCReader, self).__init__(filename, bbox)

    def geometries(self, filter=None):
        """
        Overrides :meth:`~FionaReader.geometries` so that specified geomtries
        can be filtered based on record attributes.

        Parameters
        ----------
        filter
        A dictionary containing key:value pairs used to filter geometries.

        """
        if filter is None:
            filter = {}

        for item in self._data:
            if any([item[key] == value for key, value in filter.items()]):
                continue
            else:
                yield item['geometry']

    def records(self, filter=None):
        """
        Overrides :meth:`~FionaReader.records` so that specified records
        can be filtered based on record attributes.

        Parameters
        ----------
        filter
        A dictionary containing key:value pairs used to filter records.

        """
        if filter is None:
            filter = {}
            
        for item in self._data:
            if any([item[key] == value for key, value in filter.items()]):
                continue
            else:
                yield FionaRecord(item['geometry'],
                                {key: value for key, value in
                                item.items() if key != 'geometry'})


class ConvectiveOutlookDownloader(Downloader):
    """
    Base class that extends :class:`cartopy.io.Downloader` for SPC convective outlooks.

    """
    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template,
                 target_path_template,
                 pre_downloaded_path_template,
                 ):
        super(ConvectiveOutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    def acquire_resource(self, target_path, format_dict):
        target_dir = os.path.dirname(target_path)
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)

        url = self.url(format_dict)

        geoJSON_online = self._urlopen(url)

        with open(target_path, 'wb') as fh:
            fh.write(geoJSON_online.read())

        return target_path


class Day1OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 1 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """
    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day1OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)
    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day1OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day1OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day2OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 2 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day2OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day2OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day2OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day3OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 3 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day3otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day3OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day3OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day3otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day3OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day4OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 4 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
                         '/day4prob_{year:4d}{month:02d}{day:02d}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day4OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day4OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day4otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day4OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day5OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 5 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
                         '/day5prob_{year:4d}{month:02d}{day:02d}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day5OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day5OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day5otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day5OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day6OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 6 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
                         '/day6prob_{year:4d}{month:02d}{day:02d}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day6OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day6OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day6otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day6OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day7OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 7 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
                         '/day7prob_{year:4d}{month:02d}{day:02d}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day7OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day6OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day7otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day7OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day8OutlookDownloader(ConvectiveOutlookDownloader):
    """
    Specializes :class:`spcartopy.io.ConvectiveOutlookDownloader` to download the Day 8 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
                         '/day8prob_{year:4d}{month:02d}{day:02d}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day8OutlookDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day8OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day8otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day8OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)

                                        
# Add a generic SPC Convective Outlook geoJSON downloader to the config dictionary's
# 'downloaders' section.
_day1_co_key = ('geoJSON', 'Day1Outlook')
_day2_co_key = ('geoJSON', 'Day2Outlook')
_day3_co_key = ('geoJSON', 'Day3Outlook')
_day4_co_key = ('geoJSON', 'Day4Outlook')
_day5_co_key = ('geoJSON', 'Day5Outlook')
_day6_co_key = ('geoJSON', 'Day6Outlook')
_day7_co_key = ('geoJSON', 'Day7Outlook')
_day8_co_key = ('geoJSON', 'Day8Outlook')

config['downloaders'].setdefault(_day1_co_key, Day1OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day2_co_key, Day2OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day3_co_key, Day3OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day4_co_key, Day4OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day5_co_key, Day5OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day6_co_key, Day6OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day7_co_key, Day7OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day8_co_key, Day8OutlookDownloader.default_downloader())
