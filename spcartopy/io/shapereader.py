"""
This module contains custom extensions to download and process SPC geoJSON files.

"""

import os
import re

from cartopy.io import Downloader
from cartopy.io.shapereader import Reader
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


class Day1OutlookDownloader(Downloader):
    """
    Specialises :class:`cartopy.io.Downloader` to download the Day 1 SPC 
    forecast geoJSON filesto the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """
    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson')

    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day1OutlookDownloader, self).__init__(url_template, target_path_template,
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

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day1OutlookShpDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day1OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day2OutlookDownloader(Downloader):
    """
    Specialises :class:`cartopy.io.Downloader` to download the Day 2 SPC 
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """

    _SPC_URL_TEMPLATE = ('https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson')

    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day2OutlookDownloader, self).__init__(url_template, target_path_template,
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

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day2OutlookDownloader instance.

        """
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard}.geojson')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day2OutlookDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


# Add a generic SPC Convective Outlook geoJSON downloader to the config dictionary's
# 'downloaders' section.
_day1_co_key = ('geoJSON', 'Day1Outlook')
_day2_co_key = ('geoJSON', 'Day2Outlook')
config['downloaders'].setdefault(_day1_co_key, Day1OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day2_co_key, Day2OutlookDownloader.default_downloader())