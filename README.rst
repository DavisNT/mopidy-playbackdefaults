****************************
Mopidy-PlaybackDefaults
****************************

.. image:: https://img.shields.io/pypi/v/Mopidy-PlaybackDefaults.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-PlaybackDefaults/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-PlaybackDefaults.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-PlaybackDefaults/
    :alt: Number of PyPI downloads

.. image:: https://travis-ci.org/DavisNT/mopidy-playbackdefaults.svg?branch=master
    :target: https://travis-ci.org/DavisNT/mopidy-playbackdefaults
    :alt: Travis-CI build status

.. image:: https://coveralls.io/repos/DavisNT/mopidy-playbackdefaults/badge.svg
    :target: https://coveralls.io/r/DavisNT/mopidy-playbackdefaults
    :alt: Coveralls test coverage

`Mopidy <http://www.mopidy.com/>`_ extension for configurable default playback settings.


Installation
============

Install by running::

    pip install Mopidy-PlaybackDefaults


Configuration
=============

After installing the extension playback defaults can be configured in ``mopidy.conf`` config file (each setting accepts values *true* or *false*, all settings are optional)::

    [playbackdefaults]
    # To set default for Random option (in this case enable it)
    default_random = true

    # To set default for Repeat option (in this case enable it)
    default_repeat = true

    # To set default for Consume option (in this case ensure it is disabled)
    default_consume = false

    # To set default for Single option (in this case ensure it is disabled)
    default_single = false


Usage
=============

During Mopidy startup playback settings will be automatically adjusted according to configuration.

License
=============
::

   Copyright 2016-2020 Davis Mosenkovs

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


Project resources
=================

- `Source code <https://github.com/DavisNT/mopidy-playbackdefaults>`_
- `Issue tracker <https://github.com/DavisNT/mopidy-playbackdefaults/issues>`_
- `Development branch tarball <https://github.com/DavisNT/mopidy-playbackdefaults/archive/develop.tar.gz#egg=Mopidy-PlaybackDefaults-dev>`_


Changelog
=========

v0.1.2
----------------------------------------

- Upgraded to Mopidy 3.0+ and Python 3.7+.

v0.1.1
----------------------------------------

- Changed branching model to `git-flow <http://nvie.com/posts/a-successful-git-branching-model/>`_.
- Changed extension type from ``http:app`` to ``frontend``.
- Improved unit tests.

v0.1.0
----------------------------------------

- Initial release.
