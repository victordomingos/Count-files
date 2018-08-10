How to use
----------


CLI arguments
^^^^^^^^^^^^^

Arguments can be specified in both short and long form. For example: ``-a`` or ``--all``.
::

   usage: count-files [-h] [-v] [-st] [-a]
                      [-c] [-nr] [-nf]
                      [-t TOTAL] [-alpha]
                      [-fe FILE_EXTENSION] [-fs]
                      [-p] [-ps PREVIEW_SIZE] [path]


   usage: count-files [--help] [--version] [--supported-types] [--all]
                      [--case-sensitive] [--no-recursion] [--no-feedback]
                      [--total TOTAL] [--sort-alpha]
                      [--file-extension FILE_EXTENSION] [--file-sizes]
                      [--preview] [--preview-size PREVIEW_SIZE] [path]

Common arguments
""""""""""""""""

``path``, ``--all``, ``--case-sensitive``, ``--no-recursion``, ``--no-feedback``

Special arguments
"""""""""""""""""

* File counting by extension (sorted table):
   ``--sort-alpha``

* File searching by extension (list with file paths):
   ``--file-extension``, ``--file-sizes``, ``--preview``, ``--preview-size``

* Total counting of files (total number):
   ``--total``

Getting help
^^^^^^^^^^^^

To check the list of available options and their usage, you just need to use
one of the following commands::

   count-files -h

   count-files --help

Check the version number of the program::

   count-files -v
   
   count-files --version

Get the list of currently supported file types for preview::

   count-files -st
   
   count-files --supported-types

.. _path-label:

The ``path`` argument
^^^^^^^^^^^^^^^^^^^^^

Optionally, you can pass it a path to the directory to scan. If you prefer, you
can leave that argument empty, and it will scan the current working directory.

To process files in the user's home directory, you can use ``~`` (tilde).

If there are spaces in the folder names, then ``path`` should be specified in quotation marks. For example, in Windows: ``count-files "~\Desktop\New folder"``

.. _non-recursive-label:

Non-recursive search or counting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The optional ``-nr`` or ``--no-recursion`` switch argument tells the
application not to scan recursively through the subdirectories.

.. _hidden-label:

Hidden files and directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, it will ignore files and directories that are supposed to be
hidden, but you can add the ``-a`` or ``--all`` optional
switch argument to make it count or search for all files.

Windows: files and directories for which ``FILE_ATTRIBUTE_HIDDEN`` is true

Linux, Mac OS: those with names starting with ``.`` (dot)


.. _case-sensitivity-label:

Case sensitivity
^^^^^^^^^^^^^^^^

The names of extensions are case insensitive by default. The results for
``ini`` and ``INI`` will be the same. To distinguish between similar
extensions in different cases, use the ``-c`` or ``--case-sensitive`` switch
argument.

* File counting by extension (sorted table):

   In this case, the file extensions in the table will be displayed as is (in lowercase and uppercase).

* File searching by extension (using ``-fe`` or ``--file-extension``):

   The result of the search will be a list with paths to files with an extension in the corresponding register.

* Total counting of files (using ``-t`` or ``--total``):

   For total counting of files with a specific extension, this option is also available.

.. _feedback-label:

Customizing operation feedback
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The program's operating indicator is printing processed file names in one line.
File names are not displayed when searching for a particular extension, if
there are no such files in the folder or if the files are hidden, and the
argument ``--all`` is not specified.

Feedback is available by default for counting files by extension 
and for counting the total number of files(using ``-t`` or ``--total``). Optional
argument ``-nf`` or ``--no-feedback`` disables it.

Using the ``--no-feedback`` argument allows you to speed up the
processing of files a little.

To search for files by extension (using ``-fe`` or ``--file-extension``) feedback is the list itself.

File counting by extension
^^^^^^^^^^^^^^^^^^^^^^^^^^

To count all files by extension, you can simply use the command ``count-files`` and, if necessary, specify common arguments: ``path``, ``--all``, ``case-sensitive``, ``--no-recursion``, ``--no-feedback``.

.. seealso:: :ref:`count-label`

The ``--sort-alpha`` argument
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, result of file counting by extension is a table showing the frequency for each file extension. To sort the extensions alphabetically, use the ``-alpha`` or ``--sort-alpha`` argument.

File searching by extension
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another main feature of this application consists in searching files by a given extension, which presents to the user a list of all found files.

Using ``-fe`` or ``--file-extension`` argument, you can find all the files with the specified extension.

.. seealso:: :ref:`search-label`

Total counting of files
^^^^^^^^^^^^^^^^^^^^^^^

To count the total number of all files, the number of files with a specific extension or without it
you can use the ``-t`` or ``--total`` argument and specify the name of the extension.

.. seealso:: :ref:`total-label`

Preview text files
^^^^^^^^^^^^^^^^^^

Preview is available for searching files using the ``-fe`` or ``--file-extension`` argument.

The default preview size depends on the terminal width settings.
You can change this value by specifying the argument ``-p`` or ``--preview-size`` and an integer (the required number of characters).

Example: ``count-files --file-extension css --preview --preview-size 50``

File sizes
^^^^^^^^^^

You can get additional information about the size of each file using the ``-fs`` or ``--file-sizes`` argument. This option is available for searching files using the ``-fe`` or ``--file-extension`` argument.

Example: ``count-files --file-extension js --file-sizes``

