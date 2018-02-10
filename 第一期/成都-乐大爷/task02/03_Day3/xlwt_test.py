# -*- coding:utf-8 -*-

__author__ = 'catleer'

import xlwt

"""
参考资料：http://blog.csdn.net/ngforever/article/details/14225495

font:字体

pattern:底部颜色
pattern = xlwt.Pattern() # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN,SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black,1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7= Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = DarkYellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = LightGray, 23 = Dark Gray, the list goes on...

borders:表格框线
borders = xlwt.Borders() # Create Borders
borders.left = xlwt.Borders.MEDIUM_DASHED  # May be: NO_LINE, THIN, MEDIUM,DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED,THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through0x0D.
borders.right = xlwt.Borders.MEDIUM_DASHED 
borders.top = xlwt.Borders.MEDIUM_DASHED 
borders.bottom = xlwt.Borders.MEDIUM_DASHED 
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

alignment：居中、居左、居右
alignment = xlwt.Alignment() # Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL,HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP,VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

问题：既想要表格框线又想所有数据居中应该怎么操作？首行有底色

"""

wb = xlwt.Workbook()
ws1 = wb.add_sheet('Python')

alignment = xlwt.Alignment() # Create Alignment
alignment.horz = xlwt.Alignment.HORZ_CENTER # May be: HORZ_GENERAL,HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = xlwt.Alignment.VERT_CENTER # May be: VERT_TOP,VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED

pattern = xlwt.Pattern() # Create the Pattern
pattern.pattern = xlwt.Pattern.SOLID_PATTERN # May be: NO_PATTERN,SOLID_PATTERN, or 0x00 through 0x12
pattern.pattern_fore_colour = 5 # May be: 8 through 63. 0 = Black,1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7= Cyan, 16 = Maroon, 17 = Dark Green, 18 = Dark Blue, 19 = DarkYellow , almost brown), 20 = Dark Magenta, 21 = Teal, 22 = LightGray, 23 = Dark Gray, the list goes on...

borders = xlwt.Borders() # Create Borders
borders.left = xlwt.Borders.MEDIUM_DASHED  # May be: NO_LINE, THIN, MEDIUM,DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED,THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED,MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through0x0D.
borders.right = xlwt.Borders.MEDIUM_DASHED 
borders.top = xlwt.Borders.MEDIUM_DASHED 
borders.bottom = xlwt.Borders.MEDIUM_DASHED 
borders.left_colour = 0x40
borders.right_colour = 0x40
borders.top_colour = 0x40
borders.bottom_colour = 0x40

style = xlwt.XFStyle() # Create the Style
style.alignment = alignment
style.pattern = pattern
style.borders = borders
# style.alignment = alignment # Apply the Font to the Style



L = ['序号' , '书名', '作者', '出版日期', '评分', '价格', '简介']
for i in range(len(L)):
    ws1.write(0,i,L[i],style)
    

ws2 = wb.add_sheet('other')

# 表头信息写入
# 怎么让数据进行居中显示
for i in range(len(L)):
    ws2.write(0,i,L[i],style)

wb.save('books.xls')
