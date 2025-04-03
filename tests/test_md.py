# Copyright (c) 2025 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Test downloading and plotting MDs."""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pytest

from spcartopy.feature import MDFeature

PROJ = ccrs.LambertConformal(
    central_longitude=-95, central_latitude=0, standard_parallels=(33, 45)
)


@pytest.mark.filterwarnings('ignore:Downloading')
@pytest.mark.mpl_image_compare(remove_text=True, tolerance=0.)
def test_md():
    """Test retrieving convective outlooks from SPC archive."""
    fig, ax = plt.subplots(subplot_kw={'projection': PROJ})

    ax.add_feature(
        cfeature.NaturalEarthFeature(
            category='cultural',
            name='admin_1_states_provinces_lines',
            scale='50m',
            facecolor='none',
            edgecolor='black',
            linewidth=0.5,
        ), zorder=4)

    ax.add_feature(
        cfeature.NaturalEarthFeature(
            category='physical',
            name='lakes',
            scale='110m',
            facecolor='none',
            edgecolor='black',
            linewidth=0.5
        ), zorder=4)

    ax.add_feature(
        cfeature.NaturalEarthFeature(
            category='physical',
            name='coastline',
            scale='50m',
            facecolor='none',
            edgecolor='black'
        ), zorder=4)

    ax.add_feature(
        cfeature.NaturalEarthFeature(
            category='cultural',
            name='admin_0_boundary_lines_land',
            scale='50m',
            facecolor='none',
            edgecolor='black'
        ), zorder=3)

    ax.set_extent((-122, -72, 22, 50))

    for n in range(388, 428):
        md = MDFeature(2023, n, edgecolor='#000000', facecolor='#999999', alpha=0.2, zorder=3)
        ax.add_feature(md)

    return fig
