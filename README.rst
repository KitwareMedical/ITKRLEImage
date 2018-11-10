ITKRLEImage
===========

.. |CircleCI| image:: https://circleci.com/gh/KitwareMedical/ITKRLEImage.svg?style=shield
    :target: https://circleci.com/gh/KitwareMedical/ITKRLEImage

.. |TravisCI| image:: https://travis-ci.org/KitwareMedical/ITKRLEImage.svg?branch=master
    :target: https://travis-ci.org/KitwareMedical/ITKRLEImage

.. |AppVeyor| image:: https://img.shields.io/appveyor/ci/itkrobot/itkrleimage.svg
    :target: https://ci.appveyor.com/project/itkrobot/itkrleimage

=========== =========== ===========
   Linux      macOS       Windows
=========== =========== ===========
|CircleCI|  |TravisCI|  |AppVeyor|
=========== =========== ===========


Overview
--------

Run-length encoded memory compression scheme for an `ITK <http://itk.org>`_
image.

The module provides run-length encoded storage for image content, iterators
for efficient reading and writing, and a specialization of region of
interest filter which can also be used to convert to and from regular
`itk::Image`.


License
-------

This software is distributed under the Apache 2.0 license. Please see
the *LICENSE* file for details.


Acknowledgements
----------------

This work is supported by NIH grant R01 EB014346, “Continued development and
maintenance of the ITK-SNAP 3D image segmentation software.”
