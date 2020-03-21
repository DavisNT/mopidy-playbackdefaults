import re

from setuptools import find_packages, setup


def get_version(filename):
    content = open(filename).read()
    metadata = dict(re.findall("__([a-z]+)__ = '([^']+)'", content))
    return metadata['version']


setup(
    name='Mopidy-PlaybackDefaults',
    version=get_version('mopidy_playbackdefaults/__init__.py'),
    url='https://github.com/DavisNT/mopidy-playbackdefaults',
    license='Apache License, Version 2.0',
    author='Davis Mosenkovs',
    author_email='python-apps@dm.id.lv',
    description='Mopidy extension for configurable default playback settings.',
    long_description=open('README.rst').read(),
    packages=find_packages(exclude=['tests', 'tests.*']),
    zip_safe=False,
    include_package_data=True,
    python_requires='>= 3.7',
    install_requires=[
        'setuptools',
        'Mopidy >= 3.0',
        'Pykka >= 1.1',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock >= 1.0',
    ],
    entry_points={
        'mopidy.ext': [
            'playbackdefaults = mopidy_playbackdefaults:PlaybackDefaultsExtension',
        ],
    },
    classifiers=[
        'Environment :: No Input/Output (Daemon)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Sound/Audio :: Players',
    ],
)
