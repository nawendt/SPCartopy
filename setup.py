from setuptools import convert_path, setup
import os


def find_package_tree(root_path, root_package):
    """
    Return the package and all its sub-packages.
    Automated package discovery - extracted/modified from Distutils Cookbook:
    https://wiki.python.org/moin/Distutils/Cookbook/AutoPackageDiscovery
    """
    packages = [root_package]
    # Accept a root_path with Linux path separators.
    root_path = root_path.replace('/', os.path.sep)
    root_count = len(root_path.split(os.path.sep))
    for (dir_path, dir_names, _) in os.walk(convert_path(root_path)):
        # Prune dir_names *in-place* to prevent unwanted directory recursion
        for dir_name in list(dir_names):
            if not os.path.isfile(os.path.join(dir_path, dir_name,
                                               '__init__.py')):
                dir_names.remove(dir_name)
        if dir_names:
            prefix = dir_path.split(os.path.sep)[root_count:]
            packages.extend(['.'.join([root_package] + prefix + [dir_name])
                             for dir_name in dir_names])
    return packages


setup(
    name='SPCartopy',
    version='1.0.0',
    packages=find_package_tree('spcartopy', 'spcartopy'),
    url='https://github.com/nawendt/SPCartopy',
    license='BSD-3',
    author='Nathan Wendt',
    author_email='nathan.wendt@noaa.gov',
    description='Add SPC features to cartopy maps',
    install_requires=['cartopy', 'fiona', 'matplotlib'],
)
