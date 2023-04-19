# Copyright (c) 2023 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Custom extensions to download and process SPC text files."""

import json
from pathlib import Path

from cartopy import config
from cartopy.io import Downloader

from spcartopy.io.decode import mcd_to_geojson


def MD(year, number):
    """Return the path to the requested SPC mesoscale discussion geoJSON."""
    md_downloader = Downloader.from_config(
        ('geoJSON', 'MD', year, number)
    )
    format_dict = {'config': config, 'year': year, 'number': number}

    return md_downloader.path(format_dict)


class MDDownloader(Downloader):
    """MD Downloader."""

    FORMAT_KEYS = ('config', 'year', 'number')

    _SPC_URL_TEMPLATE = (
        'https://www.spc.noaa.gov/products/md/{year:4d}/md{number:04d}.txt'
    )

    def __init__(self,
                 url_template=_SPC_URL_TEMPLATE,
                 target_path_template=None,
                 pre_downloaded_path_template='',
                 ):
        super().__init__(url_template, target_path_template, pre_downloaded_path_template)

    def acquire_resource(self, target_path, format_dict):
        """Download resource."""
        target_dir = Path(target_path).parent
        target_dir.mkdir(parents=True, exist_ok=True)

        url = self.url(format_dict)

        md_txt = self._urlopen(url)

        with open(target_path, 'w') as fh:
            json.dump(mcd_to_geojson(md_txt.read()), fh)

        return target_path

    @staticmethod
    def default_downloader():
        """Return a generic, standard, MD downloader instance."""
        default_spec = ('geoJSON', 'SPC', 'md', '{year:4d}',
                        'md{number:04d}.geojson')
        md_path_template = str(Path('{config[data_dir]}').joinpath(*default_spec))
        pre_path_template = str(
            Path('{config[pre_existing_data_dir]}').joinpath(*default_spec)
        )

        return MDDownloader(target_path_template=md_path_template,
                            pre_downloaded_path_template=pre_path_template)


_md_key = ('geoJSON', 'MD')

config['downloaders'].setdefault(_md_key, MDDownloader.default_downloader())
