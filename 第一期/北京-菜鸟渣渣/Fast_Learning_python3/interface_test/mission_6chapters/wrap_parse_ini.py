#coding=utf-8

import logging
from datetime import time, date, datetime

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] %(name)s:%(levelname)s: %(message)s")

def info(key):
    logging.info(key)
from  configparser import ConfigParser
import  os

class InIparse:
    def __init__(self,path):
        self.path=path
        self.cf=ConfigParser()

        self.cf.read(self.path, encoding='utf-8') if os.path.exists(path) else exit(0)

    def _addSections(self,sect):
        if self.cf:
            self.cf.add_section(sect)
            return  self.cf.write(open(self.path,"w"),space_around_delimiters=True)

    def _addKeyValue(self,sec,key,values):
        if self.cf:
            self.cf.set(sec,key,values)
            return self.cf.write(open(self.path, "w"), space_around_delimiters=True)


    @property
    def getSections(self): # # 获取sections列表
        if self.cf:
            return  self.cf.sections()
    def getSectItems(self):
        if self.cf:
            return  self.cf.items()

    def getItemkey(self,sec,key):
        if self.cf:
            return  self.cf.get(sec,key)

    def getAllkey(self,key): # 获取指定的section的options列表
        if self.cf:
            if key:
                return self.cf.options(key)
            else:
                info(["getAllkey", None])
        else:
            exit(0)
    def get_section_items(self,section):#根据指定的key 获取参数key对应的value数值
        if self.cf:
            return  self.cf.items(section)
    def update_items(self,section,key,value):
        if self.cf:
            self.cf.set(section,key,value)
            return  self.cf.write(open("ini_data.ini","w"),space_around_delimiters=True)

    def remove_items(self, section, param):
        if self.cf:
            return  self.cf.remove_option(section,param)

        pass


if __name__ == '__main__':
    ini = InIparse("ini_data.ini")
    '''
    ini._addSections("MySQL")
    ini._addKeyValue(sec="MySQL",key="host",values="localhost")
    ini._addKeyValue(sec="MySQL", key="port", values="8888")
    ini._addKeyValue(sec="MySQL", key="datatime", values=str(date.today()))

    ini._addSections("Oracle")
    ini._addKeyValue(sec="Oracle", key="host", values="127.0.0.1")
    ini._addKeyValue(sec="Oracle", key="port", values="8080")
    ini._addKeyValue(sec="Oracle", key="datatime", values=str(date.today()))
    '''



    logging.info(ini.getSections)
    for  section in ini.getSections:
        logging.info(ini.getAllkey(section))
        logging.info(ini.get_section_items(section))
        if section == "mysql":
            logging.info(ini.getItemkey(section,"host"))
            ini.update_items(section,"user","young")
        if section == "MySQL":
            print("-"*15)
            logging.info(ini.getItemkey(section, "datatime"))

            if  "datatime" in section:
                ini.remove_items(section, "datatime")
            if "datatime" in section:
                logging.info("datatime in section")
            else:
                logging.info("datatime Not in section")




        logging.info("*"*50)





    '''
    
    info(ini.getSections)
    info(ini.getAllkey("mysql"))
'''

    # info(ini.get_section_items(ini.get_section_items(sec) for sec in ini.getSections))

