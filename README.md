# SPCartopy
Plot SPC products using simple cartopy and matplotlib syntax

#### What is SPCartopy?
SPCartopy was created to make retriving and plotting certain Storm Prediction Center ([SPC](https://www.spc.noaa.gov)) products easy. The package uses the Python map plotting package [cartopy](https://scitools.org.uk/cartopy/docs/latest) as a foundation and extends some of its classes. Convective/fire weather outlooks and MDs are the products currently supported.

#### How do I install it?
First, you need python. The easiest way to get it is to use something like [miniconda](https://docs.conda.io/en/latest/miniconda.html). Once you have python, you need to have cartopy, fiona, and matplotlib installed. Then, just download this repository, use your terminal to navigate to the package folder, and run the following command:
```shell
python setup.py install
# or
pip install .
```

#### How do I use SPCartopy?
As SPCartopy simply extends the `cartopy.feature.Feature` class, it is about as easy as using the `NaturalEarthFeature` (a common way of adding basic map elements). A [tutorial](tutorials/spcartopy.ipynb) is included in this repository that includes several practical examples to help you get started.

#### Will new features be added?
Possibly. The originally intended functionality is there, but other SPC products may be added in the future.

#### Can I contribute?
Absolutely. Whether you have something you would like to plot and want to help add the functionality or if you just use the package and report issues, all will be helpful.
