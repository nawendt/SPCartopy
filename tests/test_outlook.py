# Copyright (c) 2025 Nathan Wendt.
# Distributed under the terms of the BSD 3-Clause License.
# SPDX-License-Identifier: BSD-3-Clause
"""Test downloading and plotting outlooks."""

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pytest

from spcartopy.feature import Day1ConvectiveOutlookFeature, Day1FireOutlookFeature
import spcartopy.legends as spclegends

PROJ = ccrs.LambertConformal(
    central_longitude=-95, central_latitude=0, standard_parallels=(33, 45)
)


@pytest.mark.filterwarnings('ignore:Downloading')
@pytest.mark.mpl_image_compare(remove_text=True, tolerance=0.)
def test_convective_outlook():
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

    cof = Day1ConvectiveOutlookFeature(1630, 2020, 4, 12, 'cat', zorder=3, linewidth=1.5)
    ax.add_feature(cof)

    leg = spclegends.convective_categorical()
    lax = ax.legend(*leg, loc=3, ncol=2, framealpha=1, fontsize=8, edgecolor='black')
    lax.get_frame().set_linewidth(2)

    return fig


@pytest.mark.filterwarnings('ignore:Downloading')
@pytest.mark.mpl_image_compare(remove_text=True, tolerance=0.)
def test_fire_outlook():
    """Test retrieving fire outlooks from SPC archive."""
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

    windrh = Day1FireOutlookFeature(1700, 2022, 9, 7, 'windrh', zorder=3)
    dryt = Day1FireOutlookFeature(1700, 2022, 9, 7, 'dryt', zorder=3.1)
    ax.add_feature(windrh)
    ax.add_feature(dryt)

    leg = spclegends.fire_categorical()
    lax = ax.legend(*leg, loc=3, ncol=2, framealpha=1, fontsize=6, edgecolor='black')
    lax.get_frame().set_linewidth(2)

    return fig
