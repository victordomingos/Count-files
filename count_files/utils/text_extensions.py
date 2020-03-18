#!/usr/bin/env python3
# encoding: utf-8
"""Files that may be text.
Contain official registered types by IANA
(https://www.iana.org/assignments/media-types/media-types.xhtml)
and not registered types
(text, developer file extensions)
"""


text_extensions_and_mime_types = {
    'ipy': '',  # IPython Script, text/plain
    'ipynb': '',  # Jupyter Notebook Files, text/plain, actually json-based
    'pxd': '',  # Cython, Pyrex Definition File, text/plain
    'pxi': '',
    'py': '',  # Python Script, application/x-python-code, text/x-python, text/plain
    'py3': '',  # Python Script
    'py3tb': '',
    'pyde': '',
    'pyi': '',  # Stub Files, text/plain
    'pyp': '',
    'pyproj': '',  # Microsoft Visual Studio Python project(xml)
    'pyt': '',  # Python Toolbox, text/plain
    'pytb': '',
    'pyw': '',  # Windows Python GUI Source File
    'pyx': '',  # Cython, Pyrex Source Code File, text/plain
    'rpy': '',  # Python Script, Ren'Py Script - text/plain, may be Touhou Project Replay File

    'bat': '',  # DOS Batch File, text/plain
    'cfg': '',  # Configuration/Settings Files, may be saved in a text format, Windows and Macintosh systems
    'cmd': '',  # Windows Command File, Files similar in functionality to BAT file format, text/plain
    'cs': '',  # C# Source Code File
    'dart': '',  # Dart Source Code File, text/plain
    'ejs': '',  # application/javascript Embedded Java Script
    'erl': '',  # Erlang Source Code File
    'go': '',  # Go Source Code File, text/plain
    # Windows Initialization File: text/plain, application/textedit, zz-application/zz-winassoc-ini
    # Finale Preferences File, Symbian OS Configuration File, Gravis UltraSound Bank Setup File
    'ini': '',  # text/plain
    'latex': '',  # LaTeX Document
    'lisp': '',  # Lisp Source Code File, text/plain
    'ltx': '',  # LaTeX Document
    'lua': '',  # Lua Source File
    'markdn': '',  # text/markdown
    'markdown': '',  # text/markdown
    'md': '',  # Text Markdown or some binary media files
    'mdown': '',  # text/markdown
    'mjs': '',  # application/javascript Node.js ES Module File
    'nim': '',  # Nim Source File
    'nimble': '',  # Nim Package File
    'php': '',  # PHP, application/x-httpd-php, text/php, application/php, magnus-internal/shellcgi, application/x-php
    'qss': '',  # Qt Style Sheet
    'rst': '',  # reStructuredText File
    'sh': '',  # Bash Shell Script - text/plain, or Unix Shell Archive(Compressed Files, .shar)
    'vbs': '',  # VBScript File
    'xml': '',  # Extensible Markup Language
    'yaml': '',  # YAML Document application/x-yaml
    'yml': '',  # YAML Document application/x-yaml

    # http://svn.apache.org/viewvc/httpd/httpd/trunk/docs/conf/mime.types?view=markup
    # Fri Sep 29 15:10:29 2017 UTC
    'pl': 'text/plain',  # Perl or Prolog, text/x-script.perl, application/x-perl, application/perlscript
    'shtml': 'text/html',
    'js': 'application/javascript',  # Java Script or JScript Executable Script Microsoft
    'json': 'application/json',  # json
    'tcl': 'application/x-tcl',  # Tcl Script
    'tex': 'application/x-tex',  # mostly LaTeX Source Document, or some binaries Texture File, Raster Image Files
    'appcache': 'text/cache-manifest',
    'ics': 'text/calendar',
    'ifb': 'text/calendar',
    'css': 'text/css',
    'csv': 'text/csv',
    'html': 'text/html',
    'htm': 'text/html',
    'n3': 'text/n3',
    'txt': 'text/plain',
    'text': 'text/plain',
    'conf': 'text/plain',  # Configuration/Settings Files, may be saved in a text format, Unix and Linux based systems
    'def': 'text/plain',
    'list': 'text/plain',
    'log': 'text/plain',
    'in': 'text/plain',
    'dsc': 'text/prs.lines.tag',
    'rtx': 'text/richtext',
    'sgml': 'text/sgml',
    'sgm': 'text/sgml',
    'tsv': 'text/tab-separated-values',
    't': 'text/troff',
    'tr': 'text/troff',
    'roff': 'text/troff',
    'man': 'text/troff',
    'me': 'text/troff',
    'ms': 'text/troff',
    'ttl': 'text/turtle',
    'uri': 'text/uri-list',
    'uris': 'text/uri-list',
    'urls': 'text/uri-list',
    'vcard': 'text/vcard',
    'curl': 'text/vnd.curl',
    'dcurl': 'text/vnd.curl.dcurl',
    'mcurl': 'text/vnd.curl.mcurl',
    'scurl': 'text/vnd.curl.scurl',
    'fly': 'text/vnd.fly',
    'flx': 'text/vnd.fmi.flexstor',
    'gv': 'text/vnd.graphviz',
    '3dml': 'text/vnd.in3d.3dml',
    'spot': 'text/vnd.in3d.spot',
    'jad': 'text/vnd.sun.j2me.app-descriptor',
    'wml': 'text/vnd.wap.wml',
    'wmls': 'text/vnd.wap.wmlscript',
    's': 'text/x-asm',
    'asm': 'text/x-asm',
    'c': 'text/x-c',  # C
    'cc': 'text/x-c',
    'cxx': 'text/x-c',  # C++
    'cpp': 'text/x-c',
    'h': 'text/x-c',
    'hh': 'text/x-c',
    'dic': 'text/x-c',
    'f': 'text/x-fortran',  # Fortran
    'for': 'text/x-fortran',
    'f77': 'text/x-fortran',
    'f90': 'text/x-fortran',
    'java': 'text/x-java-source',  # Java
    'nfo': 'text/x-nfo',
    'opml': 'text/x-opml',
    'p': 'text/x-pascal',  # Pascal
    'pas': 'text/x-pascal',  # Delphi Unit Source File, Pascal Source File
    'etx': 'text/x-setext',
    'sfv': 'text/x-sfv',
    'uu': 'text/x-uuencode',
    'vcs': 'text/x-vcalendar',
    'vcf': 'text/x-vcard',
}  # 116

