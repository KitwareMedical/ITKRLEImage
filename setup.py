# -*- coding: utf-8 -*-
from __future__ import print_function
from os import sys

try:
    from skbuild import setup
except ImportError:
    print('scikit-build is required to build from source.', file=sys.stderr)
    print('Please run:', file=sys.stderr)
    print('', file=sys.stderr)
    print('  python -m pip install scikit-build')
    sys.exit(1)

setup(
    name='itk-rleimage',
    version='1.0.0',
    author='Paul A. Yushkevich',
    author_email='pauly2@mail.med.upenn.edu',
    packages=['itk'],
    package_dir={'itk': 'itk'},
    download_url=r'https://github.com/KitwareMedical/ITKRLEImage',
    description=r'ITK classes for run-length encoded memory compression',
    long_description='ITKRLEImage provides run-length encoded storage for'
                     'image content, iterators for efficient reading and'
                     'writing, and a specialization of region of interest'
                     'filter which can also be used to convert to and from'
                     'regular `itk::Image`.',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: C++",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries",
        "Operating System :: Android",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS"
        ],
    license='Apache',
    keywords='ITK InsightToolkit Run-length-encoding',
    url=r'https://github.com/KitwareMedical/ITKRLEImage',
    install_requires=[
        r'itk>=5.2rc1'
    ]
    )
