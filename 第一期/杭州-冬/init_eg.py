#--codingg:utf-8--
#一个简单的ini文件操作类
class  Iniding:
    #定义一个dict sec_part-存放section option value
    def __init__(self,sec_part={}):
        self.sec_part=sec_part
        
    #增加一个section
    def add_secton(self,sec_name):
        self.sec_part[sec_name]={}

    #增加 section中的 option-value键值对
    def set(self,sec_name2,opt_name2,val_name2):
        #opt_val为一个dict--存放section对应的 option和value
        opt_val=self.sec_part[sec_name2]
        opt_val[opt_name2]=val_name2

    #以列表的形式获取所有的section
    def sections(self):
        return self.sec_part.keys()

    #获取指定sectionde option
    def options(self,sec_name3):
        opt_value= self.sec_part.get(sec_name3)
        return opt_value.keys()

        #获取section中的option值 str类型
    def get(self,sec_name4,opt_name4):
        return str(self.sec_part[sec_name4][opt_name4])

if __name__=="__main__":
    inidingone=Iniding()
    inidingone.add_secton("第一部分")
    inidingone.add_secton("第三部分")
    inidingone.set("第一部分","第一章","第一节")
    inidingone.set("第一部分","第二章","第二节")
    inidingone.set("第三部分","第三章","第三节")
    print(inidingone.sections())
    print(inidingone.options("第三部分"))
    print(inidingone.get("第三部分","第三章"))
