# coding=utf-8
import configparser
import os

class ReadConfig:
  def __init__(self,path,node):
    self._cf=self.__load_config(path)
    self.node=node
  def __load_config(self,path):
    cf=configparser.ConfigParser()
    cf.read(path,encoding="UTF-8")
    return cf

  def get_element_value(self,key):
    return self._cf.get(self.node,key)

if __name__ == "__main__":
    config=ReadConfig(path=os.path.join(os.getcwd(),"config/mechaincsOrder.ini"),node="mechaincsDetail")
    result=config.get_element_value("add_shopcart_success_tips")
    print(result)