"""
Python related extensions:
py_ext = {
    'egg': 'Python egg metadata, regenerated from source files by setuptools',
    'egg-info': 'Python egg metadata, regenerated from source files by setuptools',
    'egg-link': 'Python Egg Link',
    'epp': 'Python Egg data',
    'ipy': 'IPython script',
    'ipynb': 'IPython notebook, Jupyter Notebook',
    'npy': 'Python NumPy Array File, binary',
    'npz': 'A .npz file is a zip file containing multiple .npy files, one for each array (zipped archive).',
    'oog': 'related to Object Oriented Graphics (OOG) in PyGraph -  Python Graphics Interface',
    'p': 'Python module, that is converted by process called "picking"',
    'p4a': 'Python script, optimized for Google Android system and apps',
    'pickle': 'Python Pickle data, application/octet-stream, also *.pck, *.pcl, *.pkl(in Python 2)',
    'pil': 'Python Image Library font',
    'pth': 'Python path configuration, '
           'also: common PyTorch convention is to save models using either a .pt or .pth file',
    'pxd': 'Cython, Pyrex Definition File(like C/C++ header) or Pixlr Layered Image(binary)',
    'pxi': 'Pyrex header',
    'py': 'Python Script, python.exe',
    'py2': 'text',
    'py3': 'text',
    'py3tb': 'Python traceback, text',
    'pyc': 'Python Compiled File, Python byte code',
    'pyd': 'Python Dynamic Module, an equivalent of DLL format (dynamic link library), Binary',
    'pyde': 'text',
    'pyi': 'Stub Files, https://www.python.org/dev/peps/pep-0561/#stub-only-packages, '
           'files containing only type information(Type Hints, mypy), empty of runtime code',
    'pym': 'Python preprocessor macro',
    'pyo': 'Python Optimized Code, Compiled Python File, Python byte code',
    'pyp': 'AllPlan PythonParts, xml file',
    'pyproj': 'Microsoft Visual Studio Python project(xml)',
    'pyt': 'Python declaration data, Python Toolbox',
    'pytb': 'Python traceback, text',
    'pyw': 'Windows Python GUI Source File, pythonw.exe',
    'pyx': 'Cython, Pyrex Source Code File',
    'pyz': 'Python Archive File, application/x-zip-compressed',
    'pyzw': 'Python Archive File, application/x-zip-compressed',
    're': 'Python Regular Expressions source code',
    'rpy': "Python Script, Ren'Py Script",
    'ssdf': 'Simple Structured Data Format, scientific data Python or Matlab',
    'whl': 'Python Wheel Package, Compressed Files'
}
https://setuptools.readthedocs.io/en/latest/formats.html
"""

"""
Initialize the internal data structures. 
If given, files must be a sequence of file names which should be used to augment the default type map. 
If omitted, the file names to use are taken from knownfiles; 
on Windows, the current registry settings are loaded. 
Each file named in files or knownfiles takes precedence over those named before it. 
Calling init() repeatedly is allowed.
import mimetypes
mimetypes.init(files=None)
Also: 'gitmodules': 'text/plain', 'gitignore': 'text/plain', 'gitattributes': 'text/plain'
"""
