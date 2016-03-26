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

Mopidy extension for configurable default playback settings.


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

Project resources
=================

- `Source code <https://github.com/DavisNT/mopidy-playbackdefaults>`_
- `Issue tracker <https://github.com/DavisNT/mopidy-playbackdefaults/issues>`_
- `Development branch tarball <https://github.com/DavisNT/mopidy-playbackdefaults/archive/master.tar.gz#egg=Mopidy-PlaybackDefaults-dev>`_


Changelog
=========

v0.1.0
----------------------------------------

- Initial release.
