# -*- coding:utf-8-*-

from tkinter import *
import case_office
import case1_stat
import case2_stat

root = Tk()
# 进入消息循环
root.title('图像内容识别技术和对比挖掘在网站分析中的应用研究')
root.geometry('1200x1200')

'''
首页布局设计
'''
lb = Label(root, text='请选择想要进行展示的案例：',fg='black',font=('宋体',42),height=2)
           # width=10,
lb.grid(column = 7, row = 2)   # 设置标签label的位置

lb = Button(root, text='案例一：办公室图像对比',bg='#d3fbfb',fg='red',font=('华文新魏',32),
            width=20,height=2,relief=RAISED,command=case1_stat.Display)
lb.grid(column = 7, row = 4) # 设置button位置

lb = Button(root,text='案例二：酒店图像对比',bg='#d3fbfb',fg='red',font=('华文新魏',32),
            width=20,height=2,relief=RAISED,command=case2_stat.Display)
lb.grid(column = 7, row = 6)   # 设置button位置

col_count, row_count = root.grid_size()
for col in range(0,col_count):
    root.grid_columnconfigure(col, minsize=40)

for row in range(0,row_count):
    root.grid_rowconfigure(row, minsize=40)

root.mainloop()


