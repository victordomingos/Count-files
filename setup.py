# coding=utf-8
from setuptools import setup

setup(name='countfiles',
      version='1.4',
      packages=['countfiles'],
      entry_points={
          'console_scripts': [
              'countfiles = countfiles.__main__:main_flow'
          ]
      },
      )
