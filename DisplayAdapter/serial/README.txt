Originally, the 'serial' directory was installed into Project Conway on setup as 'pyserial', but it is not supported by
Python 3, and was breaking every time 'make setup' was run. In order to fix this bug, pyserial was downloaded into the
code so we could fix the bug just once and the fix would stay in place. Only one line of code was added in order to fix
the bug.
The file changes is serialutil.py.

The code in this directory is used under the PSF licence.
