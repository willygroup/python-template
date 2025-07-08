# pylint: disable=import-error, disable=broad-except disable=missing-module-docstring, disable=missing-class-docstring, disable=missing-function-docstring, disable=duplicate-code


import os
import unittest


from tests.commons import (
    prepare_env,
    restore_env,
)
from modules.paths import Paths


class TestPathsMethods(unittest.TestCase):
    '''
    Testing Paths
    '''

    def test_init(self):
        '''
        Init method test
        '''

        tmp_dir = prepare_env("paths_init", False)

        try:
            Paths.init(tmp_dir)

            self.assertEqual(Paths.base, tmp_dir)

        except (Exception,) as e:
            print(e)
            self.fail()

        finally:
            restore_env(tmp_dir)

    def test_image(self):
        '''
        image method test
        '''

        tmp_dir = prepare_env("paths_image")

        try:
            self.assertEqual(Paths.image("image.png"),
                             os.path.join(tmp_dir, "files", "images", "image.png"))

        except (Exception,) as e:
            print(e)
            self.fail()

        finally:
            restore_env(tmp_dir)

    def test_locale(self):
        '''
        locale method test
        '''

        tmp_dir = prepare_env("paths_locale")

        try:
            self.assertEqual(Paths.locale("file"),
                             os.path.join(tmp_dir, "files", "locale", "file"))

        except (Exception,) as e:
            print(e)
            self.fail()

        finally:
            restore_env(tmp_dir)

    def test_file(self):
        '''
        file method test
        '''

        tmp_dir = prepare_env("paths_file")

        try:
            self.assertEqual(Paths.file("file"),
                             os.path.join(tmp_dir, "files", "file"))

        except (Exception,) as e:
            print(e)
            self.fail()

        finally:
            restore_env(tmp_dir)
