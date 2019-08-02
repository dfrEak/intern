# ref
# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

import configparser
from pathlib import Path

class config:
    """
    config class
    """

    # parameter
    # パラメータ
    config = configparser.ConfigParser()

    config.read((Path(__file__).absolute().parent / "conf.ini").as_posix())

    # set the path
    # パスを設定
    config['DOWNLOAD']['FOLDER']=str(Path(__file__).parent.parent / config['DOWNLOAD']['FOLDER'])
    config['CRAWL']['FILENAME']=str(Path(__file__).parent.parent / config['CRAWL']['FILENAME'])

    def __init__(self):
        pass


if __name__ == "__main__":
    print(str(Path(__file__).parent.parent))
    print(config.config['DOWNLOAD']['FOLDER'])
    print(config.config['CRAWL']['FILENAME'])
