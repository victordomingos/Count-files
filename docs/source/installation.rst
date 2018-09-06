Installation and dependencies
-----------------------------

On regular desktop operating systems
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Count Files is a platform-independent application that runs in Python and
can be easily installed using `pip <https://pip.pypa.io/en/stable/quickstart/>`_::

   pip3 install count-files

If you are interested in the current development version, you can simply clone
this git repository and install it using
`pip3 install -e <https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs>`_.
Please notice, however, that only released versions are expected to be stable
and usable. The development code is often unstable or buggy, for the simple
reason that it is a work in progress.

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
``wget``, ``git clone``, ``pip install`` and many others. It really deserves
an home screen shortcut on your iPhone or iPad.

After following the instructions for StaSh installation, you may need to
update it to a more recent version. Try this command::

   selfupdate.py -f dev

Then force-quit and restart Pythonista and launch StaSh again. It should now
be running in Python 3. You may now try to install this application, directly
from this git repository::

   pip install count-files

If all goes well, it should place a new ``count_files``
package inside the ``~/Documents/site-packages-3/`` folder and create an
entry point script named ``count-files.py`` in ``stash_extensions/bin``. Then
force-quit and launch StaSh again. You should now be able to run this
application directly from the shell to count any files that you may have
inside your Pythonista environment.

If you are interested in the current development version, you can clone
this git repository into your Pythonista environment using StaSh. You can also
install it directly using::

   pip3 install victordomingos/Count-files

Please notice, however, that only released versions are expected to be stable
and usable. The development code is often unstable or buggy, for the simple
reason that it is a work in progress.
