from __future__ import unicode_literals

import os

from mopidy import config, ext

__version__ = '0.1.0'


class PDExtension(ext.Extension):

    dist_name = 'Mopidy-PlaybackDefaults'
    ext_name = 'playbackdefaults'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(PDExtension, self).get_config_schema()
        schema['default_random'] = config.Boolean(optional=True)
        schema['default_repeat'] = config.Boolean(optional=True)
        schema['default_consume'] = config.Boolean(optional=True)
        schema['default_single'] = config.Boolean(optional=True)
        return schema

    def setup(self, registry):
        registry.add(
            'http:app', {'name': self.ext_name, 'factory': self.factory})

    def factory(self, config, core):
        if type(config[PDExtension.ext_name]['default_random']) is bool:
            core.tracklist.random = config[PDExtension.ext_name]['default_random']
        if type(config[PDExtension.ext_name]['default_repeat']) is bool:
            core.tracklist.repeat = config[PDExtension.ext_name]['default_repeat']
        if type(config[PDExtension.ext_name]['default_consume']) is bool:
            core.tracklist.consume = config[PDExtension.ext_name]['default_consume']
        if type(config[PDExtension.ext_name]['default_single']) is bool:
            core.tracklist.single = config[PDExtension.ext_name]['default_single']

        return []
