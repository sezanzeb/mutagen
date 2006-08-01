import os
import shutil

from tempfile import mkstemp
from tests import TestCase, add
from mutagen.m4a import M4A, Atom

class TM4A(TestCase):
    def setUp(self):
        fd, self.filename = mkstemp(suffix='mp3')
        os.close(fd)
        shutil.copy(self.original, self.filename)
        self.audio = M4A(self.filename)

    def test_length(self):
        self.failUnlessAlmostEqual(3.7, self.audio.info.length, 1)

    def tearDown(self):
        os.unlink(self.filename)

class TM4AHasTags(TM4A):
    original = os.path.join("tests", "data", "has-tags.m4a")

    def test_save_simple(self):
        self.audio.save()

    def test_has_tags(self):
        self.failUnless(self.audio.tags)

add(TM4AHasTags)

class TM4ANoTags(TM4A):
    original = os.path.join("tests", "data", "no-tags.m4a")

    def test_no_tags(self):
        self.failUnless(self.audio.tags is None)

add(TM4ANoTags)