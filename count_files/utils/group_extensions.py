#!/usr/bin/env python3
# encoding: utf-8

ext_and_group_dict = {
    '7z': 'archives',
    'arc': 'archives',
    'arj': 'archives',
    'bz': 'archives',
    'bz2': 'archives',
    'bzip2': 'archives',
    'cab': 'archives',
    'dar': 'archives',
    'gz': 'archives',
    'gzip': 'archives',
    'jar': 'archives',
    'lz': 'archives',
    'lzma': 'archives',
    'rar': 'archives',
    'shar': 'archives',
    'shr': 'archives',
    'tar': 'archives',
    'tbz': 'archives',
    'tbz2': 'archives',
    'tg': 'archives',
    'tgz': 'archives',
    'txz': 'archives',
    'xz': 'archives',
    'zip': 'archives',
    'zipx': 'archives',

    # https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Containers
    '3gp': 'audio/video',
    '3gp2': 'audio/video',
    '3gpp': 'audio/video',
    '3gpp2': 'audio/video',
    'mp4': 'audio/video',
    'mpeg': 'audio/video',
    'mpg': 'audio/video',
    'ogg': 'audio/video',
    'webm': 'audio/video',

    'aac': 'audio',
    'aif': 'audio',
    'aiff': 'audio',
    'amr': 'audio',
    'cda': 'audio',
    'flac': 'audio',
    'mp1': 'audio',
    'mp2': 'audio',
    'mp3': 'audio',
    'm4a': 'audio',
    'mid': 'audio',
    'midi': 'audio',
    'mka': 'audio',
    'mpa': 'audio',
    'oga': 'audio',
    'wav': 'audio',
    'wave': 'audio',
    'wma': 'audio',

    'accdb': 'data',  # Microsoft Access databases
    'accdc': 'data',  # Microsoft Access databases
    'accde': 'data',  # Microsoft Access compiled execute only database
    'csv': 'data',
    'dat': 'data',  # data or resource files, may be anything
    'data': 'data',  # data or resource files
    'database': 'data',  # databases
    'db': 'data',  # databases
    'dbf': 'data',  # databases
    'ini': 'data',  # configuration files
    'cfg': 'data',  # configuration files
    'conf': 'data',  # configuration files
    'geojson': 'data',
    'json': 'data',
    'log': 'data',
    'mdb': 'data',  # databases
    'mysql': 'data',
    'numbers': 'data',  # spreadsheet, Apple Numbers application on Mac OS X (macOS), iOS
    'odb': 'data',  # OpenDocument databases, LibreOffice
    'ods': 'data',  # OpenDocument spreadsheet, LibreOffice
    'pdb': 'data',  # databases
    'sqlite': 'data',  # databases
    'sqlite3': 'data',  # databases
    'sqlitedb': 'data',  # databases
    'topojson': 'data',
    'torrent': 'data',  # configuration files
    'tsv': 'data',  # Tab Separated Values
    'wndb': 'data',
    'xls': 'data',
    'xlsx': 'data',
    'xml': 'data',
    'yaml': 'data',  # configuration files
    'yml': 'data',  # configuration files

    # markup, office
    'abw': 'documents',
    'bib': 'documents',
    'bibtex': 'documents',
    'epub': 'documents',
    'latex': 'documents',
    'ltx': 'documents',
    'markdn': 'documents',
    'markdown': 'documents',
    'md': 'documents',
    'mdown': 'documents',
    'pdf': 'documents',
    'pub': 'documents',
    'rst': 'documents',
    'rtf': 'documents',
    'tex': 'documents',
    'text': 'documents',
    'txt': 'documents',
    # office
    'doc': 'documents',  # many various applications
    'docx': 'documents',  # Microsoft Word
    'odp': 'documents',  # OpenDocument presentation document, LibreOffice
    'ott': 'documents',  # OpenDocument text document, LibreOffice
    'ppt': 'documents',  # Microsoft PowerPoint presentation
    'pptx': 'documents',  # Microsoft PowerPoint presentation

    # executable code, executable file, or executable program, Shell scripts, installation archives
    'action': 'executables',
    'apk': 'executables',
    'app': 'executables',
    'applescript': 'executables',
    'application': 'executables',
    'appref-ms': 'executables',
    'ba_': 'executables',
    'bash': 'executables',
    'bat': 'executables',
    'bin': 'executables',
    'bsh': 'executables',
    'cmd': 'executables',
    'com': 'executables',
    'command': 'executables',
    'csh': 'executables',
    'deb': 'executables',  # installation package
    'elf': 'executables',
    'ex_': 'executables',
    'exe': 'executables',
    'ipa': 'executables',
    'ksh': 'executables',
    'mpkg': 'executables',
    'msi': 'executables',  # Microsoft Windows Installer installation package
    'ps1': 'executables',  # PowerShell
    'ps2': 'executables',
    'psc1': 'executables',
    'psc2': 'executables',
    'run': 'executables',
    'sh': 'executables',
    'tcsh': 'executables',
    'vbe': 'executables',
    'vbs': 'executables',
    'workflow': 'executables',
    'wsf': 'executables',
    'zsh': 'executables',
    #
    'a': 'executables',
    'dll': 'executables',
    'lib': 'executables',
    'o': 'executables',
    'so': 'executables',

    'fon': 'fonts',
    'font': 'fonts',
    'ttf': 'fonts',
    'woff': 'fonts',
    'woff2': 'fonts',

    'apng': 'images',
    'bmp': 'images',
    'dib': 'images',
    'djv': 'images',
    'djvu': 'images',
    'gif': 'images',
    'ico': 'images',
    'icon': 'images',
    'jfif': 'images',
    'jpeg': 'images',
    'jpg': 'images',
    'pic': 'images',
    'pict': 'images',
    'pjp': 'images',
    'pjpeg': 'images',
    'pjpg': 'images',
    'png': 'images',
    'raw': 'images',
    'svg': 'images',
    'svgz': 'images',
    'tif': 'images',
    'tiff': 'images',

    'egg': 'python',
    'egg-info': 'python',
    'egg-link': 'python',
    'epp': 'python',
    'ipy': 'python',
    'ipynb': 'python',
    'npy': 'python',
    'npz': 'python',
    'oog': 'python',
    'p4a': 'python',
    'pck': 'python',
    'pcl': 'python',
    'pickle': 'python',
    'pil': 'python',
    'pth': 'python',
    'pxd': 'python',
    'pxi': 'python',
    'py': 'python',
    'py2': 'python',
    'py3': 'python',
    'py3tb': 'python',
    'pyc': 'python',
    'pyd': 'python',
    'pyde': 'python',
    'pyi': 'python',
    'pym': 'python',
    'pyo': 'python',
    'pyp': 'python',
    'pyproj ': 'python',
    'pyt': 'python',
    'pytb': 'python',
    'pyw': 'python',
    'pyx': 'python',
    'pyz': 'python',
    'pyzw': 'python',
    'rpy': 'python',
    'whl': 'python',

    'asf': 'videos',
    'avchd': 'videos',
    'avi': 'videos',
    'flv': 'videos',
    'h264': 'videos',
    'm4v': 'videos',
    'mkv': 'videos',
    'mov': 'videos',
    'mpv': 'videos',
    'ogm': 'videos',
    'ogv': 'videos',
    'ogx': 'videos',
    'rm': 'videos',
    'rmvb': 'videos',
    'qt': 'videos',
    'qtff': 'videos',
    'swf': 'videos',
    'vob': 'videos',
    'wmv': 'videos'
}
