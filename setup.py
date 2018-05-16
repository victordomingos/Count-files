# coding=utf-8
from setuptools import setup

long_desc = "Count files, grouped by extension, in a directory. By " \
            "default, it will count files recursively in current " \
            "working directory and all of its subdirectories, and " \
            "will display a table showing the frequency for each file " \
            "extension (e.g.: .txt, .py, .html, .css) and the total " \
            "number of files found. Any hidden files or folders " \
            "(those with names starting with '.') are ignored by " \
            "default."

setup(name='countfiles',
      version = '1.4',
      description = 'Count files, grouped by extension, in a directory.',
      packages = ['countfiles'],
      long_description = long_desc,
      license = 'Attiribution-ShareAlike 4.0 International (CC BY-SA 4.0)',

      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
      ],
    
      keywords='file count code analysis',
      install_requires=[
        'puremagic==1.4',
      ],

      entry_points = {
          'console_scripts': [
              'countfiles = countfiles.__main__:main_flow'
          ]
      },
      )
