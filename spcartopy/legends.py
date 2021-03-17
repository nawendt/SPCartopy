"""
Module containing legend objects for plotting.

"""

from matplotlib.patches import Rectangle

from spcartopy.colors import Outlooks


class SPCLegend(object):
    """
    SPC Legends

    """

    @classmethod
    def convectiveAllHazards(cls):
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

        return tuple([handles, labels])

    @classmethod
    def convectiveCategorical(cls):
        handles = []
        labels = []
        for _cat, props in Outlooks.categorical.items():
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
            labels.append(props['label'])

        return tuple([handles, labels])

    @classmethod
    def convectiveExtended(cls):
        handles = []
        labels = []
        for _cat, props in Outlooks.extended_severe.items():
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
            labels.append(props['label'])

        return tuple([handles, labels])

    @classmethod
    def convectiveHail(cls):
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

        return tuple([handles, labels])

    @classmethod
    def convectiveTornado(cls):
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

        return tuple([handles, labels])

    @classmethod
    def convectiveWind(cls):
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

        return tuple([handles, labels])

    @classmethod
    def fireCategorical(cls):
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

        return tuple([handles, labels])

    @classmethod
    def extendedFireCategorical(cls):
        handles = []
        labels = []
        for _cat, props in Outlooks.extended_fire_weather_categorical.items():
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
            labels.append(props['label'])

        return tuple([handles, labels])

    @classmethod
    def extendedFireProbability(cls):
        handles = []
        labels = []
        for _cat, props in Outlooks.extended_fire_weather_probability.items():
            handles.append(Rectangle((0, 0), 3, 2, ec=props['ec'],
                                     fc=props['fc']))
            labels.append(props['label'])

        return tuple([handles, labels])
