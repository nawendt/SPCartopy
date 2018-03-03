"""
This module contains custom extensions to download and process SPC shapefiles.

"""

import os

import six

from cartopy.io import Downloader
from cartopy.io.shapereader import Reader
from cartopy import config


def convective_outlook(fday, ftime, year, month, day, product):
    """
    Return the path to the requested SPC Convective Outlook shapefile,
    downloading and unzipping if necessary.

    """
    outlook_downloader = Downloader.from_config(('shapefiles', 'convective_outlook',
                                                 fday, ftime, year, month, day,
                                                 product))
    format_dict = {'config': config, 'fday': fday, 'ftime': ftime, 'year': year,
                   'month': month, 'day': day, 'product': product}

    return outlook_downloader.path(format_dict)


class OutlookShpDownloader(Downloader):
    """
    Specialises :class:`cartopy.io.Downloader` to download the zipped
    SPC forecast shapefiles and extract them to the defined location
    (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``category``, ``resolution`` and ``name``.

    """

    FORMAT_KEYS = ('config', 'product', 'fday', 'ftime', 'year', 'month', 'day')

    _SPC_URL_TEMPLATE = ('http://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
                         '/day{fday}otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}-shp.zip')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super(OutlookShpDownloader, self).__init__(url_template, target_path_template,
                                                   pre_downloaded_path_template)

    def zip_file_contents(self, format_dict):
        for ext in ['.shp', '.dbf', '.shx', '.prj']:
            yield ('day{fday}otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{product}'
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
        Return a generic, standard, OutlookShpDownloader instance.

        """
        default_spec = ('shapefiles', 'convective_outlook', '{year:4d}',
                        'day{fday}otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{product}.shp')
        co_path_template = os.path.join('{config[data_dir]}', *default_spec)
        pre_path_template = os.path.join('{config[pre_existing_data_dir]}',
                                         *default_spec)

        return OutlookShpDownloader(target_path_template=co_path_template,
                                    pre_downloaded_path_template=pre_path_template)


# add a generic SPC Convective Outlook shapefile downloader to the config dictionary's
# 'downloaders' section.
_co_key = ('shapefiles', 'convective_outlook')
config['downloaders'].setdefault(_co_key, OutlookShpDownloader.default_downloader())
