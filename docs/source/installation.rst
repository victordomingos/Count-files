Installation and dependencies
-----------------------------

On regular desktop operating systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The current development version can be installed with ``pip install -e``,
followed by the path to the main project directory (the same directory that
has the ``setup.py`` file). To run this application, you need to have a working
Python 3.6+ instalation.

We plan to submit this to PyPI as soon as possible, in order to provide a more
straight-forward instalation and upgrade process. While that doesn't happen,
please feel free to take a look at the last section and maybe consider
contributing to this project.

On iPhone or iPad (in Pythonista 3 for iOS)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First you will need a Python environment and a command-line shell compatible
with Python 3. Presently, it means you need to have an app called
`Pythonista 3 <http://omz-software.com/pythonista/>`_ (which is, among other
things, a very nice environment for developing and/or running pure Python
applications on iOS).

Then you need to install
`StaSh <https://github.com/ywangd/stash>`_, which is a Python-based shell
application for Pythonista. It will enable you to use useful commands like
``wget``, ``git clone``, ``pip install`` and many others. It really deserves an home
screen shortcut on your iPhone or iPad.

After following the instructions for
StaSh installation, you may need to update it to a more recent version. Try
this command::

   selfupdate.py -f bennr01:command_testing

Then force-quit and restart Pythonista and launch StaSh again. It should now
be running in Python 3. You may now try to install this application, directly
from this git repository::

   pip install victordomingos/Count-files

If all goes well, it should place a new ``count_files``
package inside the ``~/Documents/site-packages-3/`` folder and create an
entrypoint script named ``count-files.py`` in ``stash_extensions/bin``. Then force-quit and
launch StaSh again. You should now be able to run this application directly
from the shell to count any files that you may have inside your Pythonista
environment.
