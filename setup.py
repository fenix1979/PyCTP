# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 14:39:27 2016

@author: zhuolin
"""

import platform
from setuptools import setup
from setuptools.extension import Extension
from os.path import join, split, dirname

headers = ['stdafx.h', 'UserApiDataType.h', 'UserApiStruct.h', 'MdApi.h', 'TraderApi.h']
sources = ['stdafx.cpp', 'PyCTP.cpp', 'UserApiDataType.cpp', 'UserApiStruct.cpp', 'MdApi.cpp', 'TraderApi.cpp']

sources = [join('.', 'src', file) for file in sources]
depends = [join('.', 'src', file) for file in headers]

optional = {}
if platform.system() == 'Linux':
    optional['extra_compile_args'] = ['-std=c++11']
    optional['runtime_library_dirs'] = ['./']
    optional['include_dirs']=['./v6.3.15_20190220_api_tradeapi_se_linux64']
    optional['library_dirs']=['./v6.3.15_20190220_api_tradeapi_se_linux64']
if platform.system() == 'Windows':
    if '64 bit' in platform.python_compiler():
        optional['include_dirs'] = ['./v6.3.15_20190220_tradeapi64_se_windows']
        optional['library_dirs'] = ['./v6.3.15_20190220_tradeapi64_se_windows']
    else:
        optional['include_dirs'] = ['./v6.3.15_20190220_tradeapi_se_windows']
        optional['library_dirs'] = ['./v6.3.15_20190220_tradeapi_se_windows']
argments = dict(name='PyCTP',
                sources=sources,
                language='c++',
                libraries=['thostmduserapi_se', 'thosttraderapi_se'],
                extra_link_args=['-Wl,-rpath,/usr/local/lib/CTP'],
                depends=depends)
argments.update(optional)

setup(name='PyCTP',
      version='1.1.1',
      description='CTP for Python',
      long_description='CTP v6.3.15_20190220 for Python',
      author='Shi Zhuolin',
      author_email='shizhuolin@hotmail.com',
      url='http://www.pyctp.org/',
      keywords=['ctp','futures','stock'],
      license='LGPL-3.0',
      platforms=['linux-x86_64','win32','win-amd64'],
      ext_modules=[Extension(**argments)]
      )
