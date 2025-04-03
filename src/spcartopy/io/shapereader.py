# Copyright (c) 2025 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Custom extensions to download and process SPC geoJSON files."""

from pathlib import Path

from cartopy import config
from cartopy.io import Downloader
from cartopy.io.shapereader import FionaReader, FionaRecord


def spc_convective(fday, ftime, year, month, day, hazard, product):
    """Return the path to the requested SPC Convective Outlook geoJSON."""
    outlook_downloader = Downloader.from_config(
        ('geoJSON', f'Day{fday:1d}Outlook',
         fday, ftime, year, month, day, hazard, product)
    )
    format_dict = {'config': config, 'ftime': ftime, 'year': year,
                   'month': month, 'day': day, 'hazard': hazard,
                   'product': product}

    return outlook_downloader.path(format_dict)


def spc_fire(fday, ftime, year, month, day, hazard, product):
    """Return the path to the requested SPC Fire Outlook geoJSON."""
    outlook_downloader = Downloader.from_config(
        ('geoJSON', f'Day{fday:1d}Fire',
         fday, ftime, year, month, day, hazard, product)
    )
    format_dict = {'config': config, 'ftime': ftime, 'year': year,
                   'month': month, 'day': day, 'hazard': hazard,
                   'product': product}

    return outlook_downloader.path(format_dict)


class SPCReader(FionaReader):
    """Read and filter SPC geoJSON files."""

    def __init__(self, filename, bbox=None):
        super().__init__(filename, bbox)

    def geometries(self, filter_keys=None):
        """Get SPC outlook geometries.

        Overrides `FionaReader.geometries` so that specified geomtries can be
        filtered based on record attributes.

        Parameters
        ----------
        filter_keys : dict
            A dictionary containing key:value pairs used to filter geometries.
        """
        if filter_keys is None:
            filter_keys = {}

        for item in self._data:
            if any(item[key] == value for key, value in filter_keys.items()):
                continue
            else:
                yield item['geometry']

    def records(self, filter_keys=None):
        """Get SPC outlook records.

        Overrides `FionaReader.records` so that specified records can be
        filtered based on record attributes.

        Parameters
        ----------
        filter_keys : dict
            A dictionary containing key:value pairs used to filter records.

        """
        if filter_keys is None:
            filter_keys = {}

        for item in self._data:
            if any(item[key] == value for key, value in filter_keys.items()):
                continue
            else:
                yield FionaRecord(item['geometry'],
                                  {key: value for key, value in
                                  item.items() if key != 'geometry'})


class ConvectiveOutlookDownloader(Downloader):
    """SPC convectie outlook downloader.

    Base class that extends `cartopy.io.Downloader` for SPC convective outlooks.
    """

    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template,
                 target_path_template,
                 pre_downloaded_path_template,
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    def acquire_resource(self, target_path, format_dict):
        """Download resource."""
        target_dir = Path(target_path).parent
        target_dir.mkdir(parents=True, exist_ok=True)

        url = self.url(format_dict)

        geojson_response = self._urlopen(url)

        with open(target_path, 'wb') as fh:
            fh.write(geojson_response.read())

        return target_path


