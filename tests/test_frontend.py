from __future__ import unicode_literals

import unittest

import mock

from mopidy_playbackdefaults import PlaybackDefaultsFrontend


class PlaybackDefaultsFrontendTest(unittest.TestCase):

    def test_no_settings(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        core.tracklist.random = 'untouched'
        core.tracklist.repeat = 'untouched'
        core.tracklist.consume = 'untouched'
        core.tracklist.single = 'untouched'

        PlaybackDefaultsFrontend(config, core)

        self.assertEqual(core.tracklist.random, 'untouched')
        self.assertEqual(core.tracklist.repeat, 'untouched')
        self.assertEqual(core.tracklist.consume, 'untouched')
        self.assertEqual(core.tracklist.single, 'untouched')

    def test_random(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        core.tracklist.random = 'untouched'
        core.tracklist.repeat = 'untouched'
        core.tracklist.consume = 'untouched'
        core.tracklist.single = 'untouched'

        config['playbackdefaults']['default_random'] = True
        PlaybackDefaultsFrontend(config, core)
        self.assertTrue(core.tracklist.random)

        config['playbackdefaults']['default_random'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertFalse(core.tracklist.random)

        self.assertEqual(core.tracklist.repeat, 'untouched')
        self.assertEqual(core.tracklist.consume, 'untouched')
        self.assertEqual(core.tracklist.single, 'untouched')

    def test_repeat(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        core.tracklist.random = 'untouched'
        core.tracklist.repeat = 'untouched'
        core.tracklist.consume = 'untouched'
        core.tracklist.single = 'untouched'

        config['playbackdefaults']['default_repeat'] = True
        PlaybackDefaultsFrontend(config, core)
        self.assertTrue(core.tracklist.repeat)

        config['playbackdefaults']['default_repeat'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertFalse(core.tracklist.repeat)

        self.assertEqual(core.tracklist.random, 'untouched')
        self.assertEqual(core.tracklist.consume, 'untouched')
        self.assertEqual(core.tracklist.single, 'untouched')

    def test_consume(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        core.tracklist.random = 'untouched'
        core.tracklist.repeat = 'untouched'
        core.tracklist.consume = 'untouched'
        core.tracklist.single = 'untouched'

        config['playbackdefaults']['default_consume'] = True
        PlaybackDefaultsFrontend(config, core)
        self.assertTrue(core.tracklist.consume)

        config['playbackdefaults']['default_consume'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertFalse(core.tracklist.consume)

        self.assertEqual(core.tracklist.random, 'untouched')
        self.assertEqual(core.tracklist.repeat, 'untouched')
        self.assertEqual(core.tracklist.single, 'untouched')

    def test_single(self):
        config = {'playbackdefaults': {'default_random': '', 'default_repeat': '', 'default_consume': '', 'default_single': ''}}
        core = mock.Mock()
        core.tracklist.random = 'untouched'
        core.tracklist.repeat = 'untouched'
        core.tracklist.consume = 'untouched'
        core.tracklist.single = 'untouched'

        config['playbackdefaults']['default_single'] = True
        PlaybackDefaultsFrontend(config, core)
        self.assertTrue(core.tracklist.single)

        config['playbackdefaults']['default_single'] = False
        PlaybackDefaultsFrontend(config, core)
        self.assertFalse(core.tracklist.single)

        self.assertEqual(core.tracklist.random, 'untouched')
        self.assertEqual(core.tracklist.repeat, 'untouched')
        self.assertEqual(core.tracklist.consume, 'untouched')
