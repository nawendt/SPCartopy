# Copyright (c) 2023 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Helper function for generating legends for SPC outlook plots."""

from matplotlib.patches import Rectangle

from spcartopy.colors import Outlooks


def convectiveAllHazards():
    """Legend for all hazards probabilistic outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.hail.items():
        if _cat == 'SIGN':
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc='none', hatch='SS'))
        else:
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def convectiveCategorical():
    """Legend for categorical convective outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.categorical.items():
        handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                 fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def convectiveExtended():
    """Legend for extended convective outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.extended_severe.items():
        handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                 fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def convectiveHail():
    """Legend for probabilistic hail outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.hail.items():
        if _cat == 'SIGN':
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc='none', hatch='SS'))
        else:
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def convectiveTornado():
    """Legend for probabilistic tornado outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.tornado.items():
        if _cat == 'SIGN':
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc='none', hatch='SS'))
        else:
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def convectiveWind():
    """Legend for probabilistic wind outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.wind.items():
        if _cat == 'SIGN':
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc='none', hatch='SS'))
        else:
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def fireCategorical():
    """Legend for categorical fire outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.fire_weather_categorical.items():
        if _cat in ['IDRT', 'SDRT']:
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc'], hatch='xx'))
        else:
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def extendedFireCategorical():
    """Legend for extended fire outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.extended_fire_weather_categorical.items():
        handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                 fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)


def extendedFireProbability():
    """Legend for fire probabilistic outlook."""
    handles = []
    labels = []
    for _cat, props in Outlooks.extended_fire_weather_probability.items():
        handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                 fc=props['fc']))
        labels.append(props['label'])

    return (handles, labels)