class FireOutlookDownloader(Downloader):
    """SPC fire weather outlook downloader.

    Base class that extends `cartopy.io.Downloader` for SPC fire outlooks.
    """

    FORMAT_KEYS = ('config', 'hazard', 'ftime', 'year', 'month', 'day', 'product')

    def __init__(self,
                 url_template,
                 target_path_template,
                 pre_downloaded_path_template,
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    def acquire_resource(self, target_path, format_dict):
        """Download resource."""
        target_dir = Path(target_path).parent
        target_dir.mkdir(parents=True, exist_ok=True)

        url = self.url(format_dict)

        geojson_response = self._urlopen(url)

        with open(target_path, 'wb') as fh:
            fh.write(geojson_response.read())

        return target_path


class Day1OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 1 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 1 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
        '/day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1OutlookDownloader instance."""
        default_spec = (
            'geoJSON', 'SPC', '{product}', '{year:4d}',
            'day1otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson'
        )
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day1OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day2OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 2 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 2 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
        '/day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day2OutlookDownloader instance."""
        default_spec = (
            'geoJSON', 'SPC', '{product}', '{year:4d}',
            'day2otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson'
        )
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day2OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day3OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 3 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 3 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.

    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/outlook/archive/{year:4d}'
        '/day3otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day3OutlookDownloader instance."""
        default_spec = (
            'geoJSON', 'SPC', '{product}', '{year:4d}',
            'day3otlk_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson'
        )
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day3OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day4OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 4 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 4 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
        '/day4prob_{year:4d}{month:02d}{day:02d}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day4OutlookDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day4otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day4OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day5OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 5 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 5 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
        '/day5prob_{year:4d}{month:02d}{day:02d}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day5OutlookDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day5otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day5OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day6OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 6 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 6 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
        '/day6prob_{year:4d}{month:02d}{day:02d}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day6OutlookDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day6otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day6OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day7OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 7 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 7 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.

    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
        '/day7prob_{year:4d}{month:02d}{day:02d}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day6OutlookDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day7otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day7OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day8OutlookDownloader(ConvectiveOutlookDownloader):
    """Day 8 convective outlook downloader.

    Specializes `spcartopy.io.ConvectiveOutlookDownloader` to download the Day 8 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically ``year``, ``month``, ``day``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/day4-8/archive/{year:4d}'
        '/day8prob_{year:4d}{month:02d}{day:02d}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day8OutlookDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day8otlk_{year:4d}{month:02d}{day:02d}.geojson')
        co_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day8OutlookDownloader(target_path_template=co_path_template,
                                     pre_downloaded_path_template=pre_path_template)


class Day1FireDownloader(FireOutlookDownloader):
    """Day 1 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 1 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/fire_wx/{year:4d}'
        '/day1fw_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day1fw_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day1FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day2FireDownloader(FireOutlookDownloader):
    """Day 2 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 2 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``ftime``, ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/fire_wx/{year:4d}'
        '/day2fw_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day2fw_{year:4d}{month:02d}{day:02d}_{ftime:04d}_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day2FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day3FireDownloader(FireOutlookDownloader):
    """Day 3 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 3 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/fire_wx/{year:4d}'
        '/day3fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day3fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day3FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day4FireDownloader(FireOutlookDownloader):
    """Day 4 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 4 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/fire_wx/{year:4d}'
        '/day4fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.lyr.geojson')

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day4fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day4FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day5FireDownloader(FireOutlookDownloader):
    """Day 5 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 5 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/fire_wx/{year:4d}'
        '/day5fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day5fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day5FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day6FireDownloader(FireOutlookDownloader):
    """Day 6 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 6 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/fire_wx/{year:4d}'
        '/day6fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day6fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day6FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day7FireDownloader(FireOutlookDownloader):
    """Day 7 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 7 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/fire_wx/{year:4d}'
        '/day7fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day7fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day7FireDownloader(target_path_template=fo_path_template,
                                  pre_downloaded_path_template=pre_path_template)


class Day8FireDownloader(FireOutlookDownloader):
    """Day 8 fire outlook downloader.

    Specializes `spcartopy.io.FireOutlookDownloader` to download the Day 8 SPC
    forecast geoJSON files to the defined location (typically user configurable).

    The keys which should be passed through when using the ``format_dict``
    are typically  ``year``, ``month``, ``day`` and ``hazard``.
    """

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/exper/fire_wx/{year:4d}'
        '/day8fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.lyr.geojson'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    @staticmethod
    def default_downloader():
        """Return a generic, standard, Day1FireDownloader instance."""
        default_spec = ('geoJSON', 'SPC', '{product}', '{year:4d}',
                        'day8fw_{year:4d}{month:02d}{day:02d}_1200_{hazard:s}.geojson')
        fo_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return Day8FireDownloader(target_path_template=fo_path_template,
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

_day1_fw_key = ('geoJSON', 'Day1Fire')
_day2_fw_key = ('geoJSON', 'Day2Fire')
_day3_fw_key = ('geoJSON', 'Day3Fire')
_day4_fw_key = ('geoJSON', 'Day4Fire')
_day5_fw_key = ('geoJSON', 'Day5Fire')
_day6_fw_key = ('geoJSON', 'Day6Fire')
_day7_fw_key = ('geoJSON', 'Day7Fire')
_day8_fw_key = ('geoJSON', 'Day8Fire')

config['downloaders'].setdefault(_day1_co_key, Day1OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day2_co_key, Day2OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day3_co_key, Day3OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day4_co_key, Day4OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day5_co_key, Day5OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day6_co_key, Day6OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day7_co_key, Day7OutlookDownloader.default_downloader())
config['downloaders'].setdefault(_day8_co_key, Day8OutlookDownloader.default_downloader())

config['downloaders'].setdefault(_day1_fw_key, Day1FireDownloader.default_downloader())
config['downloaders'].setdefault(_day2_fw_key, Day2FireDownloader.default_downloader())
config['downloaders'].setdefault(_day3_fw_key, Day3FireDownloader.default_downloader())
config['downloaders'].setdefault(_day4_fw_key, Day4FireDownloader.default_downloader())
config['downloaders'].setdefault(_day5_fw_key, Day5FireDownloader.default_downloader())
config['downloaders'].setdefault(_day6_fw_key, Day6FireDownloader.default_downloader())
config['downloaders'].setdefault(_day7_fw_key, Day7FireDownloader.default_downloader())
config['downloaders'].setdefault(_day8_fw_key, Day8FireDownloader.default_downloader())
