# import cartopy.mpl.geoaxes
# import matplotlib.axes
# from spcartopy.mpl import feature_artist
#
#
# class GeoAxes(cartopy.mpl.geoaxes.GeoAxes):
#     """
#     A subclass of :class:`matplotlib.axes.Axes` which represents a
#     map :class:`~cartopy.crs.Projection`.
#     This class replaces the Matplotlib :class:`~matplotlib.axes.Axes` class
#     when created with the *projection* keyword. For example::
#         # Set up a standard map for latlon data.
#         geo_axes = pyplot.axes(projection=cartopy.crs.PlateCarree())
#         # Set up an OSGB map.
#         geo_axes = pyplot.subplot(2, 2, 1, projection=cartopy.crs.OSGB())
#     When a source projection is provided to one of it's plotting methods,
#     using the *transform* keyword, the standard Matplotlib plot result is
#     transformed from source coordinates to the target projection. For example::
#         # Plot latlon data on an OSGB map.
#         pyplot.axes(projection=cartopy.crs.OSGB())
#         pyplot.contourf(x, y, data, transform=cartopy.crs.PlateCarree())
#
#     """
#
#     def add_feature(self, feature, **kwargs):
#         """
#         Add the given :class:`~cartopy.feature.Feature` instance to the axes.
#         Parameters
#         ----------
#         feature
#             An instance of :class:`~cartopy.feature.Feature`.
#         Returns
#         -------
#         A :class:`cartopy.mpl.feature_artist.FeatureArtist` instance
#             The instance responsible for drawing the feature.
#         Note
#         ----
#             Matplotlib keyword arguments can be used when drawing the feature.
#             This allows standard Matplotlib control over aspects such as
#             'facecolor', 'alpha', etc.
#
#         """
#         # Instantiate an artist to draw the feature and add it to the axes.
#         artist = feature_artist.FeatureArtist(feature, **kwargs)
#         return self.add_artist(artist)
#
# # Define the GeoAxesSubplot class, so that a type(ax) will emanate from
# # spcartopy.mpl.geoaxes, not matplotlib.axes.
# GeoAxesSubplot = matplotlib.axes.subplot_class_factory(GeoAxes)
# GeoAxesSubplot.__module__ = GeoAxes.__module__
