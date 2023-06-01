"""Load Ini File"""

import numpy as np
import re

class IniFileReader:
    """Iniファイル読み込みクラス"""
    def __init__(self, filename):
        self.filename = filename
    
    def read(self):
        f = open(self.filename)
        self.params_list = f.readlines()
        f.close()
        self.params_list = [re.match("(.+)=(.+)", line) for line in self.params_list]
        self.dict = {item[1]:item[2] for item in self.params_list if item}

class ImageProcIniReader(IniFileReader):
    """画像処理Iniファイル読み込みクラス"""

    def deploy(self):
        if (len(self.dict) != 0):
            self.x = self.dict['x']
            self.y = self.dict['y']
            self.thresh = self.dict['threshold']
            self.lena_img_path = self.dict['LenaImagePath']