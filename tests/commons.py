import os
import shutil
import tempfile

from modules.paths import Paths


def get_test_dirname() -> str:
    dirname = os.path.realpath(__file__)
    dirname = os.path.split(dirname)[0]
    return dirname


def prepare_env(suffix, create=True):
    tmp_dir = tempfile.mkdtemp("tmp_", suffix)
    if create:
        Paths.init(tmp_dir)
        os.makedirs(Paths.files)
    return tmp_dir


def restore_env(directory):
    shutil.rmtree(directory, ignore_errors=True)
