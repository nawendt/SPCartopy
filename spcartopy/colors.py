"""
This module contains common SPC colors for outlooks

"""


def scale_rgb(rgb_list):
    return {key: tuple([color / 255 for color in rgb]) for key, rgb in rgb_list.items()}


_catRGB = {2: (193, 233, 193),  # Thunder
           3: (0, 176, 80),     # Marginal
           4: (255, 255, 0),    # Slight
           5: (255, 163, 41),   # Enhanced
           6: (255, 0, 0),      # Moderate
           8: (255, 0, 255)}    # High

cat_colors = scale_rgb(_catRGB)

_hailRGB = {5: (139, 71, 38),   # 5%
            15: (255, 200, 0),   # 15%
            30: (255, 0, 0),     # 30%
            45: (255, 0, 255),   # 45%
            60: (145, 44, 238)}  # 60%

hail_colors = scale_rgb(_hailRGB)

_sigRGB = {10: (0, 0, 0),}

sig_colors = scale_rgb(_sigRGB)

_tornRGB  = {2: (0, 139, 0),     # 2%
            5: (139, 71, 38),   # 5%
            10: (255, 200, 0),   # 10%
            15: (255, 0, 0),     # 15%
            30: (255, 0, 255),   # 30%
            45: (145, 44, 238),  # 45%
            60: (16, 78, 139)}   # 60%

torn_colors = scale_rgb(_tornRGB)

_windRGB = {5: (139, 71, 38),   # 5%
            15: (255, 200, 0),   # 15%
            30: (255, 0, 0),     # 30%
            45: (255, 0, 255),   # 45%
            60: (145, 44, 238)}  # 60%

wind_colors = scale_rgb(_windRGB)
