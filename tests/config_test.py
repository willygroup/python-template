import shutil
import unittest
import os

# pylint: disable=import-error
from commons import get_dirname, prepare_env, restore_env
from modules.config_mod import Config


class TestConfigodule(unittest.TestCase):

    def test_init_config_with_creation(self):

        tmp_dirs = prepare_env("test_init_config_with_creation")

        config_file = os.path.join(tmp_dirs, "not_existing_conf.json")

        config = Config(config_file)

        self.assertTrue(os.path.isfile(config_file))

        restore_env(tmp_dirs)

    def test_init_config_with_existing_config(self):

        tmp_dirs = prepare_env("test_init_config_with_existing_config")

        src_config = os.path.join(get_dirname(), "files", "config.json")
        dest_config = os.path.join(tmp_dirs, "config.json")

        shutil.copyfile(src_config, dest_config)
        self.assertTrue(os.path.isfile(dest_config))
        config = Config(dest_config)

        self.assertTrue(os.path.isfile(dest_config))

        restore_env(tmp_dirs)

    def test_load_config(self):

        tmp_dirs = prepare_env("test_load_config")

        src_config_1 = os.path.join(get_dirname(), "files", "config.json")
        config_1 = os.path.join(tmp_dirs, "config.json")

        src_config_2 = os.path.join(get_dirname(), "files", "config2.json")
        config_2 = os.path.join(tmp_dirs, "config2.json")

        shutil.copyfile(src_config_1, config_1)
        shutil.copyfile(src_config_2, config_2)

        config = Config(config_1)

        self.assertEqual(config.data.language, 'en')
        self.assertEqual(config.data.datas.data1, 100)

        config.config_file = config_2
        config.load_config()

        self.assertEqual(config.data.language, 'it')
        self.assertEqual(config.data.datas.data1, 1000)

        restore_env(tmp_dirs)


if __name__ == "__main__":
    unittest.main()
