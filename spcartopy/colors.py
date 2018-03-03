"""
This module contains common SPC colors for outlooks

"""


def scale_rgb(rgb_list):
    return [tuple([color / 255 for color in rgb]) for rgb in rgb_list]


_catRGB = [(193, 233, 193),  # Thunder
           (0, 176, 80),     # Marginal
           (255, 255, 0),    # Slight
           (255, 163, 41),   # Enhanced
           (255, 0, 0),      # Moderate
           (255, 0, 255)]    # High

cat_colors = scale_rgb(_catRGB)

_legacy_catRGB = [(193, 233, 193),  # Thunder
                  (255, 255, 0),    # Slight
                  (255, 0, 0),      # Moderate
                  (255, 0, 255)]    # High

legacy_cat_colors = scale_rgb(_legacy_catRGB)

_hailRGB = [(139, 71, 38),   # 5%
            (255, 200, 0),   # 15%
            (255, 0, 0),     # 30%
            (255, 0, 255),   # 45%
            (145, 44, 238)]  # 60%

hail_colors = scale_rgb(_hailRGB)

_tornRGB  = [(0, 139, 0),     # 2%
            (139, 71, 38),   # 5%
            (255, 200, 0),   # 10%
            (255, 0, 0),     # 15%
            (255, 0, 255),   # 30%
            (145, 44, 238),  # 45%
            (16, 78, 139)]   # 60%

torn_colors = scale_rgb(_tornRGB)

_windRGB = [(139, 71, 38),   # 5%
            (255, 200, 0),   # 15%
            (255, 0, 0),     # 30%
            (255, 0, 255),   # 45%
            (145, 44, 238)]  # 60%

wind_colors = scale_rgb(_windRGB)
