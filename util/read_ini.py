# coding=utf-8

import configparser

import os
class ReadIni(object):
    
    def __init__(self, node="RegisterElement", file_name="E:\\coding\\yangqin\\pythonAuto\\config\\RegisterElement.ini"):
        self.cf = self.load_ini(file_name)
        self.node = node

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        return self.cf.get(self.node, key)


if __name__ == "__main__":
    readIni = ReadIni()
    print('test main')
    print(readIni.get_value("user_email"))
