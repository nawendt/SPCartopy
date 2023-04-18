# Copyright (c) 2023 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""SPC Product Colors."""


class Outlooks:
    """Base class for SPC outlook colors."""

    categorical = {
        'HIGH': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': 'High', },
        'MDT': {'ec': '#CC0000', 'fc': '#E06666', 'label': 'Moderate', },
        'ENH': {'ec': '#FF6600', 'fc': '#FFA366', 'label': 'Enhanced', },
        'SLGT': {'ec': '#DDAA00', 'fc': '#FFE066', 'label': 'Slight', },
        'MRGL': {'ec': '#005500', 'fc': '#66A366', 'label': 'Marginal', },
        'TSTM': {'ec': '#55BB55', 'fc': '#C1E9C1', 'label': 'Thunder', },
    }

    tornado = {
        'SIGN': {'ec': '#000000', 'fc': '#888888', 'label': '10% Sig.', },
        '0.60': {'ec': '#2952a3', 'fc': '#5c85d6', 'label': '60%', },
        '0.45': {'ec': '#a300cc', 'fc': '#d633ff', 'label': '45%', },
        '0.30': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': '30%', },
        '0.15': {'ec': '#CC0000', 'fc': '#E06666', 'label': '15%', },
        '0.10': {'ec': '#DDAA00', 'fc': '#FFE066', 'label': '10%', },
        '0.05': {'ec': '#70380f', 'fc': '#9d4e15', 'label': '5%', },
        '0.02': {'ec': '#005500', 'fc': '#66A366', 'label': '2%', },
    }

    wind = {
        'SIGN': {'ec': '#000000', 'fc': '#888888', 'label': '10% Sig.', },
        '0.60': {'ec': '#a300cc', 'fc': '#d633ff', 'label': '60%', },
        '0.45': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': '45%', },
        '0.30': {'ec': '#CC0000', 'fc': '#E06666', 'label': '30%', },
        '0.15': {'ec': '#DDAA00', 'fc': '#FFE066', 'label': '15%', },
        '0.05': {'ec': '#70380f', 'fc': '#9d4e15', 'label': '5%', },
    }

    hail = {
        'SIGN': {'ec': '#000000', 'fc': '#888888', 'label': '10% Sig.', },
        '0.60': {'ec': '#a300cc', 'fc': '#d633ff', 'label': '60%', },
        '0.45': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': '45%', },
        '0.30': {'ec': '#CC0000', 'fc': '#E06666', 'label': '30%', },
        '0.15': {'ec': '#DDAA00', 'fc': '#FFE066', 'label': '15%', },
        '0.05': {'ec': '#70380f', 'fc': '#9d4e15', 'label': '5%', },
    }

    any_severe = {
        'SIGN': {'ec': '#000000', 'fc': '#888888', 'label': '10% Sig.', },
        '0.60': {'ec': '#a300cc', 'fc': '#d633ff', 'label': '60%', },
        '0.45': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': '45%', },
        '0.30': {'ec': '#CC0000', 'fc': '#E06666', 'label': '30%', },
        '0.15': {'ec': '#DDAA00', 'fc': '#FFE066', 'label': '15%', },
        '0.05': {'ec': '#70380f', 'fc': '#9d4e15', 'label': '5%', },
    }

    extended_severe = {
        '0.30': {'ec': '#FF6600', 'fc': '#FFA366', 'label': '30%', },
        '0.15': {'ec': '#DDAA00', 'fc': '#FFE066', 'label': '15%', },
    }

    fire_weather_categorical = {
        'EXTM': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': 'Extreme', },
        'CRIT': {'ec': '#cc0000', 'fc': '#ff3333', 'label': 'Critical', },
        'ELEV': {'ec': '#e68a00', 'fc': '#ffad33', 'label': 'Elevated', },
        'SDRT': {'ec': '#cc0000', 'fc': 'none', 'label': 'Scattered Dry Thunderstorm', },
        'IDRT': {'ec': '#70380f', 'fc': 'none', 'label': 'Isolated Dry Thunderstorm', },
        # 'SDRT': {'ec': '#cc0000', 'fc': '#ff3333', 'label': 'Scattered Dry Thunderstorm', },
        # 'IDRT': {'ec': '#70380f', 'fc': '#9d4e15', 'label': 'Isolated Dry Thunderstorm', },
    }

    extended_fire_weather_categorical = {
        'D3': {'ec': '#CC00CC', 'fc': '#EE99EE', 'label': 'Day 3 Critical', },
        'D4': {'ec': '#cc0000', 'fc': '#ff3333', 'label': 'Day 4 Critical', },
        'D5': {'ec': '#a300cc', 'fc': '#d633ff', 'label': 'Day 5 Critical', },
        'D6': {'ec': '#005500', 'fc': '#66A366', 'label': 'Day 6 Critical', },
        'D7': {'ec': '#2952a3', 'fc': '#5c85d6', 'label': 'Day 7 Critical', },
        'D8': {'ec': '#70380f', 'fc': '#9d4e15', 'label': 'Day 8 Critical', },
    }

    extended_fire_weather_probability = {
        'WINDRH_0.70': {'ec': '#cc0000', 'fc': '#ff3333', 'label': '70% Critical Wind & RH', },
        'WINDRH_0.40': {'ec': '#e68a00', 'fc': '#ffad33', 'label': '40% Critical Wind & RH', },
        'DRYT_0.40': {'ec': '#00b2ee', 'fc': '#80ffff',
                      'label': '40% Critical Dry Thunderstorm', },
        'DRYT_0.10': {'ec': '#8b4726', 'fc': '#c5a393',
                      'label': '10% Critical Dry Thunderstorm', },
    }
