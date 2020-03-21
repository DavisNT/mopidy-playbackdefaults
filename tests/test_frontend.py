import unittest

import mock

from mopidy_playbackdefaults import PlaybackDefaultsFrontend


class PlaybackDefaultsFrontendTest(unittest.TestCase):

    def test_no_settings(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

        PlaybackDefaultsFrontend(config, core)

        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

    def test_random(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

        config['playbackdefaults']['default_random'] = True
        PlaybackDefaultsFrontend(config, core)
        core.tracklist.set_random.assert_called_once_with(True)

        config['playbackdefaults']['default_random'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertEqual(core.tracklist.set_random.call_count, 2)
        core.tracklist.set_random.assert_called_with(False)

        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

    def test_repeat(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

        config['playbackdefaults']['default_repeat'] = True
        PlaybackDefaultsFrontend(config, core)
        core.tracklist.set_repeat.assert_called_once_with(True)

        config['playbackdefaults']['default_repeat'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertEqual(core.tracklist.set_repeat.call_count, 2)
        core.tracklist.set_repeat.assert_called_with(False)

        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

    def test_consume(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

        config['playbackdefaults']['default_consume'] = True
        PlaybackDefaultsFrontend(config, core)
        core.tracklist.set_consume.assert_called_once_with(True)

        config['playbackdefaults']['default_consume'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertEqual(core.tracklist.set_consume.call_count, 2)
        core.tracklist.set_consume.assert_called_with(False)

        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

    def test_single(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
        self.assertEqual(core.tracklist.set_single.call_count, 0)

        config['playbackdefaults']['default_single'] = True
        PlaybackDefaultsFrontend(config, core)
        core.tracklist.set_single.assert_called_once_with(True)

        config['playbackdefaults']['default_single'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertEqual(core.tracklist.set_single.call_count, 2)
        core.tracklist.set_single.assert_called_with(False)

        self.assertEqual(core.tracklist.set_random.call_count, 0)
        self.assertEqual(core.tracklist.set_repeat.call_count, 0)
        self.assertEqual(core.tracklist.set_consume.call_count, 0)
