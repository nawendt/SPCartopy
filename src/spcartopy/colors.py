# Copyright (c) 2026 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""SPC Product Colors."""


class Outlooks:
    """Base class for SPC outlook colors."""

    categorical = {
        'HIGH': {
            'ec': '#CC00CC',
            'fc': '#EE99EE',
            'label': 'High',
        },
        'MDT': {
            'ec': '#CC0000',
            'fc': '#E06666',
            'label': 'Moderate',
        },
        'ENH': {
            'ec': '#FF6600',
            'fc': '#FFA366',
            'label': 'Enhanced',
        },
        'SLGT': {
            'ec': '#DDAA00',
            'fc': '#FFE066',
            'label': 'Slight',
        },
        'MRGL': {
            'ec': '#005500',
            'fc': '#66A366',
            'label': 'Marginal',
        },
        'TSTM': {
            'ec': '#55BB55',
            'fc': '#C1E9C1',
            'label': 'Thunder',
        },
    }

    tornado = {
        'CIG1': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 1'},
        'CIG2': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 2'},
        'CIG3': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 3'},
        'SIGN': {
            'ec': '#000000',
            'fc': '#888888',
            'label': '10% Sig.',
        },
        '0.60': {
            'ec': '#104E8B',
            'fc': '#104E8B',
            'label': '60%',
        },
        '0.45': {
            'ec': '#912CEE',
            'fc': '#C896F7',
            'label': '45%',
        },
        '0.30': {
            'ec': '#FF00FF',
            'fc': '#FF80FF',
            'label': '30%',
        },
        '0.15': {
            'ec': '#FF0000',
            'fc': '#FF8080',
            'label': '15%',
        },
        '0.10': {
            'ec': '#FD8A2B',
            'fc': '#FFE481',
            'label': '10%',
        },
        '0.05': {
            'ec': '#7F3F27',
            'fc': '#BD998A',
            'label': '5%',
        },
        '0.02': {
            'ec': '#1A731D',
            'fc': '#79BA7A',
            'label': '2%',
        },
    }

    wind = {
        'CIG1': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 1'},
        'CIG2': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 2'},
        'CIG3': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 3'},
        'SIGN': {
            'ec': '#000000',
            'fc': '#888888',
            'label': '10% Sig.',
        },
        '0.90': {'ec': '#5c85d6', 'fc': '#1affff', 'label': '90%'},
        '0.75': {'ec': '#2952a3', 'fc': '#5c85d6', 'label': '75%'},
        '0.60': {
            'ec': '#a300cc',
            'fc': '#d633ff',
            'label': '60%',
        },
        '0.45': {
            'ec': '#CC00CC',
            'fc': '#EE99EE',
            'label': '45%',
        },
        '0.30': {
            'ec': '#CC0000',
            'fc': '#E06666',
            'label': '30%',
        },
        '0.15': {
            'ec': '#FF9600',
            'fc': '#FFEB7F',
            'label': '15%',
        },
        '0.05': {
            'ec': '#8B4726',
            'fc': '#C5A392',
            'label': '5%',
        },
    }

    hail = {
        'CIG1': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 1'},
        'CIG2': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 2'},
        'SIGN': {
            'ec': '#000000',
            'fc': '#888888',
            'label': '10% Sig.',
        },
        '0.60': {
            'ec': '#912CEE',
            'fc': '#C895F6',
            'label': '60%',
        },
        '0.45': {
            'ec': '#FF00FF',
            'fc': '#FF7FFF',
            'label': '45%',
        },
        '0.30': {
            'ec': '#FF0000',
            'fc': '#FF7F7F',
            'label': '30%',
        },
        '0.15': {
            'ec': '#FF9600',
            'fc': '#FFEB7F',
            'label': '15%',
        },
        '0.05': {
            'ec': '#8B4726',
            'fc': '#C5A392',
            'label': '5%',
        },
    }

    any_severe = {
        'CIG1': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 1'},
        'CIG2': {'ec': '#000000', 'fc': 'none', 'label': 'Intensity Level 2'},
        'SIGN': {
            'ec': '#000000',
            'fc': '#888888',
            'label': '10% Sig.',
        },
        '0.60': {
            'ec': '#912CEE',
            'fc': '#C895F6',
            'label': '60%',
        },
        '0.45': {
            'ec': '#FF00FF',
            'fc': '#FF7FFF',
            'label': '45%',
        },
        '0.30': {
            'ec': '#FF0000',
            'fc': '#FF7F7F',
            'label': '30%',
        },
        '0.15': {
            'ec': '#FF9600',
            'fc': '#FFEB7F',
            'label': '15%',
        },
        '0.05': {
            'ec': '#8B4726',
            'fc': '#C5A392',
            'label': '5%',
        },
    }

    extended_severe = {
        '0.30': {
            'ec': '#FF9600',
            'fc': '#FFEB7F',
            'label': '30%',
        },
        '0.15': {
            'ec': '#EE8232',
            'fc': '#E6C280',
            'label': '15%',
        },
    }

    fire_weather_categorical = {
        'EXTM': {
            'ec': '#FF0000',
            'fc': '#FF80FF',
            'label': 'Extreme',
        },
        'CRIT': {
            'ec': '#FF0000',
            'fc': '#FF8080',
            'label': 'Critical',
        },
        'ELEV': {
            'ec': '#FF7F00',
            'fc': '#FFBF80',
            'label': 'Elevated',
        },
        'SDRT': {
            'ec': '#4B0082',
            'fc': '#d18cff',
            'label': 'Scattered Dry Thunderstorm',
        },
        'IDRT': {
            'ec': '#8B4726',
            'fc': '#C5A393',
            'label': 'Isolated Dry Thunderstorm',
        },
    }

    extended_fire_weather_categorical = {
        'D3': {
            'ec': '#CC00CC',
            'fc': '#EE99EE',
            'label': 'Day 3 Critical',
        },
        'D4': {
            'ec': '#cc0000',
            'fc': '#ff3333',
            'label': 'Day 4 Critical',
        },
        'D5': {
            'ec': '#a300cc',
            'fc': '#d633ff',
            'label': 'Day 5 Critical',
        },
        'D6': {
            'ec': '#005500',
            'fc': '#66A366',
            'label': 'Day 6 Critical',
        },
        'D7': {
            'ec': '#2952a3',
            'fc': '#5c85d6',
            'label': 'Day 7 Critical',
        },
        'D8': {
            'ec': '#70380f',
            'fc': '#9d4e15',
            'label': 'Day 8 Critical',
        },
    }

    extended_fire_weather_probability = {
        'WINDRH_0.70': {
            'ec': '#FF0000',
            'fc': '#FF8080',
            'label': '70% Critical Wind & RH',
        },
        'WINDRH_0.40': {
            'ec': '#FF7F00',
            'fc': '#FFBF80',
            'label': '40% Critical Wind & RH',
        },
        'DRYT_0.40': {
            'ec': '#4B0082',
            'fc': '#d18cff',
            'label': '40% Critical Dry Thunderstorm',
        },
        'DRYT_0.10': {
            'ec': '#8B4726',
            'fc': '#C5A393',
            'label': '10% Critical Dry Thunderstorm',
        },
    }
