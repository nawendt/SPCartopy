"""
This module contains common SPC colors for outlooks

"""


def scale_rgb(rgb_list):
    return [tuple([color / 255 for color in rgb]) for rgb in rgb_list]

_hailRGB = [(139,71,38),   # 5%
            (255,200,0),   # 15%
            (255,0,0),     # 30%
            (255,0,255),   # 45%
            (145,44,238)]  # 60%

hail_colors = scale_rgb(_hailRGB)
