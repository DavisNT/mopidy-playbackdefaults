import os

from mopidy import config, ext

import pykka

__version__ = '0.1.2'


class PlaybackDefaultsExtension(ext.Extension):

    dist_name = 'Mopidy-PlaybackDefaults'
    ext_name = 'playbackdefaults'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(PlaybackDefaultsExtension, self).get_config_schema()
        schema['default_random'] = config.Boolean(optional=True)
        schema['default_repeat'] = config.Boolean(optional=True)
        schema['default_consume'] = config.Boolean(optional=True)
        schema['default_single'] = config.Boolean(optional=True)
        return schema

    def setup(self, registry):
        registry.add('frontend', PlaybackDefaultsFrontend)


class PlaybackDefaultsFrontend(pykka.ThreadingActor):
    def __init__(self, config, core):
        super(PlaybackDefaultsFrontend, self).__init__()

        if type(config[PlaybackDefaultsExtension.ext_name]['default_random']) is bool:
            core.tracklist.set_random(config[PlaybackDefaultsExtension.ext_name]['default_random'])
        if type(config[PlaybackDefaultsExtension.ext_name]['default_repeat']) is bool:
            core.tracklist.set_repeat(config[PlaybackDefaultsExtension.ext_name]['default_repeat'])
        if type(config[PlaybackDefaultsExtension.ext_name]['default_consume']) is bool:
            core.tracklist.set_consume(config[PlaybackDefaultsExtension.ext_name]['default_consume'])
        if type(config[PlaybackDefaultsExtension.ext_name]['default_single']) is bool:
            core.tracklist.set_single(config[PlaybackDefaultsExtension.ext_name]['default_single'])
