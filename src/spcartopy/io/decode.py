# Copyright (c) 2023 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Decoding tools."""

import re


def decode_coords(coord_string):
    """Decode coordinates.

    Parameters
    ----------
    coord_string : str
        Longitude and latitude string from
        the MCD LAT...LON section.

    Returns
    -------
    lon, lat: tuple of float
        Decoded longitude and latitude.
    """
    slat = coord_string[:4]
    slon = coord_string[4:]

    lat = int(slat) / 100

    if int(slon) < 3000:
        lon = -int(f'1{slon}') / 100
    else:
        lon = -int(slon) / 100

    return (lon, lat)


def mcd_to_geojson(mcd_text):
    """Parse MCD and output to geoJSON.

    Parameters
    ----------
    mcd_text : str or bytes
        Raw MCD text.

    Returns
    -------
    geoJSON object
    """
    parse_coords = re.compile(r'(?:LAT\.\.\.LON)\s+(?P<coords>(?:\d{8}[\s\n]*)+)')
    parse_md_number = re.compile(r'Mesoscale Discussion (?P<mdnum>\d{4})')

    try:
        text = mcd_text.decode('utf-8', 'ignore')
    except AttributeError:
        text = mcd_text

    md_number_txt = parse_md_number.search(text).groupdict()['mdnum']
    md_number = int(md_number_txt)

    coords_txt = parse_coords.search(text).groupdict()['coords']
    coords_list = coords_txt.replace('\n', '').split()
    coords_pts = [decode_coords(x) for x in coords_list]

    md_feature = {
        'type': 'Feature',
        'properties': {
            'number': md_number
        },
        'geometry': {
            'type': 'Polygon',
            'coordinates': [coords_pts],
        }
    }

    return {
        'type': 'FeatureCollection',
        'features': [md_feature],
    }
