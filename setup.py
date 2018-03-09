from setuptools import setup

setup(
    name='SPCartopy',
    version='0.1.0',
    packages=['spcartopy'],
    py_modules=['spcartopy.io', 'spcartopy.mpl'],
    url='https://github.com/nawendt/SPCartopy',
    license='BSD-3',
    author='Nathan Wendt',
    author_email='nawendt@ou.edu',
    description='Add SPC features to cartopy maps',
    install_requires=['cartopy', 'matplotlib', 'six'],
)
