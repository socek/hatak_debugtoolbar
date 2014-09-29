# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'hatak>=0.2',
    'pyramid_debugtoolbar',
]

if __name__ == '__main__':
    setup(
        name='Hatak_DebugToolBar',
        version='0.1',
        description='Debug Tool Bar plugin for Hatak.',
        license='Apache License 2.0',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        namespace_packages=['haplugin'],
        install_requires=install_requires,
        include_package_data=True,
        zip_safe=False,
    )
