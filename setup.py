'''
Setup script for BatchY.
'''

import setuptools

from batchy import __project__, __version__, CLI

README = 'README.md'


setuptools.setup(name=__project__,
                 version=__version__,

                 description='Batch YAML Editing.',
                 url="https://github.com/jkloo/BatchY",

                 author='Jeff Kloosterman',
                 author_email='kloosterman.jeff@gmail.com',

                 packages=setuptools.find_packages(),

                 entry_points={'console_scripts': [CLI + ' = batchy.cli:main']},
                 license='MIT',

                 long_description=open(README).read(),
                 install_requires=['PyYAML']
                 )
