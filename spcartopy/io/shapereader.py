"""
This module contains custom extensions to download and process SPC shapefiles.

"""

import os
import re

import six

from cartopy.io import Downloader
from cartopy.io.shapereader import Reader
from cartopy import config


def SPC(fday, ftime, year, month, day, hazard, product):
    """
    Return the path to the requested SPC Convective Outlook shapefile,
    downloading and unzipping if necessary.

    """
    outlook_downloader = Downloader.from_config(('shapefiles', 'Day{fday:1d}Outlook'.format(fday=fday),
                                                 fday, ftime, year, month, day, hazard, product))
    format_dict = {'config': config, 'ftime': ftime, 'year': year,
                   'month': month, 'day': day, 'hazard': hazard, 'product': product}

    return outlook_downloader.path(format_dict)


class Day1OutlookShpDownloader(Downloader):
    """
    Specialises :class:`cartopy.io.Downloader` to download the zipped
    Day 1 SPC forecast shapefiles and extract them to the defined location
    (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """

    _SPC_URL_TEMPLATE = ('http://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}-shp.zip')

    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day1OutlookShpDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    def zip_file_contents(self, format_dict):
        for ext in ['.shp', '.dbf', '.shx', '.prj']:
            yield ('day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard}'
                   '{extension}'.format(extension=ext, **format_dict))

    def acquire_resource(self, target_path, format_dict):
        from zipfile import ZipFile

        target_dir = os.path.dirname(target_path)
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)

        url = self.url(format_dict)

        shapefile_online = self._urlopen(url)

        zfh = ZipFile(six.BytesIO(shapefile_online.read()), 'r')

        for member_path in self.zip_file_contents(format_dict):
            ext = os.path.splitext(member_path)[1]
            target = os.path.splitext(target_path)[0] + ext
            member = zfh.getinfo(member_path)
            with open(target, 'wb') as fh:
                fh.write(zfh.open(member).read())

        shapefile_online.close()
        zfh.close()

        return target_path

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day1OutlookShpDownloader instance.

        """
        default_spec = ('shapefiles', 'SPC', '{product}', '{year:4d}',
                        'day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard}.shp')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day1OutlookShpDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


class Day2OutlookShpDownloader(Downloader):
    """
    Specialises :class:`cartopy.io.Downloader` to download the zipped
    Day 2 SPC forecast shapefiles and extract them to the defined location
    (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """

    _SPC_URL_TEMPLATE = ('http://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}-shp.zip')

    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(Day2OutlookShpDownloader, self).__init__(url_template, target_path_template,
                                                       pre_downloaded_path_template)

    # def zip_file_contents(self, format_dict):
    #     for ext in ['.shp', '.dbf', '.shx', '.prj']:
    #         if re.search('{hazard}.*\.{ext}$'.format(hazard=self.hazard, ext=ext)):
    #
    #         yield ('day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard}'
    #                '{extension}'.format(extension=ext, **format_dict))

    def acquire_resource(self, target_path, format_dict):
        from zipfile import ZipFile

        target_dir = os.path.dirname(target_path)
        if not os.path.isdir(target_dir):
            os.makedirs(target_dir)

        url = self.url(format_dict)

        shapefile_online = self._urlopen(url)

        zfh = ZipFile(six.BytesIO(shapefile_online.read()), 'r')

        for member_path in zfh.infolist():
            if re.search('{hazard}'.format(hazard=format_dict['hazard']), member_path.filename):
                ext = os.path.splitext(member_path.filename)[1]
                target = os.path.splitext(target_path)[0] + ext
                member = member_path
                with open(target, 'wb') as fh:
                    fh.write(zfh.open(member).read())

        shapefile_online.close()
        zfh.close()

        return target_path

    @staticmethod
    def default_downloader():
        """
        Return a generic, standard, Day2OutlookShpDownloader instance.

        """
        default_spec = ('shapefiles', 'SPC', '{product}', '{year:4d}',
                        'day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard}.shp')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return Day2OutlookShpDownloader(target_path_template=co_path_template,
                                        pre_downloaded_path_template=pre_path_template)


# add a generic SPC Convective Outlook shapefile downloader to the config dictionary's
# 'downloaders' section.
_day1_co_key = ('shapefiles', 'Day1Outlook')
_day2_co_key = ('shapefiles', 'Day2Outlook')
config['downloaders'].setdefault(_day1_co_key, Day1OutlookShpDownloader.default_downloader())
config['downloaders'].setdefault(_day2_co_key, Day2OutlookShpDownloader.default_downloader())