#!/usr/bin/env python3
# encoding: utf-8
"""Files that may be text.
Contain official registered types by IANA
(https://www.iana.org/assignments/media-types/media-types.xhtml)
and not registered types
(text, developer file extensions)
"""


text_extensions_and_mime_types = {
    'py': '',  # Python Script, application/x-python-code, text/x-python, text/plain
    'pyw': '',  # Windows Python GUI Source File
    'php': '',  # PHP, application/x-httpd-php, text/php, application/php, magnus-internal/shellcgi, application/x-php
    'bat': '',  # DOS Batch File, text/plain
    'cmd': '',  # Windows Command File, Files similar in functionality to BAT file format, text/plain
    'vbs': '',  # VBScript File
    'cs': '',  # C# Source Code File
    'erl': '',  # Erlang Source Code File
    'lua': '',  # Lua Source File
    'ejs': '',  # application/javascript Embedded Java Script
    'mjs': '',  # application/javascript Node.js ES Module File
    # Windows Initialization File: text/plain, application/textedit, zz-application/zz-winassoc-ini
    # Finale Preferences File, Symbian OS Configuration File, Gravis UltraSound Bank Setup File
    'ini': '',  # text/plain
    'xml': '',  # Extensible Markup Language
    'md': '',  # Text Markdown or some binary media files
    'mdown': '',  # text/markdown
    'markdn': '',  # text/markdown
    'markdown': '',  # text/markdown
    'rst': '',  # reStructuredText File
    'yml': '',  # YAML Document application/x-yaml
    'yaml': '',  # YAML Document application/x-yaml
    'latex': '',  # LaTeX Document
    'ltx': '',  # LaTeX Document
    'qss': '',  # Qt Style Sheet

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
    'conf': 'text/plain',
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
}  # 95

"""
Python Software Foundation:
py   Python Script, python.exe
pyc  Python Compiled File
pyw  Windows Python GUI Source File, pythonw.exe
pyo  Python Optimized Code
pyz  Python Archive File, application/x-zip-compressed
pyzw Python Archive File, application/x-zip-compressed
pyt  Python declaration data
npy	 Python NumPy Array File	
pyd	 Python Dynamic Module
rpy  Python Script
whl  Python Wheel Package, Compressed Files
oog  related to Object Oriented Graphics (OOG) in PyGraph -  Python Graphics Interface
p4a  Python script, optimized for Google Android system and apps
pil  Python Image Library font
pth  Python path configuration
pym  Python preprocessor macro
ssdf Simple Structured Data Format, scientific data Python or Matlab
pickle Python Pickle data
egg
egg-info
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
