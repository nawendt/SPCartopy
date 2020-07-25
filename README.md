# SPCartopy
Plot SPC products using simple cartopy and matplotlib syntax

#### What is SPCartopy?
SPCartopy was created to make retriving and plotting certain Storm Prediction Center ([SPC](https://www.spc.noaa.gov)) products easy. The package uses the Python map plotting package [cartopy](https://scitools.org.uk/cartopy/docs/latest) as a foundation and extends some of its classes. In its current states, only convective outlooks and probabilistic severe weather forecasts are supported.

#### How do I use SPCartopy?
As SPCartopy simply extends the `cartopy.feature.Feature` class, it is about as easy as using the `NaturalEarthFeature` that is the most common way of adding basic map elements. A [tutorial](tutorials/spcartopy.ipynb) is included in this repository that includes several practical examples to help you get started.

#### Will new features be added?
That is the plan. The expectation is to add fire weather outlooks once they get a geoJSON format. Other SPC products may be added in the future.

#### Can I contribute?
Absolutely. Whether you have something you would like to plot and want to help add the functionality or if you just use the package and report issues, all will be helpful.