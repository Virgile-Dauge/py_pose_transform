# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pose_transform',
    packages=find_packages(),
    version='0.2.0',
    description='Mini-Library for handling 3D pose manipulation via'
                ' Transformation matrices',
    author=u'Virgile Daugé & Sylvain Contassot-Vivier',
    author_email='virgile.dauge@pm.me',
    url='https://github.com/virgileTN/py_pose_transform',
    keywords=['3D pose', 'Transformation matrices'],
    install_requires=['numpy', 'numpy-quaternion', 'numba', 'colorama >= 0.4'],
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        ],
)
