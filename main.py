#! /usr/bin/env python
"""
MyProject Description
"""

import gettext
import locale
import logging
import sys

from modules.paths import Paths
from modules import __project_name__


CURRENT_LOCALE, _ = locale.getlocale()
if CURRENT_LOCALE == "Italian_Italy":
    CURRENT_LOCALE = "it_IT"
else:
    CURRENT_LOCALE = "en_US"
locale_path = Paths.locales
dictionary = gettext.translation("main", locale_path, [CURRENT_LOCALE])
dictionary.install()
_ = dictionary.gettext


def init_logger():
    FORMAT = "%(asctime)-15s `%(name)s` => '%(message)s'"
    log_file = Paths.file(f"{__project_name__}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format=FORMAT)
    return logging.getLogger("main")


def main(m_logger):
    '''Main function'''
    m_logger.info("Done!")
    print("Done!")


if __name__ == "__main__":
    logger = init_logger()
    logger.info("App Started")

    main(logger)

    logger.info("App Closed")

    sys.exit(0)
