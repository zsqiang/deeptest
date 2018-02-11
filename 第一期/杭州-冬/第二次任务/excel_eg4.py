#--coding:utf-8
#再次练习封装一个 excel 

import os
from openpyxl import Workbook
from openpyxl import load_workbook

class Myopenpyxl:
    #初始化：用来控制对象的初始化状态在实例化一个对象时自动调用   常用来设置对象属性 初始值
    def __init__(self,file_path):
        if os.path.exists(file_path):
            self.wb=load_workbook(file_path)
        else:
            print("找不到给定的文件")
            exit(0)     #找不到文件则中断程序

    #返回所有工作簿的名称
    def myget_sheetsname(self):
        if self.wb: #若存在excel文件且被正确读取进来则为true
            return self.wb.get_sheet_names()
        return None
        
    #返回指定工作簿
    def myget_sheet_by_name(self,sheet_name):
        if self.wb:
            return self.wb.get_sheet_by_name(sheet_name)
        return None

    ##返回指定sheet的cell的边界范围
    def myboundcell(self,shee_tname):
        if self.wb:
            return self.wb[sheet_name].calculate_dimension()
        return None

    #遍历返回cell的值
    def myvalue(self,sheet_name,minrow,maxrow,mincol,maxcol):
        
        if self.wb:
            row_range=self.wb[sheetname].iter_rows(min_row=minrow,max_row=maxrow,min_col=mincol,max_col=maxcol)
            for row in row_range:
                for cell in row:
                    return cell.value
        return None
    #修改工作簿名 修改成功则返回true
    def set_sheet_name(self,sheet_name,name)
        status=False    #定义一个变量 用以确定是否修改成功
        if self.wb:
            self.wb[sheet_name].title=name
            status=True
        return status   #在未修改成功或wb不存在时返False
    #设置cell值
    def set_cell_value(self,sheet_name,row,col,value):
        status=False
        if self.wb:
            self.wb[sheet_name].cell(row=row,column=col,value=value)
            status=True
        
        return False
    #保存文件
    def mysave(self,filename):
        status=False
        if filename !='' and self.wb:
            self.wb.save(filename)
            status=True
        return status

