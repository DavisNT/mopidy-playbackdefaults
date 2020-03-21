import unittest

import mock

from mopidy_playbackdefaults import PlaybackDefaultsExtension, PlaybackDefaultsFrontend


class PlaybackDefaultsExtensionTest(unittest.TestCase):

    def test_get_default_config(self):
        ext = PlaybackDefaultsExtension()

        config = ext.get_default_config()

        self.assertIn('[playbackdefaults]', config)
        self.assertIn('enabled = true', config)
        self.assertIn('default_random =', config)
        self.assertIn('default_repeat =', config)
        self.assertIn('default_consume =', config)
        self.assertIn('default_single =', config)

    def test_get_config_schema(self):
        ext = PlaybackDefaultsExtension()

        schema = ext.get_config_schema()

        # WARNING! Configuration element types not tested
        self.assertIn('default_random', schema)
        self.assertIn('default_repeat', schema)
        self.assertIn('default_consume', schema)
        self.assertIn('default_single', schema)

    def test_setup(self):
        registry = mock.Mock()

        ext = PlaybackDefaultsExtension()
        ext.setup(registry)

        registry.add.assert_called_once_with('frontend', PlaybackDefaultsFrontend)
