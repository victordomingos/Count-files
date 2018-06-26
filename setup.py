# encoding: utf-8
from setuptools import setup
import os
import sys


used = sys.version_info
required = (3, 6)

# if version of pip that doesn't understand the python_requires classifier, must be pip >= 9.0.0
# must be built using at least version 24.2.0 of setuptools
# in order for the python_requires argument to be recognized and the appropriate metadata generated
# python -m pip install --upgrade pip setuptools
if used[:2] < required:
    sys.stderr.write("Unsupported Python version: %s.%s. "
                     "Python 3.6 or later is required." % (sys.version_info.major, sys.version_info.minor))
    sys.exit(1)

long_desc = "Count files, grouped by extension, in a directory. By " \
            "default, it will count files recursively in current " \
            "working directory and all of its subdirectories, and " \
            "will display a table showing the frequency for each file " \
            "extension (e.g.: .txt, .py, .html, .css) and the total " \
            "number of files found. Any hidden files or folders " \
            "(those with names starting with '.') are ignored by " \
            "default."
short_desc = "A little command-line interface (CLI) utility " \
             "that helps you count all the files or search for files " \
             "with a certain file extension (or without it) in the specified directory."


def read_readme(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as f:
        return f.read()


setup(name='count-files',
      version=__import__('count_files').__version__,
      description=short_desc,
      packages=['count_files'],
      long_description=read_readme('README.md'),  # for PyPI
      long_description_content_type="text/markdown",
      license='MIT',
      url='https://github.com/victordomingos/Count-files',  # homepage
      python_requires='>=3.6',

      classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux ',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Utilities',
        'Topic :: Desktop Environment :: File Managers',
        'Topic :: System :: Filesystems',

      ],
    
      keywords='file count code analysis cli search extension recursive non-recursive',
      install_requires=[
        'puremagic==1.4',
      ],

      entry_points = {
          'console_scripts': [
              'count-files = count_files.__main__:main_flow'
          ]
      },
      project_urls={
        'Documentation': 'https://github.com/victordomingos/Count-files/docs',
        'Source': 'https://github.com/victordomingos/Count-files',
        'Bug Reports': 'https://github.com/victordomingos/Count-files/issues',
      },
      )
